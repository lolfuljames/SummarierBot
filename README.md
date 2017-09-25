# telegram-bot-test
First code for telegram bots using telepot

This bot is to be added to a telegram group chat and summarise the previous chat messages when required.

NOTE : Remember to set /privacy mode to off by talking to @BotFather

Every messages sent will be saved to a local MySQL server (column 1 : chat_id, column 2 : messages)

When the summarise command is called, it will summarise the saved messages.


There is a local storage version for this bot for non-MySQL users in the txtFileVersionSummariser file. /messages.txt will be the storage area for the messages.
