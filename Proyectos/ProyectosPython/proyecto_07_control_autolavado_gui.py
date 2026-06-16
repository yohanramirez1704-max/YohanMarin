import tkinter as tk
from tkinter import messagebox, simpledialog
import re  # Se utiliza para validar formatos estrictos (placas y horas)

# --- 1. CLASE LÓGICA (DEFINICIÓN DEL OBJETO) ---
class AutoLavado:
    def __init__(self, placa, tarifa_hora):
        # Atributos privados (Encapsulamiento). En Python se usa __ para que sean estrictamente privados.
        self.__placa = placa
        self.__tarifa_hora = tarifa_hora
        self.__hora_ingreso = None # Se inicializa vacío, se llena con el método registrar_ingreso

    def _convertir_a_minutos(self, hora_str):
        # Método interno de apoyo para transformar el texto "HH:MM" en minutos totales matemáticos
        horas, minutos = map(int, hora_str.split(":"))
        return (horas * 60) + minutos

    # --- Métodos solicitados exactamente por el Ejercicio 3 ---

    def registrar_ingreso(self, hora):
        # Asigna la hora de llegada al atributo privado
        self.__hora_ingreso = hora

    def registrar_salida(self, hora):
        # Valida que la hora de salida sea lógica (posterior o igual a la de entrada)
        if not self.__hora_ingreso:
            return False
        
        minutos_entrada = self._convertir_a_minutos(self.__hora_ingreso)
        minutos_salida = self._convertir_a_minutos(hora)
        
        if minutos_salida >= minutos_entrada:
            return True
        return False

    def calcular_pago(self, hora_salida):
        # Calcula la diferencia de tiempo en minutos y la multiplica por la tarifa
        minutos_entrada = self._convertir_a_minutos(self.__hora_ingreso)
        minutos_salida = self._convertir_a_minutos(hora_salida)
        
        tiempo_total_minutos = minutos_salida - minutos_entrada
        if tiempo_total_minutos <= 0: 
            tiempo_total_minutos = 1 # Se cobra como mínimo 1 minuto de servicio
            
        horas_decimales = tiempo_total_minutos / 60
        return round(horas_decimales * self.__tarifa_hora, 2)

    def obtener_placa(self):
        # Permite leer la placa de forma segura desde fuera de la clase
        return self.__placa
        
    def obtener_hora_ingreso(self):
        # Método auxiliar para poder imprimir el recibo
        return self.__hora_ingreso

