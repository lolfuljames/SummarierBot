from summarizer import textranker
import telepot
from telepot.loop import MessageLoop
import time


bot = telepot.Bot("402335623:AAG8tMmlN0Kc75VFeNEsPpfrfhAtvRvK4ow")


def startSummarise():
	doc=open("messages.txt","r",encoding='utf-8')
	document=doc.read()
	textranker(document)
def handle(msg):
	content_type , chat_type ,chat_id = telepot.glance(msg)
	if content_type == "text":
		chat_id = str(chat_id) 
		print("received " + msg['text'] + " from " + chat_id )
		store=open("messages.txt","a")
		store.write(msg["text"] + ". ")
		store.close()
MessageLoop(bot,handle).run_as_thread()
print ("I'm awake and currently collecting your chats")
while 1:
	time.sleep(10)
