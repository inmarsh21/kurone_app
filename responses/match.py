import re

from responses.match_lines import build_match_result
from responses.match_lines import (
    get_name1_line,
    get_birth1_line,
    get_name2_line,
    get_birth2_line
)
session_state = {}

def calc_numerology_number(birthday_str):
    total = sum(int(d) for d in birthday_str if d.isdigit())
    while total > 9:
        total = sum(int(d) for d in str(total))
    return total

def calculate_compatibility_score(num1, num2):
    distance = abs(num1 - num2)
    score = max(100 - distance * 12, 0)
    return score

def run_match_fortune(user_id, message):
    state = session_state.get(user_id, {})

    if not state:
        session_state[user_id] = {"step": 1}
        return get_name1_line()

    step = state["step"]

    if step == 1:
        session_state[user_id]["name1"] = message
        session_state[user_id]["step"] = 2
        return get_birth1_line()

    elif step == 2:
        if not re.fullmatch(r"\d{8}", message):
            return "8桁の数字で書けって。19930402みたいにな。"
        session_state[user_id]["birth1"] = message
        session_state[user_id]["step"] = 3
        return get_name2_line()

    elif step == 3:
        session_state[user_id]["name2"] = message
        session_state[user_id]["step"] = 4
        return get_birth2_line()

    elif step == 4:
        if not re.fullmatch(r"\d{8}", message):
            return "相手の誕生日もちゃんと8桁で書けや。19950911みたいに。"
        session_state[user_id]["birth2"] = message

        n1 = calc_numerology_number(session_state[user_id]["birth1"])
        n2 = calc_numerology_number(session_state[user_id]["birth2"])
        score = calculate_compatibility_score(n1, n2)
        comment = build_match_result(score)

        name1 = session_state[user_id]["name1"]
        name2 = session_state[user_id]["name2"]
        del session_state[user_id]

        return f"クロネ：『{name1}と{name2}』の相性は…{score}点。\n{comment}"

    return "なんやそれ、意味わからん。"