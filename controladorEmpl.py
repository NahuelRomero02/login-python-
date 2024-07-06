
from tkinter import messagebox
from empleados import Empleado,Register
from conexcionDB import ConexionBD,NAME


def crearEmp():
    dni=int(input('dni: '))
    nombre=str(input('nombre: '))
    apellido=str(input('apellido: '))
    telefono=int(input('Telefono: '))
    mail=input('Mail: ')
    emp=Empleado(dni,nombre,apellido,telefono,mail)
    conexionDB=ConexionBD(NAME)
    #conexionDB.cursor()
    consulta=(f'''INSERT INTO empleados (dni,nombre,apellido,telefono,mail) VALUES({emp.dni},"{emp.nomb}","{emp.ap}",{emp.telefono},"{emp.mail}")''')
    conexionDB.request(consulta)
    conexionDB.commit()
    conexionDB.closeDB()

def mostrarDatos():
    conexionDB=ConexionBD(NAME)
    consulta=('SELECT * FROM empleados')
    conexionDB.request(consulta)
    datos=conexionDB.cursor.fetchall()
    for dato in datos:
        print('----------')
        dni,nomb,ap,tel,mail=dato
        emp=Empleado(dni,nomb,ap,tel,mail)
        emp.getDatos()
    conexionDB.commit()
    conexionDB.closeDB()
    
def agregarUsuario():
    mail=input()
    contraseña=input()
    register=Register(mail,contraseña)
    conexionDB=ConexionBD(NAME)
    consulta=(f'''INSERT INTO register(nombre,contraseña) VALUES("{register.mail}","{register.psw}")''')
    conexionDB.request(consulta)
    conexionDB.commit()
    conexionDB.closeDB()

def mostrarUsersRegistrados():
    conexionDB = ConexionBD(NAME)
    consulta = 'SELECT * FROM register'
    conexionDB.request(consulta)
    datos = conexionDB.cursor.fetchall()
    for dato in datos:
        print('------------')
        numUser=dato[0]
        mail= dato[1]
        psw=dato[2]
        register = Register(numUser,mail, psw)
        register.getDatos()
    conexionDB.commit()
    conexionDB.closeDB()

def eliminarEmp():
    
    conexionDB=ConexionBD(NAME)
    query='SELECT dni,nombre FROM empleados'
    conexionDB.request(query)
    datos=conexionDB.cursor.fetchall()
    for d in datos:
        print('--------')
        print(d)
    dni=int(input('dni de la persona a eliminar: '))
    consulta=(f'DELETE FROM empleados WHERE dni={dni}')
    conexionDB.request(consulta)
    conexionDB.commit()
    conexionDB.closeDB()

def eliminarUserRegister():
    numUser=int(input('Ingrese el id del usuario a eliminar: '))
    conexionDB=ConexionBD(NAME)
    consulta=f'DELETE FROM register WHERE id={numUser}'
    conexionDB.request(consulta)
    conexionDB.commit()
    conexionDB.closeDB()

def actualizarEmp():
    conexionDB=ConexionBD(NAME)
    query=(f'SELECT dni,nombre FROM empleados')
    conexionDB.request(query)
    personas=conexionDB.cursor.fetchall()
    for per in personas:
        print(f'{per}')
    
    #try:  
    dni=int(input('DNI de la persona a editar: '))
    conexionDB=ConexionBD(NAME)
    
    consultaCheck=f'SELECT * FROM empleados WHERE dni={dni}'
    conexionDB.request(consultaCheck)
    pos=conexionDB.cursor.fetchone()
    try:
        if pos[0]!=dni:
                pass
            #if resultadoCheck==True:
        else:
            nuevoDNI=int(input('Ingrese el nuevo DNI: '))
            nuevoNombre=input('Ingrese el nuevo nombre: ')
            nuevoAp=input('Ingrese el nuevo apellido: ')
            nuevoTel=int(input('Ingrese el nuevo telefono: '))
            nuevoMail=input('Ingrese el nuevo mail: ')
            consulta=(f'UPDATE empleados SET dni={nuevoDNI},nombre="{nuevoNombre}",apellido="{nuevoAp}",telefono={nuevoTel},mail="{nuevoMail}" WHERE dni={dni}')
            conexionDB.request(consulta)
            conexionDB.commit()
            conexionDB.closeDB()
            print('REGISTRO ACTUALIZADO EXITOSAMENTE')
    except:
            print('DNI inexistente.')

def actualizarUsuarioRegistrado():
    numUser=int(input('ID del usuario a editar: '))
    conexionDB=ConexionBD(NAME)

    consulta=(f'SELECT * FROM register WHERE id={numUser}')
    conexionDB.request(consulta)
    post=conexionDB.cursor.fetchone()
    try:
        if post[0]!=numUser:
            pass
        else:
            newMail=input('Ingrese el nuevo mail: ')
            nuevaPSW=input('Ingrese la nueva contraseña: ')
            repetirPSE=input('Repita la psw: ')
            if repetirPSE==nuevaPSW:
                
                query=(f'UPDATE register SET mail="{newMail}",contraseña="{nuevaPSW}" WHERE id={numUser}')
                conexionDB.request(query)
                conexionDB.commit()
                conexionDB.closeDB()
                print('USUARIO ACTUALIZADO EXITOSAMENTE')
            else:
                print('contraseñas diferentes')
    except:
        print('ID inexistente')
        
def listar():
    listaPersonas = []
    conexionDB = ConexionBD(NAME)
    query = 'SELECT * FROM empleados ORDER BY nombre DESC'
    
    try:
        conexionDB.request(query)
        listaPersonas = conexionDB.cursor.fetchall()
        conexionDB.commit()
        conexionDB.closeDB()
    except:
        messagebox.showwarning('Error', 'Error al obtener la lista de personas')

    return listaPersonas



