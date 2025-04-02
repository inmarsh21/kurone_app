from linebot.v3.messaging import TextMessage
from responses.ending import ending_response
import random
import unicodedata

session_state = {}

def calculate_score(name1, name2):
    def name_value(name):
        return sum(ord(char) for char in name if unicodedata.category(char).startswith('L'))
    total = name_value(name1) + name_value(name2)
    score = (total % 91) + 10
    return score

def match_response(name1, name2):
    if not name1 or not name2:
        return [TextMessage(text="名前が足りないみたいだな。ちゃんと2人分入力しろよ。")]

    if len(name1) > 10 or len(name2) > 10:
        return [TextMessage(text="名前、長すぎない？もうちょい普通の名前で頼むわ。")]

    score = calculate_score(name1, name2)

    def random_comment(options):
        return random.choice(options)

    if score <= 10:
        comments = [
            "これはもう…呪われてるレベル。関わらない方がいいって。",
            "最悪すぎる。逆にどうやったらここまで相性悪くなるんだよ。",
            "正直、会話すら成立しないんじゃね？別々の世界で生きてる感じ。"
        ]
    elif score <= 19:
        comments = [
            "マジで最悪。顔合わせるたびにストレスたまるタイプ。",
            "この組み合わせ、誰が得すんの？意味不明すぎる。",
            "合わないってレベルじゃないな。地雷原を歩くようなもんだよ。"
        ]
    elif score <= 34:
        comments = [
            "厳しいな。会話のたびに温度差ありすぎて疲れそう。",
            "努力すればワンチャンある…かも。でもほぼ無理。",
            "正直、一緒にいると空気悪くなるタイプの相性だな。"
        ]
    elif score <= 49:
        comments = [
            "微妙。悪くはないけど、正直つまらない組み合わせ。",
            "空気みたいな関係ってこのことかもな。存在感ゼロ。",
            "会っても印象に残らなそう。可もなく不可もなくってやつ。"
        ]
    elif score <= 64:
        comments = [
            "まあまあ。悪くないけど、刺激も足りない感じ。",
            "安心はするけど、飽きるのも早そうなペア。",
            "一緒にいても問題はないけど、盛り上がりには欠けるな。"
        ]
    elif score <= 79:
        comments = [
            "そこそこいい感じじゃん。正直ちょっと悔しい。",
            "悪くない。意外と相性いいのかもな。",
            "これくらいなら文句なし。平和にやっていけそう。"
        ]
    elif score <= 89:
        comments = [
            "けっこう良いね。素直に認めるわ、羨ましい。",
            "仲良すぎて見てるこっちがイラっとするレベル。",
            "相性良すぎて毒吐くタイミングないわ。つまらん。"
        ]
    else:
        comments = [
            "最高レベル。運命とか信じたくなるくらいの相性。",
            "ここまで来ると嫉妬すら通り越して呆れるな。",
            "もう付き合ってんだろ？って言いたくなるくらいぴったりだわ。"
        ]

    messages = [
        TextMessage(text=f"スコア：{score}点"),
        TextMessage(text=random_comment(comments)),
        *ending_response()
    ]

    return messages
