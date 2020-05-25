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
from telegram.ext import Dispatcher, MessageHandler, Filters
import os

TOKEN = os.environ.get('TOKEN')

# Initial Flask app
app = Flask(__name__)

# Initial bot by Telegram access token
bot = telegram.Bot(token=TOKEN)


@app.route('/' + TOKEN, methods=['POST'])
def webhook_handler():
    """Set route /hook with POST method will trigger this method."""
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)

        # Update dispatcher process that handler to process this message
        dispatcher.process_update(update)
    return 'ok'


def reply_handler(bot, update):
    """Reply message."""
    text = update.message.text
    update.message.reply_text(text)


# New a dispatcher for bot
dispatcher = Dispatcher(bot, None)

# Add handler for handling message, there are many kinds of message. For this handler, it particular handle text
# message.
dispatcher.add_handler(MessageHandler(Filters.text, reply_handler))

if __name__ == "__main__":
    # Running server
    app.run()
