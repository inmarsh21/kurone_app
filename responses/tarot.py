from linebot.v3.messaging import TextMessage
import random
from responses.ending import ending_response


def tarot_response():
    cards = [
        "愚者（The Fool）", "魔術師（The Magician）", "女教皇（The High Priestess）", "女帝（The Empress）",
        "皇帝（The Emperor）", "教皇（The Hierophant）", "恋人（The Lovers）", "戦車（The Chariot）",
        "力（Strength）", "隠者（The Hermit）", "運命の輪（Wheel of Fortune）", "正義（Justice）",
        "吊るされた男（The Hanged Man）", "死神（Death）", "節制（Temperance）", "悪魔（The Devil）",
        "塔（The Tower）", "星（The Star）", "月（The Moon）", "太陽（The Sun）",
        "審判（Judgement）", "世界（The World）"
    ]

    situations = [
        "過去の行動がじわじわ効いてるかもな。今さら戻れないけど。",
        "何か変えたいなら、今すぐやらなきゃ手遅れになるかもな。",
        "まあ悪くない。って言えるレベルには、たぶん届いてないけどな。",
        "現実逃避してんじゃねぇよ。そろそろ向き合えって。",
        "タイミングは悪くない。でもお前の動きがトロいんだよ。",
        "自分で選んだ道だろ？後悔すんなよ、見ててダサいから。",
        "もしかしてラッキーと思ってる？気のせいかもな。",
        "いい夢見すぎ。そろそろ起きろ。",
        "悪くない引き。でもお前の行動が全てぶち壊す可能性あるけどな。"
    ]

    advice = [
        "深く考えるな。どうせ当たらないし。",
        "お前にしてはマシな流れ来てる。逃すなよ。",
        "今日ぐらい、ちゃんとやれ。いやマジで。",
        "油断すると全部ひっくり返るからな。ニヤけてんじゃねぇよ。",
        "今のうちに動け。動かなきゃ何も起きねぇ。",
        "何か言い訳しようとしてんな？それ、誰も聞いてねぇぞ。"
    ]

    selected_card = random.choice(cards)
    selected_situation = random.choice(situations)
    selected_advice = random.choice(advice)

    text = f"引いたカードは『{selected_card}』。\n{selected_situation}\n{selected_advice}"

    return [TextMessage(text=text)] + ending_response()
