
from conexcionDB import ConexionBD,NAME

conexDB=ConexionBD(NAME) 
query=('''CREATE TABLE IF NOT EXISTS empleados(
dni INTEGER PRIMARY KEY ,
nombre varchar(30),
apellido varchar(30),
telefono INTEGER,
mail varchar(40))''')
conexDB.request(query)
query2=('''CREATE TABLE IF NOT EXISTS register(
id INTEGER PRIMARY KEY AUTOINCREMENT,
mail varchar(40),
contraseña varchar(30)
)''')

conexDB.request(query2)
query3=('''CREATE TABLE IF NOT EXISTS productos(
id INTEGER PRIMARY KEY AUTOINCREMENT,
producto varchar(40),
descripcion varchar(30),
precio INTEGER,
stock INTEGER
)''')
conexDB.request(query3)
conexDB.commit()
conexDB.closeDB()