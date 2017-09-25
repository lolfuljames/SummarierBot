import MySQLdb
import os

class DBHelper:
	def __init__(self, dbname = "ChatDB"):
		self.conn = MySQLdb.connect("localhost",USERNAME,PASSWORD, "ChatDB")
		self.cursor = self.conn.cursor()
		self.conn.set_character_set('utf8')
		self.cursor.execute('SET NAMES utf8;')
		self.cursor.execute('SET CHARACTER SET utf8;')
		self.cursor.execute('SET character_set_connection=utf8;')

	def add_Message(self, chat_id, messages):
		try:
			add = "INSERT INTO content(chat_id, messages) VALUES (%s,%s)"
			self.cursor.execute(add,(chat_id,messages))
			self.conn.commit()
		except MySQLdb.Error as er:
			print(er)

	def remove_Message(self, chat_id, messages):
		try:
			delete = """DELETE FROM content WHERE chat_id = %s""" %chat_id
			self.cursor.execute(delete)
			self.conn.commit()
		except MySQLdb.Error as er:
			print(er)

	def get_Message(self, chat_id, messages):
		try:
			update = "SELECT messages FROM content WHERE chat_id = %s"%chat_id
			self.cursor.execute(update)
			textTuple = self.cursor.fetchall()
			return textTuple
		except MySQLdb.Error as er:
			print(er)

