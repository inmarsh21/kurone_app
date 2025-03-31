import random

# 各ステップでの聞き返しセリフ（ランダム）

name1_lines = [
    "まずお前の名前は？",
    "で、あんた、なんて名前やったっけ？",
    "教えて。お前の名前な。",
    "名前からいこうか。ちゃんと人間のな？",
    "ふーん…じゃ、名前は？いちおう聞いとくわ。",
]

birth1_lines = [
    "で、誕生日は？西暦で書けや。例：19930402",
    "お前の誕生日な。西暦8桁で頼むで。",
    "次、誕生日な。嘘ついても占いには出るけどな？",
    "生年月日や。年も月も日もちゃんとやぞ。",
    "へいへい、いつ生まれたん？数字で書けや。",
]

name2_lines = [
    "相手の名前は？まさか犬とか猫とか言うなよ？",
    "ほんで、相手の名前も教えとけ。",
    "気になる相手の名前、書いてみ？笑わへんから。",
    "誰と見てほしいん？名前な、名前。",
    "相手の呼び名、なんでもええから教えてくれ。",
]

birth2_lines = [
    "で、その人の誕生日も教えろ。わからんならテキトーでええわ。",
    "相手の誕生日な。ちゃんと数字8桁で頼むわ。",
    "そいつの誕生日、分かるか？分からんでもいいけど書いてみ。",
    "相手いつ生まれたかって？そんなん自分で聞けや…ま、書いて。",
    "ほれ、相手の生年月日や。数字やで？",
]

def get_name1_line():
    return random.choice(name1_lines)

def get_birth1_line():
    return random.choice(birth1_lines)

def get_name2_line():
    return random.choice(name2_lines)

def get_birth2_line():
    return random.choice(birth2_lines)


# 1行目：導入用の毒セリフ（共通）
intro_lines = [
    "マジで？お似合いやと思ってんの？正気か？",
    "ふーん、そういう組み合わせか…やばそう。",
    "オレにはどうでもええけど、あんま期待すんなよ？",
    "その相手でええんか？ほんまに？",
    "へぇ〜そうくる？まあ…止めはせんけどな。",
    "占いでどうにかなると思ってる時点で、もう終わっとる。",
    "恋ってアホになるやん？お前、今まさにそれやで。",
    "まさかとは思うけど…本気なん？",
    "その組み合わせ、地雷の匂いしかしないんやけど。",
    "お前のセンス、だいぶ終わってるかもな。",
    "相手が好きなんは分かるけど…お前のこと好きか？",
    "あー、見た瞬間から“やばい”感じしてたわ。",
    "はいはい、恋は盲目ってやつな。",
    "どうせまた自爆する未来しか見えへんで？",
]

# スコア帯に応じたまとめコメント（3パターンずつ）
score_comments = {
    "96-100": [
        "神レベルやな。うまくいかん方が奇跡やわ。",
        "完璧すぎて逆に怖いな。映画かなんか？",
        "…信じられへん。お前らが？運命の相手？ムカつくわ。"
    ],
    "91-95": [
        "ここまで相性ええって、もう怖いレベルやな。夢オチちゃうん？",
        "理想のパターンやけどな、現実はキビしいで。",
        "マジかよ。運命すぎて逆に別れるんちゃうか？"
    ],
    "86-90": [
        "ええやん、安定感ある組み合わせやな。",
        "なんや、相性ええとか…腹立つな。",
        "これはなかなかの鉄板ペアやな。珍しいで。"
    ],
    "81-85": [
        "恋愛漫画の設定かよ。ちょっとイラつくな。",
        "ほぉ…こういう組み合わせ、案外うまくいくねん。",
        "ええバランスやと思うで。まあ、うまくやれよ。"
    ],
    "76-80": [
        "なかなか良いな。応援したるわ…ちょっとだけな。",
        "ええやん、現実味もあるし悪くない。",
        "いい感じやけど、油断すんなよ。"
    ],
    "71-75": [
        "まあまあやな。無難すぎて逆に話広がらんわ。",
        "いけそうやけど、一瞬で壊れるかもな。",
        "平均よりちょいマシ。自信あるなら突っ込んでみ？"
    ],
    "66-70": [
        "普通よりちょい上。つまらんけど安定型や。",
        "ええ意味でも悪い意味でも普通やな。",
        "クセはないけど、ドキドキは無いやろな。"
    ],
    "61-65": [
        "ちょっとズレてるけど、努力でなんとかなりそうやな。",
        "まあ…微妙寄りの普通ってやつやな。",
        "決め手に欠けるわ。悪くはないけどな。"
    ],
    "56-60": [
        "ズレはあるけど、そこが逆にハマるかもな。",
        "タイミング次第やな。運に任せとけ。",
        "お互いに疲れそうな気もするけどな。"
    ],
    "51-55": [
        "正直、無理に付き合う理由ないレベルやな。",
        "会話は成立するけど、心は通ってなさそうや。",
        "この距離感、もはや他人やで。"
    ],
    "46-50": [
        "ちょっとしんどいな。すれ違い多そうやし。",
        "いけるかどうかは…お互いの忍耐力やな。",
        "喧嘩多めやと思うけど、止めはせん。"
    ],
    "41-45": [
        "だいぶぶつかると思うわ。疲れるやつやな。",
        "情熱はあるけど、噛み合わんパターンや。",
        "恋より修行って感じやな。"
    ],
    "36-40": [
        "危険やな。相性より先に心壊れるで。",
        "地雷原にダイブする覚悟あるなら、止めへん。",
        "火花は散るけど、すぐ燃え尽きるで。"
    ],
    "26-35": [
        "地獄の門が開いとるで。お前ら前世で何したん？",
        "やめとけって言っても聞かんやつやろ？知ってる。",
        "ネタにできるレベルで最悪やけど、それでも行くんか？"
    ],
    "16-25": [
        "…まあ、お前もツラい人生やもんな。分かるで。",
        "どーせうまくいかんって分かってんのに、期待してまうよな。",
        "あー…似てるわ、オレとお前。そういうやつ、好きになんねんな…"
    ],
    "0-15": [
        "ごめん、これはもう占いとかやないわ。お前がしんどいだけや。",
        "ここまでくると、もう何も言えん。生きてるだけでえらい。",
        "…お前の闇、深いで。でもオレは嫌いちゃうで。"
    ]
}

def get_score_band(score):
    for band in score_comments:
        min_val, max_val = map(int, band.split("-"))
        if min_val <= score <= max_val:
            return band
    return "0-15"

def build_match_result(score):
    intro = random.choice(intro_lines)
    band = get_score_band(score)
    summary = random.choice(score_comments[band])
    return f"{intro}\n{summary}"
