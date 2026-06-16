import os 
import time

#-------- Funciones -------
def limpiarPantalla(): 
    if os.name == 'nt':
        os.system('cls')
    else: 
        os.system('clear')
        
#---- Programa principal ------
print("Bienvenido, este programa te ayudara a saber cuantas veces se repite un numero") 
print("tambien ayudara a calcular la potencia de acuerdo a las veces que se repite.")
time.sleep(3) 
limpiarPantalla()

Matriz = []             # Crea una matriz vacía (lista de listas)

#---- Paso 1 - llenar la matriz ----
for f in range(4):      # Recorre 4 veces para crear cada fila (bucle) la f es el contador
    Fila  = []          # Crea una fila vacía temporal
    for c in range(4):  # Recorre 4 veces para llenar cada columna de la fila
        while True:
            try:
                valor = int(input(f"Ingrese el número para la posición ({f+1},{c+1}): ")) # el +1 se pone para que el contador no inicie desde 0 y se entienda mejor
                if 3 <= valor <= 6:
                    Fila.append(valor) # Guarda el dato valido en la fila
                    break #salir del while si el dato es valido
                else:
                    print("Error, debes ingresar un numero dentro del rango aceptable")
            except ValueError:
                print("Error: debes ingresar un numero entero.")
    Matriz.append(Fila)   # Agrega la fila completa a la matriz
    
    
#------ Mostrar matriz completa -------
print("\n Matriz completa:")
for fila in Matriz: 
    print(fila)
    # print(" | ".join(str(valor) for valor in fila)) es una forma esteticamente mas bonita

#---- Paso 2 - Contar repeticiones -----
conteo = {3: 0, 4: 0, 5: 0, 6: 0}   # Se crea un diccionario llamado conteo
for fila in Matriz:                 # Recorre cada fila de la matriz (recuerda que cada fila es una lista)
    for valor in fila:              # Recorre cada número dentro de esa fila
        conteo[valor] += 1          # Aumenta en 1 el contador correspondiente al número que encontró.

#----- Paso 3 - Calcular potencias ----       
potencias = {}                                      # Es importante recordar que en el for (sera la variable donde se guardara el dato) in es para decir que busque (en este caso se le dice que busque en el diccionario de conteo)
for numero, repeticiones in conteo.items():         # Los diccionarios necesitan clave y dato, o dicho de otra forma titulo e informacion, y lo que se esta haciendo es reccorrer el diccionario conteo y darle una clave a los valores
    potencias[numero] = numero ** repeticiones      # Calcula la potencia del número elevado a la cantidad de veces que aparece:

# ---- Paso 4: Mostrar resultados ----
print("Resultados: ")
for numero in conteo:
    print(f"El número {numero} se repite {conteo[numero]} veces → {numero}^{conteo[numero]} = {potencias[numero]}")