from summarizer import textranker
import telepot
from telepot.loop import MessageLoop
import time
import os


bot = telepot.Bot("423773801:AAEMhmJhn8jdZt9GtJ7xkX-49wJJ9rqeNJo")
path = os.getcwd()


def startSummarise(chat_id):
	if not os.path.exists(path +"/messages/"+ chat_id + ".txt"):
		newfile=open(path+ chat_id + ".txt")
		newfile.close()
	else :
		doc=open(path +"/messages/"+ chat_id + ".txt","r")
		document=doc.read()
		doc.close()
		print (document)
		summaryString=textranker(document)
		if summaryString == "[]": #output will be [] if there is not enough data
			bot.sendMessage(chat_id,"Not enough messages for me to summarise la dei, so few messages also lazy to read ah?")
		else:
			bot.sendMessage(chat_id,summaryString)

def handle(msg):
	content_type , chat_type ,chat_id = telepot.glance(msg)
	if content_type == "text":
		chat_id = str(chat_id)
		messageString = msg["text"]
		print(path)
		if messageString == "/summarise":
			startSummarise(chat_id)
		elif messageString == "/clear":
			os.remove(path +"/messages/" + chat_id + ".txt")
		elif messageString[0] != "/": #ignore messages starting with / 
			print("received " + messageString + " from " + chat_id )
			store=open(path  +"/messages/"+ chat_id + ".txt","a+") 
			store.write(msg["text"] + " ")
			store.close()
MessageLoop(bot,{"chat":handle}).run_as_thread()
print ("I'm awake and currently collecting your chats")
while 1:
	time.sleep(10)
