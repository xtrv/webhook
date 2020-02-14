import telepot
import re
import urllib3
from telepot.loop import OrderedWebhook

bot = telepot.Bot('1034101496:AAE6imsI-sOEea4LPjVV4_nJoq3-0UB5xmI')

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        pattern=re.search(r'^\*(.*)', msg['text'])
        if pattern:
            bot.sendMessage(-1001149714028, pattern.group(1))

webhook = OrderedWebhook(bot, handle)

webhook.run_as_thread()
