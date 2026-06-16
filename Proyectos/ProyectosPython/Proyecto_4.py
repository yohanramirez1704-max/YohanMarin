# ==============================================================================
# FUNCIONES SIN PARÁMETROS 
# ==============================================================================
    
def Mostrar_instrucciones ():
    """
    Muestra el mensaje de bienvenida y las reglas de codificación de los libros (Tipo, Área),
    preparando al usuario para ingresar un código válido.
    """
    print("\n===============================")
    print("BIENVENIDO A LA BIBLIOTECA LEXUS")
    print("===============================\n")
    print("Recuerde:")
    print("> Código del libro de 6 dígitos")
    print("> 1 = General")
    print("> 2 = Colección")
    print("> 3 = Reserva")
    print("> Áreas entre 101 y 108\n")
    
def Mostrar_menu_opciones ():
    """
    Muestra las tres opciones disponibles para el usuario después de ingresar un código: 
    1. Préstamo, 2. Recolección, 3. Salir.
    """
    print("Opciones:")
    print("1. Préstamo")
    print("2. Recolección")
    print("3. Salir")
    
# ==============================================================================
# FUNCIONES CON PARÁMETROS
# ==============================================================================

def validar_codigo(codigo):
    """
    Validación del Código: Verifica que el código sea de 6 dígitos y que se ajuste a las reglas de la biblioteca: 
    1) El primer dígito (el tipo) debe ser 1, 2 o 3. 
    2) Los dígitos del 2 al 4 (el area) deben estar entre 101 y 108. Devuelve 1 si es válido y 0 si es inválido.
    """
    # Verificar que sean 6 dígitos numéricos
    if len(codigo) != 6 or not codigo.isdigit():
        return 0

    tipo = int(codigo[0])       # Primer dígito
    area = int(codigo[1:4])     # Dígitos 2 a 4

    # Validar tipo
    if tipo not in [1, 2, 3]:
        return 0

    # Validar área
    if area < 101 or area > 108:
        return 0

    return 1   # Todo correcto


def validar_opcion(opcion):
    """
    Validación de Opción: Verifica si la opción ingresada por el usuario es "1", "2" o "3". 
    Devuelve 1 si es válida y 0 si no lo es.
    """
    if opcion in ["1", "2", "3"]:
        return 1
    return 0


def procesar_prestamo(tipo):
    """
    Calcula el número de días que se permite para el préstamo, 
    basándose en el tipo de libro (8, 3 o 1 día).
    """
    if tipo == 1:
        return 8
    elif tipo == 2:
        return 3
    else:
        return 1


def procesar_recoleccion(tipo):
    """
    Calcula el valor a pagar por el usuario (la multa/cargo), 
    basándose en el tipo de libro ($500, $1000 o $5000).
    """
    if tipo == 1:
        return 500
    elif tipo == 2:
        return 1000
    else:
        return 5000


# ==============================================================================
# FUNCIÓN PRINCIPAL (MAIN)
# ==============================================================================

def main():
    """
    Es la función principal. Inicializa contadores (contador_prestamos, dinero_recolectado), 
    maneja el bucle principal, coordina la entrada del código, 
    valida las opciones y llama a las funciones de procesamiento (procesar_prestamo, procesar_recoleccion).
    """
    contador_prestamos = 0
    dinero_recolectado = 0

    while True:
        
        Mostrar_instrucciones ()        

        # Solicitar código
        codigo = input("Ingrese el código del libro: ")

        # Validar código
        if validar_codigo(codigo) == 0:
            print("\nCódigo inválido. Intente de nuevo.")
            continue

        print("✔ Código válido.\n")

        while True:
            # Mostrar menú (Dentro del bucle secundario)
            Mostrar_menu_opciones ()

            opcion = input("\nSeleccione una opción: ")

            # Validar opción
            if validar_opcion(opcion) == 0:
                print("\nOpción inválida. Intente de nuevo.")
                continue  # <--- Vuelve a la PARTE SUPERIOR de este bucle (Vuelve a pedir la opción)
            
            # Si la opción es válida, salimos del bucle secundario
            break

        opcion = int(opcion)
        tipo = int(codigo[0])

        # Opción 1 – Préstamo
        if opcion == 1:
            dias = procesar_prestamo(tipo)
            contador_prestamos += 1
            print(f"\nEl libro fue prestado por {dias} días.")

        # Opción 2 – Recolección
        elif opcion == 2:
            pago = procesar_recoleccion(tipo)
            dinero_recolectado += pago
            print(f"\nEl usuario debe pagar: ${pago}")

        # Opción 3 – Salir
        elif opcion == 3:
            print("\n===== RESUMEN DEL DÍA =====")
            print(f"Total de libros prestados: {contador_prestamos}")
            print(f"Total dinero recolectado: ${dinero_recolectado}")
            print("\nGracias por usar Biblioteca Lexus.")
            break


# Llamada al programa principal
main()
