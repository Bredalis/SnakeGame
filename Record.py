
import sqlite3 as sqlite
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Record del juego guardado en bbdd local

class RecordLocal:
	def __init__(self):
		self.bbdd = sqlite.connect("SnakeGame.db")
		self.cursor = self.bbdd.cursor()
		self.datos = []

	def guardar_record(self, record):

		if record > self.datos[0][-1]:
			self.cursor.execute(f"INSERT INTO SnakeGame(Records) VALUES({record});")

			return record

	def mostrar_record(self):
		self.cursor.execute(f"SELECT MAX(Records) FROM SnakeGame;")
		self.datos = self.cursor.fetchall()

		return self.datos[0][0]

	def guardar_cambios(self):
		self.bbdd.commit()

	def cerrar_bbdd(self):
		self.bbdd.close()

# Record del juego guardado en bbdd remota

class RecordRemoto:
	def __init__(self):
		self.url = "mongodb+srv://bredalisgautreaux:ItF6fAeKDLNFpBAD@cluster0.3myzkvu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
		self.cliente = MongoClient(self.url, server_api = ServerApi("1"))
		self.db = self.cliente["SnakeGame"]
		self.coleccion = self.db["Records"]

	def ingresar_datos(self, record):

		try:

			if record != None:
				self.documento = {"Record_Maximo": record}
				self.coleccion.insert_one(self.documento)

			print("¡La coneccion fue un exito!")

		except Exception as e:
		    print("Error:", e)