from summarizer import textranker
import telepot
from telepot.loop import MessageLoop
import time
import os
from chatdb import DBHelper 
import MySQLdb

bot = telepot.Bot(INSERT TOKEN HERE)
path = os.getcwd()
  
  
def startSummarise(chat_id):
	if not os.path.exists(chat_id + ".txt"):
		newfile=open(chat_id + ".txt","w+")
	if not os.path.exists(path +"/messages/"+ chat_id + ".txt"):
		newfile=open(path+ chat_id + ".txt")
		newfile.close()
	else :
		doc=open(chat_id + ".txt","r")
		doc=open(path +"/messages/"+ chat_id + ".txt","r")
		document=doc.read()
		doc.close()
		print (document)
		summaryString=textranker(document)
		if summaryString == "[]": #output will be [] if there is not enough data
def handle(msg):
	if content_type == "text":
		chat_id = str(chat_id)
		messageString = msg["text"]
		print(path)
		if messageString == "/summarise":
			startSummarise(chat_id)
		elif messageString == "/clear":
			os.remove(chat_id + ".txt")
			os.remove(path +"/messages/" + chat_id + ".txt")
		elif messageString[0] != "/": #ignore messages starting with / 
			print("received " + messageString + " from " + chat_id )
			store=open(chat_id + ".txt","a+") 
			store=open(path  +"/messages/"+ chat_id + ".txt","a+") 
			store.write(msg["text"] + " ")
			store.close()
MessageLoop(bot,{"chat":handle}).run_as_thread()
