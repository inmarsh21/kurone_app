from linebot.v3.messaging import TextMessage
import random
from responses.ending import ending_response

def color_response():
    colors = [
        "黒", "青", "白", "赤", "紫", "灰色", "黄土色", "水色", "緑", "オレンジ",
        "金", "銀", "くすみピンク", "深緑", "ワインレッド", "ミントグリーン",
        "ネイビー", "ラベンダー", "アイボリー", "ベージュ"
    ]
    items = [
        "傘", "ヘッドホン", "古本", "スマホケース", "鍵", "マグカップ", "メモ帳",
        "ボールペン", "ぬいぐるみ", "時計", "指輪", "サングラス",
        "ポーチ", "栞", "キャンドル", "コースター", "スニーカー", "手鏡"
    ]
    thoughts = [
        "開き直る", "とことん考えない", "テンション高めに振る舞う",
        "全部人のせいにする", "やたらポジティブになる", "ひたすら無心で耐える",
        "空気になる", "逆ギレしてみる", "突然笑顔で乗り切る", "ひとまず寝る"
    ]
    people = [
        "無口な人", "年上", "動物好き", "テンション低めの人",
        "全然タイプじゃない人", "めっちゃうるさい人", "気遣いできない人",
        "小学生以下", "やたらテンション高いやつ"
    ]
    spots = [
        "バス停", "公園のベンチ", "本屋", "コンビニの前", "誰もいないカフェ",
        "商店街", "駅のホーム", "使われてない会議室", "廃墟みたいな階段",
        "昼なのに暗い通路"
    ]
    times = ["朝7時", "10時半", "14時ごろ", "夕方5時", "夜中3時", "23時ぴったり", "13時13分", "4時44分"]

    color = random.choice(colors)
    item = random.choice(items)
    thought = random.choice(thoughts)
    person = random.choice(people)
    spot = random.choice(spots)
    time = random.choice(times)

    intro_templates = [
        "ラッキーカラーは『{color}』。べつに似合うとは言ってない。",
        "今日の色は『{color}』らしいけど…期待すんな。",
        "運気がマシになる色？『{color}』だとよ。どうでもいいけどな。",
        "『{color}』って言われたけど、センスの問題で似合わなかったらごめんな。",
        "まさかの『{color}』。あー…うん、頑張れ。"
    ]
    item_templates = [
        "ラッキーアイテムは『{item}』。たぶん、お前が持ってても意味ねーけど。",
        "『{item}』を手にするとか…笑うわ。似合わなすぎて。",
        "運が逃げる前に『{item}』でも握っとけ。無駄かもだけど。",
        "『{item}』？マジか。…まあ、ないよりマシか。",
        "道端に落ちてても拾わねーけど、お前には必要かもな。『{item}』。"
    ]
    advice_templates = [
        "今日は『{thought}』で乗り切るのがマシらしい。信じるかは勝手にしろ。",
        "『{thought}』でいけってさ。無理なら無理でいいよもう。",
        "…まあ、『{thought}』ってことで。適当に流しとけ。",
        "どうせロクな判断できないんだから『{thought}』くらいでちょうどいい。",
        "いつもよりマシな失敗にしたいなら『{thought}』が合言葉らしいぞ。"
    ]
    person_templates = [
        "『{person}』がキーパーソンとか言われてるけど…ほんとかな。",
        "お前が絡むと逆に嫌われそうだけど、一応『{person}』がラッキー相手。",
        "運気のヒントは『{person}』にあるらしいよ。信用できるかは知らんけどな。",
        "『{person}』に絡まれても無視するなよ。今日だけは。",
        "普段なら絶対避けるタイプ、『{person}』。でも今日は違うらしいぞ。"
    ]
    place_templates = [
        "『{time}』に『{spot}』行くと何か起きるかもな。知らんけど。",
        "『{spot}』で『{time}』にボーッとしてたら、マシな日になるかもな。",
        "なんか知らんけど、『{spot}』×『{time}』が今日の運命っぽいぞ。",
        "どうせ暇だろ？『{time}』に『{spot}』でも行っとけ。",
        "行く意味あるかは不明。でも『{time}』に『{spot}』って出てるんだよな…怖っ。"
    ]

    text_parts = [
        random.choice(intro_templates).format(color=color),
        random.choice(item_templates).format(item=item),
        random.choice(advice_templates).format(thought=thought),
        random.choice(person_templates).format(person=person),
        random.choice(place_templates).format(spot=spot, time=time)
    ]

    endings = ending_response()
    return [TextMessage(text="\n".join(text_parts))] + endings
