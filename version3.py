class Paciente:
    def __init__(self):
      self.__nombre = ""
      self.__cedula = 0
      self.__genero = ""
      self.__servicio = ""
      
    def verNombre(self):
        return self.__nombre
    def verServicio(self):
        return self.__servicio
    def verGenero(self):
        return self.__genero
    def verCedula(self):
        return self.__cedula
    
    def asignarNombre(self,n):
        self.__nombre = n
    def asignarServicio(self,s):
        self.__servicio = s
    def asignarGenero(self,g):
        self.__genero = g
    def asignarCedula(self,c):
        self.__cedula = c

class Sistema:
    def __init__(self):
      self.__lista_pacientes = []
    #   self.__lista_pacientes = {}
    #  self.__numero_pacientes = len(self.__lista_pacientes)
      
    def ingresarPaciente(self, pac):
        self.__lista_pacientes.append(pac)

    def verNumeroPacientes(self):
        print("en el sistema hay: " + str(len(self.__lista_pacientes)) + "pacientes")
    
    def verDatosPaciente(self,c):
        for p in self.__lista_pacientes:
            if c == p.verCedula():
                return p
 
                
mi_sistema = Sistema()


def main():
    sis = Sistema()
    while True:
        opcion = int(input("1. Nuevo paciente\n - 2. Numero de paciente\n - 3. Datos paciente\n - 4. Salir:  \n"))
        if opcion == 1:
            print(" a continuación se solicitarán los datos...")
            nombre = input("Ingrese el nombre: ")
            cedula = int(input("Ingrese la cedula: "))    
            genero = input("Ingrese el genero: ")
            servicio = input("Ingrese el servicio: ")
            pac = Paciente()
            pac.asignarCedula(cedula)
            pac.asignarGenero(genero)
            pac.asignarNombre(nombre)
            pac.asignarServicio(servicio)
            
            sis.ingresarPaciente(pac)
            
        
           
            
        elif opcion == 2:
            c=int(input("ingrese la cédula a buscar: "))
            p = sis.verDatosPaciente(c)
            
        elif opcion == 3:
            mi_sistema.verDatosPaciente()
        elif opcion == 4:
            break
        else:
            print("Opcion invalida")
    
def main():
    sis = Sistema()





