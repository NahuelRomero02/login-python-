class Empleado:
    def __init__(self,dni,nombre,apellido,telefono,mail):
        #self.numPer=numPersona
        self.dni=dni
        self.nomb=nombre
        self.ap=apellido
        self.telefono=telefono
        self.mail=mail
    def getDatos(self):
        #print(f'NUM PERSONA: {self.numPer}')
        print(f"DNI: {self.dni}")
        print(f"Nombre: {self.nomb}")
        print(f"Apellido: {self.ap}")
        print(f"Telefono: {self.telefono}")
        print(f"Mail: {self.mail}")
class Register:
    def __init__(self,numUser,mail,contraseña):
        self.user=numUser
        self.mail=mail
        self.psw=contraseña
        
    def getDatos(self):
        print(f'Num User: {self.user}')
        print(f"User: {self.user}")
        print(f"PSW: {self.psw}")
    