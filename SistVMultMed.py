from datetime import datetime, date
import re
class Medicamento:
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = 0 
    
    def verNombreM(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med 
    
        
class Mascota:
    
    def __init__(self):
        self.__nombre= " "
        self.__historia= 0
        self.__tipo=" "
        self.__peso=" "
        self.__fecha_ingreso=" "
        self.__lista_medicamentos=[]
        
    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 
            
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarLista_Medicamentos(self,n):
        self.__lista_medicamentos = n 
    
class sistemaV:
    def __init__(self):
        self.__lista_caninos= {}
        self.__lista_felinos= {}
    
    def verificarExisteCanino(self,historia):
        for mascota in self.__lista_caninos.values():
            if historia == mascota.verHistoria():
                return True
        #solo luego de haber recorrido todo el ciclo se retorna False
        return False
        
    def verificarExisteFelino(self,historia):
        for mascota in self.__lista_felinos.values():
            if historia == mascota.verHistoria():
                return True
        #solo luego de haber recorrido todo el ciclo se retorna False
        return False
    
    def verificarExisteMedC(self,med):
        for medicamento in self.__lista_caninos.values():
            if med == medicamento.verNombreM():
                return True
        return False
    
    def verificarExisteMedF(self,med):
        for medicamento in self.__lista_felinos.values():
            if med == medicamento.verNombreM():
                return True
        return False
        
    def verNumeroCaninos(self):
        return len(self.__lista_caninos) 
    
    def verNumeroFelinos(self):
        return len(self.__lista_felinos) 
    
    def verNumeroMascotas(self):
        return len(self.__lista_caninos) + len(self.__lista_felinos)
    
    
    def ingresarCanino(self,Mascota,verHistoria):
        self.__lista_caninos[verHistoria] = Mascota

    def ingresarFelino(self,Mascota,verHistoria):
        self.__lista_felinos[verHistoria] = Mascota
   

    def verFechaIngresoF(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__lista_felinos.values():
            if historia == masc.verHistoria():
                return masc.verFecha() 
        return None
    
    def verFechaIngresoC(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__lista_caninos.values():
            if historia == masc.verHistoria():
                return masc.verFecha() 
        return None

    def verMedicamentoF(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__lista_felinos.values():
            if historia == masc.verHistoria():
                return masc.verLista_Medicamentos() 
        return None
    
    def verMedicamentoC(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        for masc in self.__lista_caninos.values():
            if historia == masc.verHistoria():
                return masc.verLista_Medicamentos() 
        return None
    
    def eliminarFelino(self, historia):
        if historia in self.__lista_felinos:
            del self.__lista_felinos[historia]
            return True
        return False
    
    def eliminarCanino(self, historia):
        return self.__lista_caninos.pop(historia,None) is not None # la expresión is not None será False, indicando que el pop no tuvo éxito
    
    def eliminarMedicamentosF(self, historia):
        for med in self.__lista_felinos.values():
            if historia == med.verHistoria():
                med.asignarLista_Medicamentos([]) #Limpia lista de medicamentos
                return True  #eliminado con exito
        return False 
    
    def eliminarMedicamentosC(self, historia):
        for med in self.__lista_caninos.values():
            if historia == med.verHistoria():
                med.asignarLista_Medicamentos([]) #Limpia lista de medicamentos
                return True  #eliminado con exito
        return False 
def error():
    '''Retorna un mensaje de que la ingreso una opcion no es valida '''
    return "\nIngreso una opción no valida, intente de nuevo.\n"

def valid_int():
    '''Valida que el dato ingresado sea un numero entero positivo '''
    while True:
        num = input(">> ")
        try:
            entero = int(num)
            if entero > 0:
                return entero
            else:
                print("\nIngrese un numero positivo")
        except ValueError:
            print("\nIngrese solo numeros enteros, intente de nuevo")
            
def valid_float():
    '''Valida que el dato ingresado sea un numero flotante'''
    while True:
        num = input(">> ")
        try:
            flotante = float(num)
            return flotante
        except ValueError:
            print("\nIngrese solo numero flotante, intente de nuevo")


def valid_letras():
    '''Valida que el dato ingresado sea de caracteres alfabetico, 
    incluyendo tildes, mayusculas, minusculas, espacio sin aceptar caracteres especiales o números '''
    while True:
        txt = input(">> ")
        try:
            if re.match("^[a-zA-Z-ñÑ-áÁéÉíÍóÓúÚ ]*$", txt):
                return txt
            else:
                print("Ingreso caracteres especiales o números")
        except ValueError:
            print("\nIngrese solo letras y espacios, intente de nuevo")

def valid_date():
    '''VSolicita una fecha y valida que esta sea correcta'''
    while True:
        print("\nIngrese el día: ")
        dia = valid_int()
        
        print("\nIngrese el mes: ")
        mes = valid_int()
        
        print("\nIngrese el año: ")
        año = valid_int()
        
        if año < 2024:
            if mes>12:
                print("\nIngrese la fecha correctamente. Intente de nuevo\n")
            elif mes == 2 and dia < 28:
                break
            elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12 < 32:
                break
            elif mes != 2 and dia < 31:
                break 
            else:
                print("\nIngrese la fecha correctamente. Intente de nuevo\n")
        else:
            print("\nIngrese la fecha correctamente. Intente de nuevo\n")
            
    fecha = date(año,mes,dia)
    print("\nFecha: ", fecha.strftime("%Y/%m/%d"))
    return str(fecha)

def main():
    servicio_hospitalario = sistemaV()
    # sistma=sistemaV()
    while True:
        menu=int(input('''\nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota 
                       \n6- Eliminar medicamento
                       \n7- Salir 
                       \nUsted ingresó la opción: ''' ))
        if menu==1: # Ingresar una mascota 
            if servicio_hospitalario.verNumeroMascotas() >= 10:
                print("No hay espacio ...") 
                continue
            masc = input("""Ingrese la opción del tipo de mascota a ingresar:
                         1.Felino
                         2.Canino
                         """)
            if masc == "1":
                historia=int(input("Ingrese la historia clínica del felino: "))
                #   verificacion=servicio_hospitalario.verDatosPaciente(historia)
                if servicio_hospitalario.verificarExisteFelino(historia) == False:
                    nombre=input("Ingrese el nombre de la mascota: ")
                    peso=int(input("Ingrese el peso de la mascota: "))
                    print("Ingrese la fecha de ingreso: ")
                    fecha = valid_date()
                    nm=int(input("Ingrese cantidad de medicamentos: "))
                    lista_med=[]

                    for i in range(0,nm):
                        nombre_medicamentos = input("Ingrese el nombre del medicamento: ")

                        medicamento_rep = False
                        for medicamento in lista_med:
                            if nombre_medicamentos == medicamento.verNombreM():
                                print("\nNo es posible recetar este medicamento porque ya ha sido recetado a esta mascota")
                                medicamento_rep = True
                                break
                        if medicamento_rep:
                            continue

                        dosis =int(input("Ingrese la dosis: "))
                        medicamento = Medicamento()
                        medicamento.asignarNombre(nombre_medicamentos)
                        medicamento.asignarDosis(dosis)
                        lista_med.append(medicamento)

                else: 
                    print("\nEl felino con esa historia clinica ya se encuentra en el sistema, intente de nuevo")

                mas= Mascota()
                mas.asignarNombre(nombre)
                mas.asignarHistoria(historia)
                mas.asignarPeso(peso)
                mas.asignarFecha(fecha)
                mas.asignarLista_Medicamentos(lista_med)
                servicio_hospitalario.ingresarFelino(mas,historia)

            elif masc == "2":
                historia=int(input("Ingrese la historia clínica del canino: "))
                #   verificacion=servicio_hospitalario.verDatosPaciente(historia)
                if servicio_hospitalario.verificarExisteCanino(historia) == False:
                    nombre=input("Ingrese el nombre de la mascota: ")
                    peso=int(input("Ingrese el peso de la mascota: "))
                    print("Ingrese la fecha de ingreso: ")
                    fecha = valid_date()
                    nm=int(input("Ingrese cantidad de medicamentos: "))
                    lista_med=[]

                    for i in range(0,nm):
                        nombre_medicamentos = input("Ingrese el nombre del medicamento: ")
                        
                        medicamento_rep = False
                        for medicamento in lista_med:
                            if nombre_medicamentos == medicamento.verNombreM():
                                print("\nNo es posible recetar este medicamento porque ya ha sido recetado a esta mascota")
                                medicamento_rep = True
                                break
                        if medicamento_rep:
                            continue
                            
                        dosis =int(input("Ingrese la dosis: "))
                        medicamento = Medicamento()
                        medicamento.asignarNombre(nombre_medicamentos)
                        medicamento.asignarDosis(dosis)
                        lista_med.append(medicamento)
                    
                else:
                    print("\nYa existe la mascota con el numero de historia clinica")

                mas= Mascota()
                mas.asignarNombre(nombre)
                mas.asignarHistoria(historia)
                mas.asignarPeso(peso)
                mas.asignarFecha(fecha)
                mas.asignarLista_Medicamentos(lista_med)
                servicio_hospitalario.ingresarCanino(mas,historia)
            else:
                print("\nIngreso una opción no valida, intente de nuevo.")

        elif menu==2: # Ver fecha de ingreso
            masc = input("""Ingrese la opción del tipo de mascota a buscar:
                         1.Felino
                         2.Canino
                         """)
            if masc == "1":
                q = int(input("Ingrese la historia clínica del felino: "))
                fecha = servicio_hospitalario.verFechaIngresoF(q)
                # if servicio_hospitalario.verificarExiste == True
                if fecha != None:
                    print("La fecha de ingreso de la mascota es: " + fecha)
                else:
                    print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

            elif masc == "2":
                q = int(input("Ingrese la historia clínica del canino: "))
                fecha = servicio_hospitalario.verFechaIngresoC(q)
                # if servicio_hospitalario.verificarExiste == True
                if fecha != None:
                    print("La fecha de ingreso de la mascota es: " + fecha)
                else:
                    print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

            else:
                print("Ingresó una opción no valida")
            
        elif menu==3: # Ver número de mascotas en el servicio 
            felinos=servicio_hospitalario.verNumeroFelinos()
            caninos=servicio_hospitalario.verNumeroCaninos()
            print(f"El número de pacientes en el sistema es: {felinos} felinos y {caninos} caninos" )

        elif menu==4: # Ver medicamentos que se están administrando
            masc = input("""Ingrese la opción del tipo de mascota a buscar:
                         1.Felino
                         2.Canino
                         """)
            if masc == "1":
                q = int(input("Ingrese la historia clínica del felino: "))
                medicamento = servicio_hospitalario.verMedicamentoF(q) 
                if medicamento != None: 
                    print("Los medicamentos suministrados son: ")
                    for m in medicamento:   
                        print(f"\n- {m.verNombreM()}")
                else:
                    print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

            elif masc == "2":
                q = int(input("Ingrese la historia clínica del canino: "))
                medicamento = servicio_hospitalario.verMedicamentoC(q) 
                if medicamento != None: 
                    print("Los medicamentos suministrados son: ")
                    for m in medicamento:   
                        print(f"\n- {m.verNombreM()}")
                else:
                    print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

            else:
                print("Ingreso una opción no valida, intente de nuevo")

        
        elif menu == 5: # Eliminar mascota
            masc = input("""Ingrese la opción del tipo de mascota a buscar:
                         1.Felino
                         2.Canino
                         """)
            if masc == "1":
                q = int(input("Ingrese la historia clínica del felino: "))
                resultado_operacion = servicio_hospitalario.eliminarFelino(q) 
                if resultado_operacion == True:
                    print("Mascota eliminada del sistema con exito")
                else:
                    print("No se ha podido eliminar la mascota")
            elif masc == "2":
                q = int(input("Ingrese la historia clínica del canino: "))
                resultado_operacion = servicio_hospitalario.eliminarCanino(q) 
                if resultado_operacion == True:
                    print("Mascota eliminada del sistema con exito")
                else:
                    print("No se ha podido eliminar la mascota")


        elif menu == 6:
            masc = input("""Ingrese la opción del tipo de mascota a buscar:
                         1.Felino
                         2.Canino
                         """)
            if masc == "1":
                q = int(input("Ingrese la historia clinica del felino: "))
                resultado_operacion = servicio_hospitalario.eliminarMedicamentosF(q)
                if resultado_operacion == True:
                    print("Medicamento eliminado del sistema con exito")
                else:
                    print("No se ha podido eliminar el medicamento")
            elif masc == "2":
                q = int(input("Ingrese la historia clinica del canino: "))
                resultado_operacion = servicio_hospitalario.eliminarMedicamentosC(q)
                if resultado_operacion == True:
                    print("Medicamento eliminado del sistema con exito")
                else:
                    print("No se ha podido eliminar el medicamento")
            else:
                print("Ingreso una opción no valida, intente de nuevo")

        elif menu==7:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break
        
        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")

if __name__=='__main__':
    main()