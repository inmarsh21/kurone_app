from flask import Flask, request, abort
import os
from dotenv import load_dotenv # type: ignore

from linebot.v3.messaging import Configuration, MessagingApi, ApiClient
from linebot.v3.webhook import WebhookHandler
from linebot.v3.webhooks import MessageEvent, TextMessageContent, StickerMessageContent
from linebot.exceptions import InvalidSignatureError

from router import route_message

load_dotenv()
ENABLE_LOGGING = os.getenv("ENABLE_LOGGING", "false").lower() == "true"

app = Flask(__name__)

LINE_CHANNEL_ACCESS_TOKEN = os.environ.get("LINE_CHANNEL_ACCESS_TOKEN")
LINE_CHANNEL_SECRET = os.environ.get("LINE_CHANNEL_SECRET")

config = Configuration(access_token=LINE_CHANNEL_ACCESS_TOKEN)
api_client = ApiClient(config)
line_bot_api = MessagingApi(api_client)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

@handler.add(MessageEvent)
def handle_message(event):
    if not isinstance(event.message, TextMessageContent):
        return

    user_message = event.message.text.strip()
    user_id = event.source.user_id

    reply_text = route_message(user_id, user_message)
    if reply_text:
        from linebot.v3.messaging import TextMessage, ReplyMessageRequest

        # TextMessage型のオブジェクトかどうかを確認
        if isinstance(reply_text, TextMessage):
            message_obj = reply_text
        else:
            message_obj = TextMessage(text=reply_text)

        line_bot_api.reply_message(
            ReplyMessageRequest(
                reply_token=event.reply_token,
                messages=[message_obj]
            )
        )
@handler.add(MessageEvent, message=StickerMessageContent)
def handle_sticker(event):
    reply = "クロネ：は？なんやそのスタンプ。ダサ。"
    from linebot.v3.messaging import TextMessage, ReplyMessageRequest
    line_bot_api.reply_message(
        ReplyMessageRequest(
            reply_token=event.reply_token,
            messages=[TextMessage(text=reply)]
        )
    )


@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers.get("X-Line-Signature", "")
    body = request.get_data(as_text=True)
    print("=== Webhook受信 ===")
    print("Signature:", signature)
    print("Body:", body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("❌ InvalidSignatureError: 署名が一致しませんでした。")
        abort(400)
    except Exception as e:
        print("❌ その他の例外発生:", str(e))
        abort(500)
    return "OK"

@app.route("/")
def home():
    return "クロネBotはRender上で動作中やで！"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
