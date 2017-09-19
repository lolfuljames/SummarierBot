from summarizer import textranker
import telepot
from telepot.loop import MessageLoop
import time
import math


bot = telepot.Bot("402335623:AAG8tMmlN0Kc75VFeNEsPpfrfhAtvRvK4ow")


def startSummarise(chat_id):
	doc=open("messages.txt","r")
	document=doc.read()
	summaryString=textranker(document)
	if summaryString == "[]": #output will be [] if there is not enough data
		bot.sendMessage(chat_id,"Not enough messages for me to summarise la dei, so few messages also lazy to read ah?")
	else:
		bot.sendMessage(chat_id,summaryString)

def handle(msg):
	content_type , chat_type ,chat_id = telepot.glance(msg)
	if content_type == "text":
		messageString = msg["text"]
		if messageString == "/summarise@Testingphase1bot":
			startSummarise(chat_id)
		elif messageString == "/clear@Testingphase1bot":
			store=open("messages.txt","w") #rewrites whole file
			store.write(" ")
			store.close()
		elif messageString[0] != "/": #ignore messages starting with /
			chat_id = str(chat_id) 
			print("received " + messageString + " from " + chat_id )
			store=open("messages.txt","a") 
			store.write(msg["text"] + " ")
			store.close()
MessageLoop(bot,{"chat":handle}).run_as_thread()
print ("I'm awake and currently collecting your chats")
while 1:
	time.sleep(10)
