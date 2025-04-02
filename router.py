
from responses import base
from responses import match, tarot, color
from utils.keywords import fortune_keywords, worry_keywords

def route_message(user_id, user_message):
    message = user_message.lower()

    from responses import match

    # 占いメニュー番号 or 名称で分岐
    if message in ["1", "相性", "相性診断"]:
        return match.match_fortune(user_id, message)
    if user_id in match.session_state:
        return match.match_fortune(user_id, message)

    elif message in ["2", "タロット"]:
        return base.reply_tarot()

    elif message in ["3", "ラッキーカラー", "カラー", "色"]:
        base.reply_color()

    # 占いワードに該当
    elif any(keyword in message for keyword in fortune_keywords):
        return base.reply_fortune_intro(message)

    # ネガティブワードに該当
    elif any(keyword in message for keyword in worry_keywords):
        return base.reply_worry_response(message)

    # それ以外（雑な対応）
    else:
        return base.reply_misc(message)
