from linebot.v3.messaging import TextMessage
import random
from responses.ending import ending_response
from kurone_lines import kurone_lines

poison_comments = [
    "占い頼みもほどほどにせぇよ。",
    "どうせ聞いたところで何も変えへんやろ？",
    "ま、結局は自分次第ってことや。",
    "運に頼りすぎやでホンマ。"
]

def draw_card():
    card_name = random.choice(list(kurone_lines.keys()))
    position = random.choice(["正位置", "逆位置"])
    time_period = random.choice(["過去", "現在", "未来"])
    meaning = random.choice(kurone_lines[card_name][position][time_period])
    return card_name, position, time_period, meaning

def tarot_response():
    past_card, past_pos, past_time, past_meaning = draw_card()
    present_card, present_pos, present_time, present_meaning = draw_card()
    future_card, future_pos, future_time, future_meaning = draw_card()

    poison = random.choice(poison_comments)

    text = (
        f"【過去】『{past_card}』{past_pos}（{past_time}）\n{past_meaning}\n\n"
        f"【現在】『{present_card}』{present_pos}（{present_time}）\n{present_meaning}\n\n"
        f"【未来】『{future_card}』{future_pos}（{future_time}）\n{future_meaning}\n\n"
        f"【クロネの一言】\n{poison}"
    )

    return [TextMessage(text=text)] + ending_response()
