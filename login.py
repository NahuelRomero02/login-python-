import sys
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import BOLD
import generic as utl
from conexcionDB import ConexionBD,NAME
from controladorEmpl import *

class app:
    
    def __init__(self):
        #Diseñamos la ventana grafica
        self.ventana = tk.Tk()
        self.ventana.title('Inicio sesion')
        self.ventana.geometry("1200x800")
        self.ventana.config(bg='#fcfcfc')
        #self.ventana.resizable(width=0, height=0)

        #Insertamos la imagen
        #utl.centrarVentana(self.ventana,600,400)
        #logo=utl.leerImagen("./Imagen/emp.png",(175,175))

        #Creamos el marco donde ira la imagen
        frameLogo=tk.Frame(self.ventana,bd=0,width=300,relief=tk.SOLID,padx=10,pady=10,bg='#3a7ff6')
        frameLogo.pack(side="left",expand=tk.NO,fill=tk.BOTH)
        #Rellenamos el marco
        #label=tk.Label(frameLogo,image=logo,bg='#3a7ff6')
        #label.place(x=0,y=0,relwidth=1,relheight=1)

        frameForm=tk.Frame(self.ventana,bd=0,relief=tk.SOLID,bg='#fcfcfc')
        frameForm.pack(side="right",expand=tk.YES,fill=tk.BOTH)
        
        frameFormTop=tk.Frame(frameForm,height=50,bd=0,relief=tk.SOLID,bg='black')
        frameFormTop.pack(side='top',fill=tk.X)
        #Creamos el titulo de la ventana
        title=tk.Label(frameFormTop,text="Inicio de sesion",font=('Times',30),fg="#666a88",bg='#fcfcfc',pady=50)
        title.pack(expand=tk.YES,fill=tk.BOTH)

        frameFromFill=tk.Frame(frameForm,height=50,bd=0,relief=tk.SOLID,bg='#fcfcfc')
        frameFromFill.pack(side="bottom",expand=tk.YES,fill=tk.BOTH)
        #Etiqueta usuario
        etiquetaUsuario=tk.Label(frameFromFill,text='Usuario',font=('Times',14),fg='#666a88',bg='#fcfcfc',anchor='w')
        etiquetaUsuario.pack(fill=tk.X,padx=20,pady=5)
        #obtenemos el usuario ingresado
        self.usuario=ttk.Entry(frameFromFill,font=('Times',14))
        self.usuario.pack(fill=tk.X,padx=20,pady=5)
        # Etiqueta psw
        etiquetaPsw= tk.Label(frameFromFill,text='Contraseña',font=('Times',14),fg='#666a88',bg='#fcfcfc',anchor='w')
        etiquetaPsw.pack(fill=tk.X,padx=20,pady=5)
        #obtenemos la pwd ingresada
        self.contraseña=ttk.Entry(frameFromFill,font=('Times',14))
        self.contraseña.pack(fill=tk.X,padx=20,pady=5)
        self.contraseña.config(show="*")

        # Insertamos el boton de "iniciar sesion"
        inicio=tk.Button(frameFromFill,text="Iniciar sesion",font=("Times",15,BOLD),bg="#3a7ff6",bd=0,fg="#fff",command=self.ejecutarAcciones)
        inicio.pack(fill=tk.X,padx=20,pady=20)
        inicio.bind("<Return>",(lambda event:self.verificar()))

        # Insertamos el boton de "Registrarse"

       # registrarse = tk.Button(frameFromFill, text='Registrarse', font=("Times", 15, BOLD), bg="#3a7ff6", bd=0, fg="#fff", command=self.register)
       # registrarse.pack(fill=tk.X, padx=20, pady=20)
        registrarse = tk.Button(frameFromFill, text='Registrarse', font=("Times", 15, BOLD), bg="#3a7ff6", bd=0,fg="#fff", command=self.crearRegistrar)
        registrarse.pack(fill=tk.X, padx=20, pady=20)
        
        # Insertamos el boton de "Salir"
        salir=tk.Button(frameFromFill,text='Salir',font=("Times", 15, BOLD), bg="#3a7ff6", bd=0,fg="#fff", command=self.salir)
        salir.pack(fill=tk.X,padx=20,pady=20)
        self.ventana.mainloop()
    
    def inicio(self):
        self.ventana=tk.Tk()
        self.ventana.geometry('1200x800')
        self.ventana.title('INICIO')
        self.ventana.config(bg='#fcfcfc')
        #utl.centrarVentana(self.ventana, 600, 400)
        #logo = utl.leerImagen("./Imagen/emp.png", (175, 175))

        # Creamos el marco donde irá la imagen
        frameLogo = tk.Frame(self.ventana, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg='#3a7ff6')
        frameLogo.pack(side='left',expand=tk.NO,fill=tk.BOTH)
        # Rellenamos el marco
        #label = tk.Label(frameLogo, image=logo, bg='#3a7ff6')
        #label.place(x=0,y=0,relheight=1,relwidth=1)

        frameForm = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frameForm.pack(side='right', expand=tk.YES, fill=tk.BOTH)

        frameFromFill = tk.Frame(frameForm, height=50, bd=0, relief=tk.SOLID, bg='#fcfcfc')
        frameFromFill.pack(side='bottom', expand=tk.YES, fill=tk.BOTH)

        createProducto=tk.Button(frameFromFill,font=('arial',12),text='Crear producto',bg='green',fg='white',command=self.ejActions)
        createProducto.pack(side=tk.LEFT,pady=10,padx=10)

        venta=tk.Button(frameFromFill,font=('arial',12),text='Venta',bg='green',fg='white',command=self.salir)
        venta.pack(side=tk.LEFT,pady=10,padx=10)
        
        self.ventana.mainloop()

    
    def ejActions(self):
        self.ventana.destroy()
        # self.createProducto()
        self.newWnd()



    def newWnd(self):
            #funcion para verificar si el login fue exitoso y ahi abrir la sig ventana.
        #if self.verificar():
            self.ventana=tk.Tk()
            self.ventana.geometry('1200x800')
            self.ventana.title('CRUD')
            self.ventana.config(bg='#fcfcfc')
            #utl.centrarVentana(self.ventana, 600, 400)
            #logo = utl.leerImagen("./Imagen/emp.png", (175, 175))

            # Creamos el marco donde irá la imagen
            frameLogo = tk.Frame(self.ventana, bd=0, width=300, relief=tk.SOLID, padx=10, pady=10, bg='#3a7ff6')
            frameLogo.pack(side='left',expand=tk.NO,fill=tk.BOTH)
            # Rellenamos el marco
            #label = tk.Label(frameLogo, image=logo, bg='#3a7ff6')
            #label.place(x=0,y=0,relheight=1,relwidth=1)

            frameForm = tk.Frame(self.ventana, bd=0, relief=tk.SOLID, bg='#fcfcfc')
            frameForm.pack(side='right', expand=tk.YES, fill=tk.BOTH)

            frameFromFill = tk.Frame(frameForm, height=50, bd=0, relief=tk.SOLID, bg='#fcfcfc')
            frameFromFill.pack(side='bottom', expand=tk.YES, fill=tk.BOTH)

            
            dni=tk.Label(frameFromFill,text='DNI',font=('Times',12), bg='grey')
            dni.pack(fill=tk.X,padx=20,pady=20)
            self.dni=tk.Entry(frameFromFill,font=('Times',12), bg='light gray')
            self.dni.pack(fill=tk.X,padx=20,pady=20)

            nombre=tk.Label(frameFromFill,text='NOMBRE',font=('Times',12), bg='grey')
            nombre.pack(fill=tk.X,padx=20,pady=20)
            self.entryNombre=tk.Entry(frameFromFill,font=('Times',12), bg='light gray')
            self.entryNombre.pack(fill=tk.X,padx=20,pady=20)

            apellido=tk.Label(frameFromFill,font=('Times',12),text='APELLIDO', bg='grey')
            apellido.pack(fill=tk.X,padx=20,pady=20)
            self.entryAp=tk.Entry(frameFromFill,font=('Times',12), bg='light gray')
            self.entryAp.pack(fill=tk.X,padx=20,pady=20)

            telefono=tk.Label(frameFromFill,font=('Times',12),text='TELEFONO', bg='grey')
            telefono.pack(fill=tk.X,padx=20,pady=20)
            self.entryTel=tk.Entry(frameFromFill,font=('Times',12), bg='light gray')
            self.entryTel.pack(fill=tk.X,padx=20,pady=20)


            mail=tk.Label(frameFromFill,font=('Times',12),text='MAIL', bg='grey')
            mail.pack(fill=tk.X,padx=20,pady=20)
            self.mailEntry=tk.Entry(frameFromFill,font=('Times',12), bg='light gray')
            self.mailEntry.pack(fill=tk.X,padx=20,pady=20)

            btnCrearPersona=tk.Button(frameFromFill,font=('arial',12),text='Crear Persona',command=self.guardarPersona,bg='darkgreen', fg='white')
            btnCrearPersona.pack(side=tk.LEFT,pady=10,padx=10)

            btnUpd=tk.Button(frameFromFill,font=('arial',12),text='Actualizar',bg='blue', fg='white',command=self.editarDatos)
            btnUpd.pack(side=tk.LEFT,pady=10,padx=10)

            btnSave=tk.Button(frameFromFill,font=('arial',12),text='Guardar',bg='grey',fg='white',command=self.updMen)
            btnSave.pack(side=tk.LEFT,pady=10,padx=10)

            btnEliminarPersona=tk.Button(frameFromFill,font=('arial',12),text='Eliminar Persona',bg='red',fg='white',command=self.eliminarPersona)
            btnEliminarPersona.pack(side=tk.LEFT,pady=10,padx=10)

            btnExit=tk.Button(frameFromFill,font=('arial',12),text='Salir',bg='green',fg='white',command=self.salir)
            btnExit.pack(side=tk.LEFT,pady=10,padx=10)
            

            self.tabla=ttk.Treeview(columns=('nombre','apellido','telefono','mail'))
            self.tabla.pack()
            #Texto encabezador
            self.tabla.heading('#0',text='DNI')
            self.tabla.heading('#1',text='Nombre')
            self.tabla.heading('#2',text='Apellido')
            self.tabla.heading('#3',text='Telefono')
            self.tabla.heading('#4',text='Mail')
            #Ancho de las columnas
            self.tabla.column('#0', width=100)  
            self.tabla.column('#1', width=100)  
            self.tabla.column('#2', width=100)  
            self.tabla.column('#3', width=100)  
            self.tabla.column('#4', width=150)

            self.listaPer=listar()

            for p in self.listaPer:
                dni = p[0]
                nombre = p[1]
                apellido = p[2]
                telefono =p[3]
                mail=p[4]
                
                self.tabla.insert('', 'end', text=dni, values=(nombre, apellido,telefono,mail))
            #self.ventana.lift()
            self.ventana.mainloop()

    def editarDatos(self):
        try:
            itemSeleccionado = self.tabla.focus()
            if itemSeleccionado:
                self.Dni=self.tabla.item(self.tabla.selection())['text']
                self.Name=self.tabla.item(self.tabla.selection())['values'][0]
                self.Ap=self.tabla.item(self.tabla.selection())['values'][1]
                self.Tel=self.tabla.item(self.tabla.selection())['values'][2]
                self.Mail=self.tabla.item(self.tabla.selection())['values'][3]
                self.dni.insert(0,self.Dni)
                self.entryNombre.insert(0,self.Name)
                self.entryAp.insert(0,self.Ap)
                self.entryTel.insert(0,self.Tel)
                self.mailEntry.insert(0,self.Mail)
                #info_item = self.tabla.item(itemSeleccionado)
                #valor_text = info_item['text']
        except Exception as e:
            messagebox.showerror('Error',e)

    def updMen(self):
        try:
            nameEntry=self.entryNombre.get()
            surEntry=self.entryAp.get()
            dniEntry=self.dni.get()
            if not dniEntry:
                messagebox.showerror('Error','Debe ingresar un DNI')
                return
            if not nameEntry:
                messagebox.showerror('Error','Debe ingresar un nombre')
                return
            if not surEntry:
                messagebox.showerror('Error','Debe ingresar un apellido')
                return
            else:
                self.Dni=self.tabla.item(self.tabla.selection())['text']
                conexionDB=ConexionBD(NAME)
                d=self.dni.get()
                n=self.entryNombre.get()
                a=self.entryAp.get()
                t=self.entryTel.get()
                m=self.mailEntry.get()
                consulta=f'UPDATE empleados SET dni={d},nombre="{n}",apellido="{a}",telefono={t},mail="{m}"WHERE dni={self.Dni}'
                conexionDB.request(consulta)
                conexionDB.commit()
                conexionDB.closeDB()
                self.listaPer=listar()
                self.actualizarTabla()
                messagebox.showinfo('Actualizado','Acutalizacion exitosa')
                self.dni.delete(0,tk.END)
                self.entryNombre.delete(0,tk.END)
                self.entryAp.delete(0,tk.END)
                self.entryTel.delete(0,tk.END)
                self.mailEntry.delete(0,tk.END)
        except Exception as e:
            messagebox.showerror('Error','Intente de nuevo')
            messagebox.showerror('Error ',e)

    def eliminarPersona(self):
        try:
            # Seleccionamos el item con focus()
            itemSeleccionado = self.tabla.focus()
            if itemSeleccionado:
                respuesta=messagebox.askquestion("Confirmación", "¿Seguro que deseas eliminar esta persona?")
                if respuesta=='yes':

            #if itemSeleccionado:
                    dni = self.tabla.item(itemSeleccionado)['text']

                    conexionDB = ConexionBD(NAME)
                    query = f'DELETE FROM empleados WHERE dni = {dni}'
                    conexionDB.request(query)
                    conexionDB.commit()
                    conexionDB.closeDB()

                    self.listaPer = listar()
                    self.actualizarTabla()

                    messagebox.showinfo('Registro eliminado', 'El registro se ha eliminado correctamente')
                else:
                    pass
            else:
                messagebox.showerror('Error', 'No se ha seleccionado ninguna persona')
        except:
            messagebox.showerror('Error', 'Error al eliminar persona')    
        
    def actualizarTabla(self):
    # Limpiar la tabla antes de actualizar los datos
        self.tabla.delete(*self.tabla.get_children())
    # Actualizar la tabla con los nuevos datos
        for p in self.listaPer:
            self.tabla.insert('',0,text=p[0],values=(p[1],p[2],p[3],p[4]))

    def guardarPersona(self):
        try:
            rest=list()
            entryName=self.entryNombre.get()
            entryAp=self.entryAp.get()
            entryDNI=self.dni.get()
            entryTel=self.entryTel.get()
            entryMail=self.mailEntry.get()
            conexionDB=ConexionBD(NAME)
            query=f'SELECT * FROM empleados WHERE dni={entryDNI}'
            conexionDB.request(query)
            rest=conexionDB.cursor.fetchone()
            if rest is not None:
                count = 1
            else:
                count = 0
           
            conexionDB.commit()
            conexionDB.closeDB()
        
            
            if count>0:
                
                messagebox.showerror('Error', 'Usuario ya registrado en el sistema.')
                #self.resetWnd()
                self.dni.delete(0,tk.END)
                #messagebox.showerror('error',rest)
   
                return
                
            if not entryDNI:
                messagebox.showerror('Error','Debe ingresar DNI')
                return
            if not entryName:
                messagebox.showerror('Error','Debe ingresar un nombre')
                return
            elif not entryAp:
                messagebox.showerror('Error','Debe ingresar un apellido')
                return
            elif not entryTel:
                messagebox.showerror('Error','Debe ingresar un telefono')
                return
            elif not entryMail:
                messagebox.showerror('Error','Debe ingresar un Mial')
                return

            else: 
                conexionDB=ConexionBD(NAME) 
                consulta=f'INSERT INTO empleados(dni,nombre,apellido,telefono,mail) VALUES ({entryDNI},"{entryName}","{entryAp}",{entryTel},"{entryMail}")'
                conexionDB.request(consulta)
                conexionDB.commit()           
                conexionDB.closeDB()
                self.listaPer=listar()
                self.actualizarTabla()
                self.dni.delete(0,tk.END)
                self.entryNombre.delete(0, tk.END)  # Limpiar el campo de entrada
                self.entryAp.delete(0, tk.END)
                self.entryTel.delete(0,tk.END)
                self.mailEntry.delete(0,tk.END)  # Limpiar el campo de entrada
                
                messagebox.showinfo('Registro guardado', 'El registro se ha guardado correctamente')
                return
        except Exception as e:
            messagebox.showerror('Error','Usuario registrado')
            messagebox.showerror('Error', f'Error: {str(e)}')
            
    def ejecutarAcciones(self):
        self.ventana.destroy()
        self.newWnd()
        self.verificar()
        
    
    def verificar(self):
        #self.ventana.destroy()
        #self.newWnd()
    
        usu=self.usuario.get()
        psw=self.contraseña.get()
        if not usu or not psw:
            messagebox.showerror('Error','Campos vacios.')
            return
        
        conexionBD=ConexionBD(NAME)
        consulta=(f"SELECT * FROM register WHERE mail='{usu}'")
        conexionBD.request(consulta)
        usuarios=conexionBD.cursor.fetchone()

        if not usuarios:
            messagebox.showerror('Error','El usuario no existe')
            return
        if psw==usuarios[2]:
            messagebox.showinfo('Iniciando sesion','Registro exitoso')
          
            self.ventana.destroy()
            self.inicio()
 
            return
        else:
            messagebox.showerror('Error','Usuario o contraseña invalidas')
        
        conexionBD.commit()
        conexionBD.closeDB()

    def crearRegistrar(self):
        self.ventanaRegistro = tk.Toplevel()
        self.ventanaRegistro.title('Registro')
        self.ventanaRegistro.geometry('150x170')
        self.ventanaRegistro.config(background='#fcfcfc')

        # Calcula el ancho del fondo azul
        

        labelNombre = tk.Label(self.ventanaRegistro, text="Nombre:", font=("arial", 10))
        labelNombre.pack()

        self.entryNombre = tk.Entry(self.ventanaRegistro)
        self.entryNombre.pack()

        self.labelContraseña = tk.Label(self.ventanaRegistro, text="Contraseña:", font=("arial", 10))
        self.labelContraseña.pack()

        self.entryContraseña = tk.Entry(self.ventanaRegistro, show="*")
        self.entryContraseña.pack()

        labelRepContraseña = tk.Label(self.ventanaRegistro, text="Repetir Contraseña:", font=("arial", 10))
        labelRepContraseña.pack()

        self.entryRepContraseña = tk.Entry(self.ventanaRegistro, show="*")
        self.entryRepContraseña.pack()

        boton = tk.Button(self.ventanaRegistro, text='Registrarse', command=self.registrarUsuario)
        boton.pack()

        btnSalir = tk.Button(self.ventanaRegistro, text='Salir', command=self.salirRegistro)
        btnSalir.pack()
        
    def registrarUsuario(self):
        mail = self.entryNombre.get()
        contraseña = self.entryContraseña.get()
        repContraseña = self.entryRepContraseña.get()
    ## Verificamos que la contraseña cumpla una serie de pautas.
        if mail == "":
            messagebox.showerror('Error', 'Debe ingresar un nombre')
            self.ventanaRegistro.lift()
            return
        if contraseña == "":
            messagebox.showerror('Error', 'Debe ingresar una contraseña')
            self.ventanaRegistro.lift()
            return
        if len(contraseña)<4:
            messagebox.showerror('Error', 'La contraseña debe contener mas de 4 caracteres')
            self.ventanaRegistro.lift()
            return
        if repContraseña == "":
            messagebox.showerror('Error', 'Debe repetir la contraseña ingresada')
            self.ventanaRegistro.lift()
            return
        if contraseña != repContraseña:
            messagebox.showerror('Error','Las contraseñas no coinciden, intentelo de nuevo')
            self.ventanaRegistro.lift()
            return
        try:
            # Conexión a la base de datos
            conexionBd=ConexionBD(NAME)

            # Insertar el nuevo usuario en la tabla 'register'
            #conexionBd.request("INSERT INTO register (nombre, contraseña) VALUES (?, ?)", (nombre, contraseña))
            consulta = f"INSERT INTO register (mail, contraseña) VALUES ('{mail}', '{contraseña}')"
            conexionBd.request(consulta)
            conexionBd.commit()

            messagebox.showinfo('Registrado','Registro exitoso')
            conexionBd.closeDB()
            self.ventanaRegistro.destroy()
            
        except Exception as e:
            messagebox.showerror('Error', str(e))
        # Metodo para salir de la ventana de registro   
             
    def salirRegistro(self):
            self.ventanaRegistro.destroy() 
    def listar():
    # Conectamos a la base de datos
        conexionBD=ConexionBD(NAME)
        cursor = conexionBD.cursor()

        # Ejecutamos una consulta para obtener todos los registros de la tabla 'personas'
        cursor.execute("SELECT dni, nombre, apellido, telefono, mail FROM personas")
        lista_personas = cursor.fetchall()

        # Cerramos la conexión a la base de datos
        conexionBD.close()

        return lista_personas

    def salir(self):
        sys.exit()    
    