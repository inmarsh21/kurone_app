import random

def run_match_fortune(user_id, message):
    results = [
        "最悪", "微妙", "普通", "まぁまぁ", "相性バッチリ"
    ]

    replies = {
        "最悪": "クロネ：診断結果？『最悪』やって。うわ〜お似合いやな。",
        "微妙": "クロネ：『微妙』やって。まあ、お前にはちょうどええやろ。",
        "普通": "クロネ：『普通』。それが一番つまらんねんけどな。",
        "まぁまぁ": "クロネ：『まぁまぁ』やって。…なんかリアクションに困るやつ。",
        "相性バッチリ": "クロネ：『相性バッチリ』やと。調子乗んなよ？"
    }

    result = random.choice(results)
    return replies[result]