import telegram
from flask import Flask, request
from telegram.ext import Dispatcher, MessageHandler, Filters, CommandHandler

import os
import psycopg2
from base64 import *

TOKEN = os.environ['TOKEN']

app = Flask(__name__)

bot = telegram.Bot(token=TOKEN)

def start(update, context):
    update.message.reply_text(
        "你好，世界！\n我現在什麼都不會！\n\n我的原始碼: [GitHub](https://github.com/CA-Lee/WALL-YEE)",
        parse_mode="Markdown",
        disable_web_page_preview=True,
        quote=False
    )


def status_listall(update, context ):
    with psycopg2.connect(os.environ['DATABASE_URL'], sslmode='require') as conn:
        with conn.cursor() as cur:
            cur.execute('SELECT * FROM case_status;')
            # id, status, case_name, case_url
            status_emoji = ['👀', '💼', '💬', '📝']
            text = ""
            for rec in cur.fetchall():
                text += status_emoji[rec[1]] + ' '
                text += '[{}]({})'.format(b64decode(rec[2]).decode(), b64decode(rec[3]).decode())
                text += '\n'
            update.message.reply_text(
                text,
                parse_mode="Markdown",
                disable_web_page_preview=True,
                quote=False
            )

def status_addcase(update, context):
#    with psycopg2.connect(os.environ['DATABASE_URL'], sslmode='require') as conn:
#        with conn.cursor() as cur:
#            cur.execute('insert into case_status (name, url) values (\'{}\',\'{}\');'.format(b64encode(update.args[0].encode()).decode(), b64encode(update.args[1].encode()).decode()))
    update.message.reply_text(
        '成功新增案件，辛苦了❤️\n {} {} {}'.format( type(context.args), type(bot), type(update)),
        quote=False
    )
    #status_listall(bot, update)

@app.route('/' + TOKEN, methods=['POST'])
def webhook_handler():
    """Set route /hook with POST method will trigger this method."""
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)
        dispatcher.process_update(update)
    return 'ok'


dispatcher = Dispatcher(bot, None, use_context=True)
#dispatcher.add_handler(MessageHandler(Filters.text, reply_handler))
dispatcher.add_handler(CommandHandler(['start'], start))
dispatcher.add_handler(CommandHandler(['status_listall'], status_listall))
dispatcher.add_handler(CommandHandler(['status_addcase'], status_addcase))

if __name__ == "__main__":

    app.run()
