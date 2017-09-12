import sys
import time
import telepot
from telepot.loop import MessageLoop
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton

#this bot is to test out the features and usage of telepot's API

def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    global a
    a=0 #a is to ensure the inline buttons do not exceed screen limit

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
                    [dict(text='you could try this though', callback_data='he did it')],
                    [dict(text='CANT TOUCH THIS', callback_data='press'), dict(text='Exit Bot', callback_data='exit')]])

    bot.sendMessage(chat_id, "Don't you dare touch my buttons", reply_markup=keyboard)

def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, from_id, query_data)
    
    global a
    a += 1
    if a>5:
        bot.sendMessage(from_id,"Stop touching and buttons and talk to me! Or else my buttons will be hard to find!")
    if query_data == "he did it":
                    bot.sendMessage(from_id,"doooood nice")
    elif query_data == "press":
                    bot.sendMessage(from_id,"Stop it!")
                                  
    else:
        bot.sendMessage(from_id,"I am a bot anyway, you can just ignore me.")

    print (a)

bot = telepot.Bot("put your own token")
MessageLoop(bot, {'chat': on_chat_message,
                  'callback_query': on_callback_query}).run_as_thread()
print('Listening ...')
a=1

# Keep the program running. 
while 1:
    time.sleep(10)
