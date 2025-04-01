from linebot.v3.messaging import TextMessage, QuickReply, QuickReplyItem, MessageAction
import random
from utils.keywords import greeting_variants
from responses.match import match_response
from responses.color import color_response
from responses.tarot import tarot_response

# 占いメニューの呼びかけ

def reply_fortune_intro(user_message):
    return TextMessage(
        text=(
            "占いか。ったく、いちいち面倒くせぇな。\n"
            "でもどうせお前、気になってんだろ？\n"
            "ほら、何占うんだよ。"
        ),
        quick_reply=QuickReply(
            items=[
                QuickReplyItem(action=MessageAction(label="相性診断", text="相性診断")),
                QuickReplyItem(action=MessageAction(label="タロット", text="タロット")),
                QuickReplyItem(action=MessageAction(label="ラッキーカラー", text="ラッキーカラー")),
            ]
        )
    )

# 相性診断ラッパー
def reply_match_intro(name1, name2):
    return match_response(name1, name2)

# ラッキーカラーラッパー
def reply_color():
    return color_response()

# タロットラッパー
def reply_tarot():
    return tarot_response()

# ネガティブ系相談に対する応答
def reply_worry_response(user_message):
    return (
        "はぁ…お前、いきなり重てぇんだよ。\n"
        "全部どうでもよくなってんだろ？顔に書いてあるぞ。\n"
        "しょうがねぇから少しだけ相手してやる。感謝しろ。"
    )

# あいさつ・雑談系応答
def reply_misc(user_message):
    return random.choice(greeting_variants)