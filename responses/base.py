from linebot.v3.messaging import TextMessage, QuickReply, QuickReplyItem, MessageAction
import random
from utils.keywords import greeting_variants


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


def reply_worry_response(user_message):
    return (
        "はぁ…お前、いきなり重てぇんだよ。\n"
        "全部どうでもよくなってんだろ？顔に書いてあるぞ。\n"
        "しょうがねぇから少しだけ相手してやる。感謝しろ。"
    )


def reply_misc(user_message):
    return random.choice(greeting_variants)