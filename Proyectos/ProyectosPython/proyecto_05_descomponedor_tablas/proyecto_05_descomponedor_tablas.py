# ==============================================================================
# FUNCIONES SIN PARÁMETROS 
# ==============================================================================

def mostrar_instrucciones():
    """
    Es la función de bienvenida. Su único propósito es imprimir en la consola las reglas y requisitos del programa, 
    guiando al usuario sobre el formato de entrada esperado.
    """
    print("\n=======================================================")
    print("      PROGRAMA MODULAR DE DESCOMPOSICIÓN Y TABLAS")
    print("=======================================================")
    print("Requisitos:")
    print("1. Debe ingresar un número EXACTO de 6 dígitos.")
    print("2. El número se descompondrá en tres pares: A, B, y C.")
    print("3. Se generarán las tablas de multiplicar desde A hasta B.")
    print("4. Para que funcione, el número A debe ser menor que B (A < B).")
    print("=======================================================")

# ==============================================================================
# FUNCIONES CON PARÁMETROS
# ==============================================================================

def verificar(numero_ingresado):
    """
    Validación: Comprueba rigurosamente dos cosas: 
    1) Que la cadena tenga exactamente 6 caracteres. 
    2) Que todos esos caracteres sean dígitos numéricos. 
    Devuelve 1 si es válido y 0 si no lo es.
    """
    # 1. Comprueba que tenga 6 caracteres
    if len(numero_ingresado) != 6:
        return 0
    # 2. Comprueba que todos los caracteres sean dígitos
    if not numero_ingresado.isdigit():
        return 0
    
    return 1

def calcular_tabla(A, B):
    """
    Cálculo: Genera y muestra todas las tablas de multiplicar (del 1 al 10) 
    para cada número en el rango que va desde A hasta B (incluyendo ambos).
    """
    print(f"\n--- Generando Tablas desde {A} hasta {B} ---")
    
    # Bucle EXTERIOR: Itera desde el número A hasta el número B (incluido)
    for i in range(A, B + 1): 
        linea_tabla = f"Tabla del {i}: "
        
        # Bucle INTERIOR: Genera la multiplicación de 1 a 10
        for j in range(1, 11):
            resultado = i * j
            # Formatea la salida para que sea legible
            linea_tabla += f"{i}x{j}={resultado} "
        
        print(linea_tabla)
    print("-------------------------------------------------")


def unir(A, C):
    """
    Manipulación Numérica: Su objetivo es reconstruir un número de 4 dígitos. 
    Utiliza el formato de relleno con ceros (:02d) 
    para asegurar que los números de un solo dígito (ej., 5) se conviertan correctamente a dos caracteres ("05"). 
    Concatena estas dos cadenas y devuelve el resultado como un entero.
    """
    # Convertir A y C a string, asegurando que si son menores que 10 se rellenen con '0' a la izquierda (ej. 5 -> "05").
    A_texto = f"{A:02d}"
    C_texto = f"{C:02d}"
    
    # Concatenar las cadenas de texto (unirlas)
    numero_final_texto = A_texto + C_texto
    
    # Devolver el resultado final convertido a ENTERO
    return int(numero_final_texto)

# ==============================================================================
# FUNCIÓN PRINCIPAL (MAIN)
# ==============================================================================

def main(): 
    """
    Es la función principal que actúa como el que dirige el programa. 
    Contiene el bucle principal (while True), pide la entrada del usuario, 
    coordina la llamada a todas las demás funciones (verificar, calcular_tabla, unir), 
    y maneja la lógica de validación. 
    """
    while True:
        mostrar_instrucciones()

        numero_ingresado = input("Ingrese el número de 6 dígitos: ")

        # Validar 6 dígitos
        if verificar(numero_ingresado) == 0:
            print("\nError: El valor debe ser un número entero de 6 dígitos EXACTOS.")
            continue # Vuelve al inicio del bucle

        # Descomponer el número
        A = int(numero_ingresado[0:2])  # Dígitos 1 y 2
        B = int(numero_ingresado[2:4])  # Dígitos 3 y 4
        C = int(numero_ingresado[4:6])  # Dígitos 5 y 6

        print(f"\nNúmero aceptado. Descomposición: A={A}, B={B}, C={C}")

        # Validar A < B
        if A >= B:
            print(f"\nError: El número A ({A}) debe ser menor que B ({B}).")
            print("Por favor, ingrese un número donde los primeros dos dígitos sean menores que los siguientes dos.")
            continue # Vuelve al inicio del bucle

        # Llamar a la función calcular_tabla
        calcular_tabla(A, B)

        # Llamar a la función unir
        numero_unido = unir(A, C)
        
        # Mostrar el número final
        print(f"Número final: La unión de A ({A}) y C ({C}) es: {numero_unido:04d}")

        # Preguntar si desea continuar
        input("\nPresione ENTER para ingresar un nuevo número...")

# Ejecución de la función principal
main()
