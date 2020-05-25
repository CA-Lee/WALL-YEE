from flask import Flask, request
import telebot

import os

TOKEN = os.environ.get('TOKEN')
WEBHOOK = os.environ.get('WEBHOOK')
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

def send_markdown_message(message,content):
    bot.send_message(
        chat_id=message.chat.id,
        parse_mode="Markdown",
        disable_web_page_preview=True,
        text=content
    )

@bot.message_handler(commands=['start'])
def start(message):
    send_markdown_message(
        message,
        '你好，世界！\n我現在什麼都不會！\n\n我的原始碼: [GitHub](https://github.com/CA-Lee/WALL-YEE)'
        )

#####
case_list = ['test']

@bot.message_handler(commands=['status_listall'])
def status_listall(message):
    reply_text = [(str(case) + '\n') for case in case_list]
    send_markdown_message(message,reply_text)

#####

@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK)
    return "!", 200

if __name__ == "__main__":
    app.run()