# --- 2. INTERFAZ GRÁFICA (MANEJO DE LA VENTANA) ---
class AppAutolavado:
    def __init__(self, ventana):
        # Configuración de la ventana (El usuario final ve esto en inglés)
        self.ventana = ventana
        self.ventana.title("Car Wash Control System - Phase 2")
        self.ventana.geometry("480x650")
        self.ventana.config(padx=25, pady=25)
        
        # Lista interna donde guardaremos los objetos creados a partir de la clase AutoLavado
        self.lista_vehiculos = [] 

        # --- Elementos Visuales (Etiquetas y Botones en Inglés) ---
        tk.Label(ventana, text="VEHICLE REGISTRATION", font=("Arial", 14, "bold")).pack(pady=10)
        
        tk.Label(ventana, text="License Plate (3 Letters & 3 Numbers):").pack()
        self.entrada_placa = tk.Entry(ventana, font=("Arial", 11), justify="center")
        self.entrada_placa.pack(pady=5)

        tk.Label(ventana, text="Entry Time (Format HH:MM):").pack()
        self.entrada_hora = tk.Entry(ventana, font=("Arial", 11), justify="center")
        self.entrada_hora.pack(pady=5)

        tk.Button(ventana, text="Register Entry", bg="#2ecc71", fg="white", 
                  font=("Arial", 10, "bold"), command=self.procesar_registro, width=25).pack(pady=20)

        tk.Label(ventana, text="VEHICLES IN PROCESS", font=("Arial", 11, "bold")).pack(pady=5)
        self.caja_lista = tk.Listbox(ventana, width=50, height=10, font=("Courier", 10))
        self.caja_lista.pack(pady=5)

        tk.Button(ventana, text="Process Exit & Payment", bg="#3498db", fg="white", 
                  font=("Arial", 10, "bold"), command=self.procesar_salida, width=25).pack(pady=15)

    def procesar_registro(self):
        # Limpieza de espacios y paso a mayúsculas
        placa_ingresada = self.entrada_placa.get().upper().strip()
        hora_ingresada = self.entrada_hora.get().strip()

        # Validación 1: Formato de placa estricto
        if not re.match(r"^[A-Z]{3}[0-9]{3}$", placa_ingresada):
            messagebox.showerror("Invalid Plate", "Use 3 letters and 3 numbers (e.g., ABC123).")
            return

        # Validación 2: Formato de hora real de 24 horas (00:00 a 23:59)
        if not re.match(r"^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$", hora_ingresada):
            messagebox.showerror("Invalid Time", "Use HH:MM format (24h).")
            return

        # Validación 3: Impedir que la misma placa se registre dos veces
        for vehiculo in self.lista_vehiculos:
            if vehiculo.obtener_placa() == placa_ingresada:
                messagebox.showwarning("Duplicate", f"Vehicle {placa_ingresada} is already registered.")
                return

        # Creación del objeto AutoLavado (Instanciación)
        nuevo_auto = AutoLavado(placa_ingresada, 5000) # Se asume una tarifa de $5000 por hora
        nuevo_auto.registrar_ingreso(hora_ingresada) # Uso del método solicitado
        
        # Se añade a la lista interna y se muestra en la interfaz
        self.lista_vehiculos.append(nuevo_auto)
        self.caja_lista.insert(tk.END, f" {placa_ingresada}  | In: {hora_ingresada}")
        
        # Limpiamos los campos de texto
        self.entrada_placa.delete(0, tk.END)
        self.entrada_hora.delete(0, tk.END)
        messagebox.showinfo("Success", f"Vehicle {placa_ingresada} registered successfully.")

    def procesar_salida(self):
        # Verificamos que el usuario haya hecho clic en un auto de la lista visual
        seleccion = self.caja_lista.curselection()
        if not seleccion:
            messagebox.showwarning("Selection Error", "Please select a vehicle from the list.")
            return

        indice_seleccionado = seleccion[0]
        vehiculo_seleccionado = self.lista_vehiculos[indice_seleccionado]

        # Ventana emergente para solicitar la hora de salida
        hora_salida = simpledialog.askstring("Exit Time", f"Enter exit time (HH:MM) for {vehiculo_seleccionado.obtener_placa()}:")

        # Validación de la hora ingresada en la ventana emergente
        if hora_salida and re.match(r"^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$", hora_salida):
            
            # Verificamos lógicamente que la hora de salida no sea anterior a la de entrada
            if vehiculo_seleccionado.registrar_salida(hora_salida):
                
                # Ejecutamos el método que calcula el costo
                total_a_pagar = vehiculo_seleccionado.calcular_pago(hora_salida)
                
                # Desplegamos el recibo final para el cliente
                messagebox.showinfo("Payment Receipt", 
                    f"--- CAR WASH RECEIPT ---\n\n"
                    f"PLATE: {vehiculo_seleccionado.obtener_placa()}\n"
                    f"ENTRY: {vehiculo_seleccionado.obtener_hora_ingreso()}\n"
                    f"EXIT:  {hora_salida}\n"
                    f"---------------------------\n"
                    f"TOTAL TO PAY: ${total_a_pagar}\n\n"
                    f"Thank you for your visit!")
                
                # Retiramos el vehículo tanto de la lista interna (memoria) como de la visual
                self.lista_vehiculos.pop(indice_seleccionado)
                self.caja_lista.delete(indice_seleccionado)
            else:
                messagebox.showerror("Time Error", "Exit time cannot be earlier than entry time.")
        elif hora_salida:
            # Si escribió algo pero el formato no era HH:MM
            messagebox.showerror("Invalid Format", "Please use HH:MM format.")

# --- INICIALIZACIÓN DEL SISTEMA ---
if __name__ == "__main__":
    raiz = tk.Tk()
    raiz.eval('tk::PlaceWindow . center') # Comando para centrar la ventana en la pantalla
    aplicacion = AppAutolavado(raiz)
    raiz.mainloop()
