
import re

# ==============================================================================
#                      MÓDULO 1: ENTRADA Y VALIDACIÓN
# ==============================================================================

def validar_numero_registros(prompt):
    """Solicita y valida un entero positivo mayor a 0."""
    while True:
        try:
            valor = input(prompt).strip()
            # Valida que solo sean dígitos y convierte a entero.
            if not valor.isdigit():
                print(f"ERROR: Debe ingresar un número entero válido (solo dígitos numericos).")
                continue
            
            numero = int(valor)
            # Valida que los números deben ser mayor a 0.
            if numero <= 0:
                print(f"ERROR: El número debe ser mayor a cero.")
                continue
            return numero
        except ValueError:
            # En caso de error inesperado, aunque isdigit lo previene
            pass

def validar_cadenas_texto(prompt, es_departamento=False):
    """Solicita y valida Nombre o Departamento."""
    # Caracteres especiales, numeros y de puntuación prohibidos
    CARACTERES_PROHIBIDOS = r'[!@#$%^&*()_+=\-[\]{};\'":\\|,.<>/?`~0-9]'
    
    DEPARTAMENTOS_VALIDOS = ["VENTAS", "RECURSOS HUMANOS", "TECNOLOGIA", "FINANZAS", "ATENCION AL CLIENTE", "MARKETING"]

    while True:
        cadena = input(prompt).strip()

        # Validar que el campo no esté vacío (ni solo espacios)
        if not cadena:
            print(f"ERROR: El campo no puede estar vacío.")
            continue
        
        # No ingresar números cuando se solicita texto
        if re.search(r'\d', cadena):
            print(f"ERROR: El texto no debe contener números.")
            continue

        # Validar que no haya caracteres especiales ni números prohibidos
        if re.search(CARACTERES_PROHIBIDOS, cadena):
            print(f"ERROR: El texto contiene caracteres especiales o prohibidos.")
            continue
        
        # Entra al camino de revisar departamento y valida que sean los permitidos
        if es_departamento:
            cadena_Convertida_MAYUSCULAS = cadena.upper()
            
            # Verifica que el departamento ingresado esté en la lista de válidos
            if cadena_Convertida_MAYUSCULAS not in DEPARTAMENTOS_VALIDOS:
                print(f"ERROR: El departamento debe ser uno de los válidos.")
                continue
            # Retorna el departamento en formato Título si es válido
            return cadena_Convertida_MAYUSCULAS.title() 
        
        # Retorna el nombre en formato Título
        return cadena.title() 

def validar_salario(prompt):
    """Solicita y valida el salario."""
    while True:
        salario_Texto = input(prompt).strip()
        
        try:
            # Simplifica la cadena para aceptar formato decimal
            salario_Modificado_Texto = salario_Texto.replace(",", "").replace("$", "").strip()
            
            # convierte a un número (decimal)
            salario = float(salario_Modificado_Texto)
            
            # verifica que los números sean mayor a 0
            if salario <= 0:
                print("ERROR: El salario debe ser un valor positivo y mayor a cero.")
                continue
            
            return salario
        except ValueError:
            print("ERROR: Debe ingresar un valor numérico válido para el salario.")

def validar_desempeno(prompt):
    """Solicita y valida el nivel de desempeño."""
    while True:
        desempeno_Texto = input(prompt).strip()
        try:
            desempeno_numero = int(desempeno_Texto)
            
            # Validar que esté entre 1 y 5
            if desempeno_numero < 1 or desempeno_numero > 5:
                print("ERROR: El nivel de desempeño debe ser un número entero entre 1 y 5.")
                continue
            
            return desempeno_numero
        except ValueError:
            print("ERROR: El nivel de desempeño debe ser un número entero válido (1 a 5).")

# ==============================================================================
#                   MÓDULO 2: CÁLCULOS CENTRALES
# ==============================================================================

def calcular_bono_y_salario_anual(salario_mensual, nivel_desempeno):
    """ Calcula el bono anual y el salario anual total """
    # 1. Calcular Salario Anual Base
    SALARIO_ANUAL_BASE = salario_mensual * 12

    # 2. Definir porcentaje de bono
    if nivel_desempeno == 5:
        porcentaje_bono = 0.20
    elif nivel_desempeno == 4:
        porcentaje_bono = 0.15
    elif nivel_desempeno == 3:
        porcentaje_bono = 0.10
    elif nivel_desempeno == 2:
        porcentaje_bono = 0.05
    else: # Nivel 1
        porcentaje_bono = 0.00
    
    # 3. Calcular Bono Anual
    bono_anual = SALARIO_ANUAL_BASE * porcentaje_bono
    
    # 4. Calcular Salario Anual Total
    salario_anual_total = SALARIO_ANUAL_BASE + bono_anual
    
    return SALARIO_ANUAL_BASE, bono_anual, salario_anual_total

# ==============================================================================
#                MÓDULO 3: PROCESAMIENTO POR EMPLEADO 
# ==============================================================================

