import os 
import time

#--------Funciones-------
def limpiarPantalla(): 
    if os.name == 'nt':
        os.system('cls')
    else: 
        os.system('clear')

#----Programa principal------
print("Bienvenido, este programa te ayudara a saber en que rango esta el numero que ingreses.")
while True:
    try:  # La funcion del try y el except es controlar los errores. Intenta ejecutar este bloque.
        print("El prorama funciona solo con numeros mayores a 0 y menores a 5000")
        DatoUsuario = int(input("Por favor ingresa el numero: ")) 
        if DatoUsuario > 0 and DatoUsuario < 5000:
            break
        else:
            print("El numero no es valido dentro de los rangos, intentalo nuevamente. ")
            time.sleep(2) 
            limpiarPantalla()
    except ValueError:   #Si ocurre ese tipo de error, ejecuta este bloque en lugar de cerrar el programa.
        limpiarPantalla()
        print("Error: Debes ingresar un numero Entero invalido, intentalo nuevamente.")
        #time.sleep(2) 
        limpiarPantalla()

#------VAlidaciones y Fin del programa-----

if DatoUsuario < 2000:
    print(f"El número {DatoUsuario} pertence al rango BAJO.")
elif 2000 <= DatoUsuario <= 4000:
    print(f"El número {DatoUsuario} pertence al rango MEDIO.")
else:
    print(f"El número {DatoUsuario} pertence al rango Alto.")