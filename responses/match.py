import re

# 一時的なセッション保存用（簡易）
session_state = {}

# 数秘術で運命数を計算（誕生日の数値合計 → 1桁）
def calc_numerology_number(birthday_str):
    total = sum(int(d) for d in birthday_str if d.isdigit())
    while total > 9:
        total = sum(int(d) for d in str(total))
    return total

# 相性スコアの算出（運命数の距離をベースに逆変換）
def calculate_compatibility_score(num1, num2):
    distance = abs(num1 - num2)
    score = max(100 - distance * 12, 40)  # 最低40点保証
    return score

# 毒づきコメントをスコアに応じて出す
def get_snarky_comment(score):
    if score >= 90:
        return "相性90点以上…マジか。こんな奇跡あんの？"
    elif score >= 75:
        return "まあまあええやん。って言っとくわ。"
    elif score >= 60:
        return "うーん、微妙。運しだいやな。"
    elif score >= 50:
        return "正直おすすめせんけど、止めへん。"
    else:
        return "やめとけ。マジで。"

# 会話ステップ管理＋診断処理
def run_match_fortune(user_id, message):
    state = session_state.get(user_id, {})

    if not state:
        session_state[user_id] = {"step": 1}
        return "は？相性診断？…ま、ええわ。まずお前の名前は？"

    step = state["step"]

    if step == 1:
        session_state[user_id]["name1"] = message
        session_state[user_id]["step"] = 2
        return "で、誕生日は？西暦で書けや。例：19930402"

    elif step == 2:
        if not re.fullmatch(r"\d{8}", message):
            return "8桁の数字で書けって。19930402みたいにな。"
        session_state[user_id]["birth1"] = message
        session_state[user_id]["step"] = 3
        return "相手の名前は？まさか犬とか猫とか言うなよ？"

    elif step == 3:
        session_state[user_id]["name2"] = message
        session_state[user_id]["step"] = 4
        return "で、その人の誕生日も教えろ。わからんならテキトーでええわ。"

    elif step == 4:
        if not re.fullmatch(r"\d{8}", message):
            return "相手の誕生日もちゃんと8桁で書けや。19950911みたいに。"
        session_state[user_id]["birth2"] = message

        # 診断開始
        n1 = calc_numerology_number(session_state[user_id]["birth1"])
        n2 = calc_numerology_number(session_state[user_id]["birth2"])
        score = calculate_compatibility_score(n1, n2)
        comment = get_snarky_comment(score)

        name1 = session_state[user_id]["name1"]
        name2 = session_state[user_id]["name2"]
        del session_state[user_id]  # セッション終了

        return f"クロネ：『{name1}と{name2}』の相性は…{score}点。\n{comment}"

    return "なんやそれ、意味わからん。"