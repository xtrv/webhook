import telepot
import re
import urllib3
from telepot.loop import OrderedWebhook

# You can leave this bit out if you're using a paid PythonAnywhere account
proxy_url = "http://proxy.server:3128"
telepot.api._pools = {
    'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=False, timeout=30),
}
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))
# end of the stuff that's only needed for free accounts

bot = telepot.Bot('1034101496:AAE6imsI-sOEea4LPjVV4_nJoq3-0UB5xmI')

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        pattern=re.search(r'^\*(.*)', msg['text'])
        if pattern:
            bot.sendMessage(-1001149714028, pattern.group(1))
#        if msg['text'] == '/start':
#            bot.sendMessage(chat_id, 'سلام چطوری؟')
#        elif msg['text'] == 'بیشور':
#            bot.sendMessage(chat_id, 'خودتی')
#        else:
#            bot.sendMessage(chat_id, msg['text'])

webhook = OrderedWebhook(bot, handle)

webhook.run_as_thread()
