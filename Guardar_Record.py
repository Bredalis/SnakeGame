
import sqlite3 as sqlite

class GuardarRecord:
	def __init__(self):
		self.bbdd = sqlite.connect("SnakeGame.db")
		self.cursor = self.bbdd.cursor()
		self.datos = []

	def guardar_record(self, record):

		if record > self.datos[0][-1]:
			self.cursor.execute(f"INSERT INTO SnakeGame(Records) VALUES({record});")

	def mostrar_record(self):
		self.cursor.execute(f"SELECT MAX(Records) FROM SnakeGame;")
		self.datos = self.cursor.fetchall()

		return self.datos[0][0]

	def guardar_cambios(self):
		self.bbdd.commit()

	def cerrar_bbdd(self):
		self.bbdd.close()