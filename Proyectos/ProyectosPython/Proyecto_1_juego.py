import random #importo un modulo de python que es una biblioteca estandar de python, relacionado con el azar
import os #Importa el módulo os que proporciona una forma de usar funcionalidades dependientes del sistema operativo.
import time #Funciona para manejar tiempos y pausas en el programa para la pausa es llamar una pausa es time.sleep(2) o el tiempo que quiera

#Definicion de Datos. FUNCIONES
#------FUNCIONES------
def limpiarPantalla(): #Esto es una funcion, se crea de esta manera y se llama asi limpiarPantalla() y hara lo que aqui abajo se le pida que haga
    # Determina el sistema operativo para usar el comando correcto
    if os.name == 'nt': # 'nt' es para Windows
        os.system('cls')
    else: # 'posix' es para sistemas tipo Unix (Linux, macOS)
        os.system('clear')
        
def MenuPrincipal():
    print("--Menu principal-- \n ¿Que deseas hacer? \n 1) entrar al bosque \n 2) buscar objeto magico \n 3) salir del juego\n")

#------- INICIO DEL JUEGO ------1
limpiarPantalla()
print("Bienvenidos al bosque encantado")
time.sleep(1) 
limpiarPantalla()
#n\ es para que en el print el texto siguiente a su posicion sea en un renglon abajo

MenuPrincipal()
SeleccionMenuInicio = input("Ingresa el numero segun tu eleccion: ")
time.sleep(1)
limpiarPantalla()


#-------Bucle Principal-----------
while SeleccionMenuInicio != "3":
    #----------Seleccion numero 1: empezar aventura---------
    if SeleccionMenuInicio == "1":
        print ("Has elegido entrar en el bosque.\nahora puedes ir por: \n1) un camino iluminado \n2) un camino oscuro ")
        while True:
            SeleccionCamino = input("Elije tu camino 1 o 2: ")
            if SeleccionCamino in ("1","2"):
                break
            else:
                print("La opcion no es valida en la seleccion de camino.")

        # CAMINO ILUMINADO        
        if SeleccionCamino == "1":
            time.sleep(1)
            limpiarPantalla()
            print("--CAMINO ILUMINADO--")
            while True:
                DecisionDescanso = input("Haz llegado a un hermoso lago donde puedes descansar. \n¿Quieres descansar? Escribe si o no, segun tu eleccion: ")
                DecisionDescanso = DecisionDescanso.lower()#.lower convierte las letras en minusculas
                if DecisionDescanso in ("si", "no"):
                    break
                else:
                    print("La opcion no es valida, intentalo nuevamente")
            if DecisionDescanso == "si":
                print("¡Felicidades! \nRecuperaste energía, saliste del bosque.")
            
            elif DecisionDescanso == "no":
                print("No recuperaste energía. \nNo lograste salir del bosque, vuelve a intentarlo desde el menú principal.")
            time.sleep(2)
            limpiarPantalla()

        # CAMINO OSCURO    
        elif SeleccionCamino == "2":
            print("--CAMINO OSCURO--")
            print("llegaste a un lugar oscuro y peligroso. \nExiste la posibilidad de encontrarte con un monstruo.")
            time.sleep(2)
            EncuentroConCriatura = random.choice([True,False]) #la forma en que se usa el random con los parametros que yo seleccione.
            if EncuentroConCriatura == True:              #True = hay encuentro false = no hay encuentro.
                print("¡Oh no!, ¡te has encontrado con una criatura magica!")
                while True: 
                    DecisionCriuatura = input("pero no te preocupes, la criatura te da la opcion de: \n1) luchar \no \n2) negociar \n¿que quieres hacer? 1 o 2: ") 
                    if DecisionCriuatura == "1":
                        print("¡Entraste en combate con la criatura!")
                        Energia = random.choice([True,False]) #True = Sobrevivir False = No Sobrevivir.
                        if Energia:
                            print("¡Felicidades! Sobreviviste a la batalla, lograste salir del bosque.")
                            print("Regresas al menú principal. \n")
                        else:
                            print("Lo siento… perdiste la batalla pero no el juego. Vuelves al menú principal para intentarlo otra vez.")
                            print("Regresas al menú principal. \n")
                        break #Rompe el blucle de la criatura - Termina encuentro
                    elif DecisionCriuatura == "2":
                        print("Propones una negociacion magica")
                        print("Entregas un poco de energía a cambio de unos zapatos encantados que te permiten caminar más rápido. \nGracias a ellos logras salir del bosque con éxito.")                   
                        break
                    else:
                        print("Opcion invalida, intenta nuevamente.")
            else:
                print("¡Felicidades! No encontraste ninguna criatura y lograste salir del bosque.\n haz finalizado el juego.")  
            time.sleep(2)
            limpiarPantalla()   

    #--------Seleccion Opción 2: objetos magicos-----------
    elif SeleccionMenuInicio == "2":
        limpiarPantalla()
        print("¿Que poder te acompañara en tu aventura?. \n Estos son los objetos: \n 1) Espada legendaria. \n 2) Escudo legendario. \n 3) Pociom de energia.")      

        #While true y su estructura se le conoce como sub-bucle
        while True: #Todas las respuestas son validas, pero con las lista se aplica a que las mencionadas sean las unicas validas
            SeleccionObjetoMagico = input ("ingrese el numero segun tu eleccion de objeto magico: ").strip()#es para borrar espacios en blaco
            if SeleccionObjetoMagico in ("1", "2", "3"): #es para que busque dentro de las lista si esta la opcion, siendo la respuesta positiva saldra del bucle
                break #Fuerza a Cerrar el bucle
            else:
                print("Opción no válida en la búsqueda mágica.") #no deja salir del bucle hasta que den una respuesta valida  

        if SeleccionObjetoMagico == "1":
            print("Buscas en la cueva oscura... ¡Encuentras la espada magica!, lo que te da mas poder de ataque.\n")
        elif SeleccionObjetoMagico == "2":
            print("Buscas en la cueva oscura... ¡Descubre el Escudo ancestral!, lo que te da mas defensa.\n")
        elif SeleccionObjetoMagico == "3":
            print("Te acercas al rio encantado... ¡hallaste una poción de Energia!, util para recuperar energia.\n") 
        time.sleep(2)
        limpiarPantalla()

    #-----Opcion invalida-----       
    else:
        print("opcion no valida, intenta de nuevo")
        time.sleep(1)
        limpiarPantalla()

    #-- SIEMPRE VUELVE AQUI AL MENÚ PRINCIPAL--
    MenuPrincipal()
    SeleccionMenuInicio = input("ingresa el numero segun tu elección: ")
    time.sleep(1)
    limpiarPantalla()

#---------mensaje al seleccionar la opcion 3: salida del juego----------
limpiarPantalla()
print("Gracias por jugar al bosque encantado. \n¡Hasta pronto aventurero!")       
