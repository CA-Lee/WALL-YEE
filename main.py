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
from telegram.ext import Updater, CommandHandler
import os

TOKEN = os.environ.get('TOKEN')
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text='你好，世界！\n我現在什麼都不會！\n\n我的原始碼: [GitHub](https://github.com/CA-Lee/WALL-YEE)'
        )

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_webhook(url_path=TOKEN)