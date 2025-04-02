from flask import Flask, request, abort
from linebot.v3 import WebhookHandler
from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3.messaging import Configuration, ApiClient, MessagingApi, TextMessage, ReplyMessageRequest
from linebot.v3.webhooks import MessageEvent, TextMessageContent
from router import route_message
import os

app = Flask(__name__)

channel_access_token = os.environ.get("CHANNEL_ACCESS_TOKEN")
channel_secret = os.environ.get("CHANNEL_SECRET")

handler = WebhookHandler(channel_secret)
configuration = Configuration(access_token=channel_access_token)

with ApiClient(configuration) as api_client:
    line_bot_api = MessagingApi(api_client)

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

@handler.add(MessageEvent)
def handle_message(event):
    if not isinstance(event.message, TextMessageContent):
        return

    user_message = event.message.text.strip()
    user_id = event.source.user_id

    reply = route_message(user_id, user_message)

    if not reply:
        return

    if not isinstance(reply, list):
        reply = [reply]

    messages = []
    for r in reply:
        if isinstance(r, TextMessage):
            messages.append(r)
        else:
            messages.append(TextMessage(text=str(r)))

    line_bot_api.reply_message(
        ReplyMessageRequest(
            reply_token=event.reply_token,
            messages=messages
        )
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
