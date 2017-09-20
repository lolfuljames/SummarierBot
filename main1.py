from summarizer import textranker
import telepot
from telepot.loop import MessageLoop
import time
import os


bot = telepot.Bot("423773801:AAEMhmJhn8jdZt9GtJ7xkX-49wJJ9rqeNJo")


def startSummarise(chat_id):
	if not os.path.exists(chat_id + ".txt"):
		newfile=open(chat_id + ".txt","w+")
		newfile.close()
	else :
		doc=open(chat_id + ".txt","r")
		document=doc.read()
		print (document)
		summaryString=textranker(document)
		if summaryString == "[]": #output will be [] if there is not enough data
			bot.sendMessage(chat_id,"Not enough messages for me to summarise la dei, so few messages also lazy to read ah?")
		else:
			bot.sendMessage(chat_id,summaryString)

def handle(msg):
	content_type , chat_type ,chat_id = telepot.glance(msg)
	if content_type == "text":
		messageString = msg["text"]
		if messageString == "/summarise":
			startSummarise(chat_id)
		elif messageString == "/clear":
			os.remove(chat_id + ".txt")
		elif messageString[0] != "/": #ignore messages starting with /
			chat_id = str(chat_id) 
			print("received " + messageString + " from " + chat_id )
			store=open(chat_id + ".txt","a+") 
			store.write(msg["text"] + " ")
			store.close()
MessageLoop(bot,{"chat":handle}).run_as_thread()
print ("I'm awake and currently collecting your chats")
while 1:
	time.sleep(10)
