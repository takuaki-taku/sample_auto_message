import json

file = open("info.json", "r", encoding="utf-8")
info = json.load(file)
# info['CHANNEL_ACCESS_TOLEN']

from linebot import LineBotApi, exceptions
from linebot.models import TextSendMessage

CHANNEL_ACCESS_TOKEN = info["CHANNEL_ACCESS_TOKEN"]
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)


def main():
    USER_ID = info["USER_ID"]
    messages = TextSendMessage(text="おはよう〜\n 朝だよ、起きてね❤️")
    line_bot_api.push_message(USER_ID, messages=messages)


if __name__ == "__main__":
    main()