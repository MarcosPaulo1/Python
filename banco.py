
import sqlite3
class Banco():

    def __init__(self):
        self.conn = sqlite3.connect('materias.db')
        self.createTable()

    def createTable(self):
        cursor = self.conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS materias ( idMateria INTEGER PRIMARY KEY AUTOINCREMENT, nome_materia TEXT NOT NULL UNIQUE,dia_horario_materia TEXT NOT NULL, professor_materia TEXT NOT NULL, campus_materia TEXT NOT NULL, nota_av1 FLOAT, nota_av2 FLOAT, nota_avd FLOAT, nota_avds FLOAT);""")