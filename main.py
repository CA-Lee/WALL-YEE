from flask import Flask, request
import telebot

import os

TOKEN = os.environ.get('TOKEN')
WEBHOOK = os.environ.get('WEBHOOK')
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

bot.set_webhook(url=WEBHOOK)

@bot.message_handler(commands=['ping'])
def ping(message):
        bot.reply_to(message, "PONG~")

@app.route('/', methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return 200

if __name__ == "__main__":
        app.run()