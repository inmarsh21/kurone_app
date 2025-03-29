import random
from utils.keywords import greeting_variants


def reply_fortune_intro(user_message):
    return (
        "占いか。ったく、いちいち面倒くせぇな。\n"
        "でもどうせお前、気になってんだろ？\n"
        "ほら、何占うんだよ。\n"
        "【1】相性診断\n【2】タロット\n【3】ラッキーカラー\n"
        "番号でも単語でもさっさと言え。"
    )


def reply_worry_response(user_message):
    return (
        "はぁ…お前、いきなり重てぇんだよ。\n"
        "全部どうでもよくなってんだろ？顔に書いてあるぞ。\n"
        "しょうがねぇから少しだけ相手してやる。感謝しろ。"
    )


def reply_misc(user_message):
    return random.choice(greeting_variants)