def procesar_empleado():
    """Orquestación completa: captura de datos, cálculo de salario y agrupación en un diccionario para un empleado."""
    # Captura de datos ingresados por el usuario 
    print("\n--- INGRESO DE DATOS DEL EMPLEADO ---")
    nombre = validar_cadenas_texto(" Ingrese el Nombre del empleado: ")
    # Validar que el departamento ingresado esté en la lista de departamentos permitidos
    departamento = validar_cadenas_texto(" Ingrese el Departamento: ", es_departamento=True)
    salario_mensual = validar_salario(" Ingrese el Salario Mensual: $")
    desempeno = validar_desempeno(" Ingrese el Nivel de Desempeño (1 al 5): ")
    
    # Cálculo del salario anual base, bono y total
    salario_anual_base, bono_anual, salario_anual_total = calcular_bono_y_salario_anual(salario_mensual, desempeno)
    
    # Agrupar todos los datos del empleado en un diccionario
    empleado = {
        "Nombre": nombre,
        "Departamento": departamento,
        "Salario Mensual": salario_mensual,
        "Desempeño": desempeno,
        "Salario Anual Base": salario_anual_base,
        "Bono Anual": bono_anual,
        "Salario Anual Total": salario_anual_total
    }
    
    print(f"\n Empleado '{nombre}' procesado con éxito. Salario anual Total: ${salario_anual_total:,.2f}")
    return empleado

# ==============================================================================
#                MÓDULO 4: REPORTE Y ESTADÍSTICAS 
# ==============================================================================

def calcular_nomina_total(empleados):
    """Calcula el total de la nómina anual."""
    # Usa una expresión generadora para sumar el salario anual de todos los empleados
    nomina_total = sum(e["Salario Anual Total"] for e in empleados)
    return nomina_total

def encontrar_salario_maximo(empleados):
    """    Encuentra y retorna una LISTA de empleados que tienen el salario anual total más alto. (Maneja empates)"""
    if not empleados:
        return [] # Retorna una lista vacía si no hay empleados
    
    # 1. Encontrar el valor máximo de Salario Anual Total
    # Usamos max() con una clave lambda para obtener el SAT más alto.
    salario_maximo_valor = max(empleados, key=lambda e: e["Salario Anual Total"])["Salario Anual Total"]
    
    # 2. Recorrer la lista y filtrar a todos los que coincidan con ese valor (Manejo de Empates)
    empleados_salarios_maximos = []
    for empleado in empleados:
        if empleado["Salario Anual Total"] == salario_maximo_valor:
            empleados_salarios_maximos.append(empleado)
            
    return empleados_salarios_maximos

def generar_reporte(empleados, nomina_total, empleado_salario_maximo):
    """Muestra el reporte final en consola."""
    
    print("\n" + "="*50)
    print("          REPORTE FINAL DE NÓMINA ANUAL ")
    print("="*50 + "\n")

    # 1. Salario Anual Total para cada empleado
    print(" 1. SALARIO ANUAL TOTAL POR EMPLEADO (Incluyendo el Bono) ---")
    for empleado in empleados:
        print(f" {empleado['Nombre']} ({empleado['Departamento']}): ${empleado['Salario Anual Total']:,.2f}")
    
    print("\n" + "-"*50)
    
    # 2. Total de la nómina anual de todos los empleados
    print(f" 2. TOTAL DE LA NÓMINA ANUAL GLOBAL: ${nomina_total:,.2f}")
    
    print("-"*50)
    
    # 3. El empleado/s con el salario anual más alto
    print(f" 3. EMPLEADO/S CON EL SALARIO ANUAL MÁS ALTO:")
    if empleado_salario_maximo:
        # Itera sobre la lista de empleados máximos (puede ser 1 o más)
        for empleado in empleado_salario_maximo:
            print(f" Nombre: {empleado['Nombre']}")
            print(f" Departamento: {empleado['Departamento']}")
            # Solo se imprime una vez el valor máximo, aunque se puede repetir en cada línea
        print(f"Salario Anual Total Máximo: ${empleado_salario_maximo[0]['Salario Anual Total']:,.2f}")
    else:
        print("No se registraron empleados para el cálculo de máximo.")
    print("\n" + "="*50)


# ==============================================================================
#                      FUNCIÓN PRINCIPAL (MAIN)
# ==============================================================================

def main():
    """Función principal que orquesta el flujo del programa."""
    # Mostrar mensaje de bienvenida
    print("="*60)
    print("  Bienvenido al Sistema de Nómina y Desempeño de Empleados  ")
    print("  Tenga en cuenta las reglas de validación.")
    print("\nComo serán los datos que se van a solicitar:")
    print("1- Ingresar el número de empleados a registrar.")
    print("2- Escribir el nombre completo del empleado.")
    print("3- Indicar el departamento al que pertenece (Ventas, Recursos Humanos, Tecnología, Finanzas, Atención al Cliente o Marketing).")
    print("4- Ingresar el salario mensual.")
    print("5- Seleccionar el nivel de desempeño en escala de 1 a 5.")

    print("="*60)
    
    # Solicitar y validar número de empleados
    numero_empleados = validar_numero_registros("Ingrese el número de empleados a registrar: ")
    
    # Inicializar la Lista vacía para los registros
    empleados = [] 
    
    # Bucle principal de repetición (Estructura de Repetición)
    for i in range(numero_empleados):
        print(f"\n\n====================== REGISTRO {i + 1} de {numero_empleados} ======================")
        
        # Procesar al empleado, obtener el diccionario
        registro_empleado = procesar_empleado()
        
        # Añadir a la lista global
        empleados.append(registro_empleado)
    
    # ------------------ CÁLCULOS FINALES Y REPORTE ------------------
    if empleados:
        # Calcular Nómina Total
        nomina_total = calcular_nomina_total(empleados)
        
        # Encontrar Empleado Máximo
        empleado_maximo = encontrar_salario_maximo(empleados)
        
        # Generar Reporte Final
        generar_reporte(empleados, nomina_total, empleado_maximo)
    else:
        print("\nPrograma finalizado sin registro de empleados.")

# Punto de entrada de la ejecución del programa
if __name__ == "__main__":
    main()
