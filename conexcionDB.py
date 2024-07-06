import sqlite3
NAME='Empleados.db'

class ConexionBD:
    def __init__(self,nombreDB):
        self.conexcion=sqlite3.connect(nombreDB)
        self.cursor=self.conexcion.cursor()
    def closeDB(self):
        self.conexcion.close()
    def request(self,request):
        self.cursor.execute(request)
        #return self.cursor.fetchall()
    def commit(self):
        self.conexcion.commit()