'''
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

@bot.message_handler(commands=['status_addcase'])
def status_addcase(message):
    reply_text = [(str(arg) + '\n') for arg in message.text.split()]
    send_markdown_message(message,str(message.text))
#####
'''
import telegram
from flask import Flask, request
from telegram.ext import Dispatcher, MessageHandler, Filters, CommandHandler
import os

TOKEN = os.environ.get('TOKEN')
app = Flask(__name__)
bot = telegram.Bot(token=TOKEN)

def reply_handler(bot, update):
    """Reply message."""
    text = update.message.text
    update.message.reply_text(text)

def start(bot, update):
    update.message.reply_text(
        "你好，世界！\n我現在什麼都不會！\n\n我的原始碼: [GitHub](https://github.com/CA-Lee/WALL-YEE)",
        parse_mode="Markdown",
        disable_web_page_preview=True,
        quote=False
        )


@app.route('/' + TOKEN, methods=['POST'])
def webhook_handler():
    """Set route /hook with POST method will trigger this method."""
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)

        dispatcher.process_update(update)
    return 'ok'

dispatcher = Dispatcher(bot, None)
#dispatcher.add_handler(MessageHandler(Filters.text, reply_handler))
dispatcher.add_handler(CommandHandler(['start'], start))

if __name__ == "__main__":

    app.run()
