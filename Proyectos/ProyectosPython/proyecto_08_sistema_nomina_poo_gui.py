import tkinter as tk
from tkinter import messagebox, simpledialog, ttk
import re

# =========================================================
# LÓGICA DE NEGOCIO (POO)
# =========================================================

class Empleado:
    """
    CLASE PADRE (SUPERCLASE): Define la estructura base.
    """
    def __init__(self, nombre, identificacion, salario_base):
        self.nombre = nombre
        self.identificacion = identificacion
        self.salario_base = salario_base

    def calcular_salario(self):
        pass

    def mostrar_informacion(self, mostrar_salario=False, mostrar_detalles=False):
        informacion = f"ID: {self.identificacion} | Name: {self.nombre}"
        if mostrar_salario:
            informacion += f" | Total Salary: ${self.calcular_salario():,.2f}"
        return informacion

class EmpleadoTiempoCompleto(Empleado):
    def __init__(self, nombre, identificacion, salario_base, bono_desempeno):
        super().__init__(nombre, identificacion, salario_base)
        self.bono_desempeno = bono_desempeno

    def calcular_salario(self):
        return self.salario_base + self.bono_desempeno

    def mostrar_informacion(self, mostrar_salario=False, mostrar_detalles=False):
        informacion = super().mostrar_informacion(mostrar_salario)
        if mostrar_detalles:
            informacion += f" | [Role: Full-Time] (Base: ${self.salario_base:,.2f} + Perf. Bonus: ${self.bono_desempeno:,.2f})"
        return informacion

class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, identificacion, tarifa_hora, horas_trabajadas):
        super().__init__(nombre, identificacion, salario_base=tarifa_hora)
        self.horas_trabajadas = horas_trabajadas

    def calcular_salario(self):
        return self.salario_base * self.horas_trabajadas

    def mostrar_informacion(self, mostrar_salario=False, mostrar_detalles=False):
        informacion = super().mostrar_informacion(mostrar_salario)
        if mostrar_detalles:
            informacion += f" | [Role: Hourly] ({self.horas_trabajadas}h x ${self.salario_base:,.2f})"
        return informacion

class EmpleadoComision(Empleado):
    def __init__(self, nombre, identificacion, salario_base, ventas, porcentaje):
        super().__init__(nombre, identificacion, salario_base)
        self.ventas = ventas
        self.porcentaje = porcentaje / 100.0

    def calcular_salario(self):
        return self.salario_base + (self.ventas * self.porcentaje)

    def mostrar_informacion(self, mostrar_salario=False, mostrar_detalles=False):
        informacion = super().mostrar_informacion(mostrar_salario)
        if mostrar_detalles:
            informacion += f" | [Role: Commission] (Base: ${self.salario_base:,.2f} | Sales: ${self.ventas:,.2f} at {self.porcentaje*100}%)"
        return informacion

class Bonificable:
    def __init__(self):
        self.lista_bonificaciones = []

    def agregar_bonificacion(self, monto):
        self.lista_bonificaciones.append(monto)

    def obtener_bonificaciones(self):
        return sum(self.lista_bonificaciones)

class EmpleadoTiempoCompletoBonificado(EmpleadoTiempoCompleto, Bonificable):
    def __init__(self, nombre, identificacion, salario_base, bono_desempeno):
        EmpleadoTiempoCompleto.__init__(self, nombre, identificacion, salario_base, bono_desempeno)
        Bonificable.__init__(self)

    def calcular_salario(self):
        return super().calcular_salario() + self.obtener_bonificaciones()

    def mostrar_informacion(self, mostrar_salario=False, mostrar_detalles=False):
        informacion = super().mostrar_informacion(mostrar_salario)
        if mostrar_detalles:
            extras = self.obtener_bonificaciones()
            informacion += f" | [Role: FT + MultiBonus] (Extras accumulated: ${extras:,.2f})"
        return informacion

class GestorNomina:
    def __init__(self):
        self.lista_empleados = []

    def agregar_empleado(self, emp):
        self.lista_empleados.append(emp)

    def existe_empleado(self, id_buscado):
        return any(e.identificacion == id_buscado for e in self.lista_empleados)

    def calcular_total(self):
        return sum(e.calcular_salario() for e in self.lista_empleados)

# =========================================================
# INTERFAZ GRÁFICA (CON MEJORAS DE VALIDACIÓN)
# =========================================================

class AplicacionNomina:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Payroll System Phase 3 - Enhanced")
        
        ancho_ventana = 800
        alto_ventana = 600
        ancho_pantalla = self.ventana.winfo_screenwidth()
        alto_pantalla = self.ventana.winfo_screenheight()
        pos_x = (ancho_pantalla // 2) - (ancho_ventana // 2)
        pos_y = (alto_pantalla // 2) - (alto_ventana // 2)
        self.ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{pos_x}+{pos_y}")
        self.ventana.config(padx=10, pady=10)

        self.gestor = GestorNomina()

        tk.Label(ventana, text="EMPLOYEE MANAGEMENT", font=("Arial", 14, "bold")).pack(pady=5)
        
        frame_entradas = tk.Frame(ventana)
        frame_entradas.pack(pady=5)

        tk.Label(frame_entradas, text="ID Number (6-10 digits):").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.ent_id = tk.Entry(frame_entradas, width=30)
        self.ent_id.grid(row=0, column=1)

        tk.Label(frame_entradas, text="Full Name (Name & Lastname):").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.ent_nom = tk.Entry(frame_entradas, width=30)
        self.ent_nom.grid(row=1, column=1)

        tk.Label(frame_entradas, text="Base Salary / Rate (COP):").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        self.ent_sal = tk.Entry(frame_entradas, width=30)
        self.ent_sal.grid(row=2, column=1)
        
        tk.Label(frame_entradas, text="(Min Wage: $1,300,000 | Min Hourly: $5,500)", font=("Arial", 8, "italic"), fg="gray").grid(row=3, column=1, sticky="w")

        btns_frame = tk.Frame(ventana)
        btns_frame.pack(pady=10)
        
        tk.Button(btns_frame, text="Add Full-Time", bg="#2ecc71", fg="white", font=("Arial", 9, "bold"), width=18, 
                  command=self.registrar_tiempo_completo).grid(row=0, column=0, padx=5, pady=5)
        
        tk.Button(btns_frame, text="Add Hourly", bg="#3498db", fg="white", font=("Arial", 9, "bold"), width=18, 
                  command=self.registrar_por_horas).grid(row=0, column=1, padx=5, pady=5)
        
        tk.Button(btns_frame, text="Add Commission", bg="#e67e22", fg="white", font=("Arial", 9, "bold"), width=18, 
                  command=self.registrar_comision).grid(row=1, column=0, padx=5, pady=5)
        
        tk.Button(btns_frame, text="Add FT + MultiBonus", bg="#9b59b6", fg="white", font=("Arial", 9, "bold"), width=18, 
                  command=self.registrar_mixto_bonificado).grid(row=1, column=1, padx=5, pady=5)

        tk.Label(ventana, text="EMPLOYEE LIST", font=("Arial", 11, "bold")).pack()
        self.variable_vista = tk.StringVar(value="Basic Info")
        cb = ttk.Combobox(ventana, textvariable=self.variable_vista, values=["Basic Info", "Info + Salary", "Full Details"], state="readonly")
        cb.pack(pady=5)
        cb.bind("<<ComboboxSelected>>", lambda e: self.refrescar_pantalla())

        list_frame = tk.Frame(ventana)
        list_frame.pack(pady=5, fill=tk.BOTH, expand=True, padx=20)
        sy = tk.Scrollbar(list_frame, orient=tk.VERTICAL)
        sx = tk.Scrollbar(list_frame, orient=tk.HORIZONTAL)
        self.listbox = tk.Listbox(list_frame, width=100, height=8, yscrollcommand=sy.set, xscrollcommand=sx.set, font=("Courier", 9))
        sy.config(command=self.listbox.yview)
        sx.config(command=self.listbox.xview)
        sy.pack(side=tk.RIGHT, fill=tk.Y)
        sx.pack(side=tk.BOTTOM, fill=tk.X)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        tk.Button(ventana, text="Add Extra Bonus to Mixed Employee", bg="#f1c40f", font=("Arial", 10, "bold"), 
                  command=self.agregar_bonificacion_extra).pack(pady=5)
        
        self.lbl_total = tk.Label(ventana, text="Total Monthly Payroll: $0.00 COP", font=("Arial", 12, "bold"), fg="red")
        self.lbl_total.pack(pady=5)

    # --- LÓGICA DE CONTROL MEJORADA ---

    def validar_entradas(self):
        i, n, s = self.ent_id.get().strip(), self.ent_nom.get().strip(), self.ent_sal.get().strip()
        
        # Mejora de error en ID
        if not i.isdigit() or not (6 <= len(i) <= 10):
            messagebox.showerror("ID Error", "The ID must contain exactly between 6 and 10 numbers. No letters or symbols.")
            return None
        if self.gestor.existe_empleado(i):
            messagebox.showerror("Duplicate ID", f"The ID {i} is already registered in the system.")
            return None
        # Mejora de error en Nombre
        if any(char.isdigit() for char in n) or not re.match(r"^[A-Za-záéíóúÁÉÍÓÚñÑ]+(\s+[A-Za-záéíóúÁÉÍÓÚñÑ]+)+$", n):
            messagebox.showerror("Name Error", "Please enter at least one Name and one Lastname (separated by a space, no numbers).")
            return None
        # Mejora de error en Salario
        try:
            val_s = float(s)
            if val_s <= 0: raise ValueError
        except ValueError:
            messagebox.showerror("Salary Error", "Salary must be a positive numeric value. Do not use symbols like '$' or ','.")
            return None

        return n, i, val_s

    def limpiar_campos(self):
        self.ent_id.delete(0, tk.END)
        self.ent_nom.delete(0, tk.END)
        self.ent_sal.delete(0, tk.END)

    def registrar_tiempo_completo(self):
        res = self.validar_entradas()
        if res:
            if res[2] < 1300000:
                messagebox.showerror("Salary Error", "Base salary cannot be less than $1,300,000 COP.")
                return
            perf = simpledialog.askinteger("Performance", "Level 1-5:", minvalue=1, maxvalue=5)
            if perf is not None:
                bonus = {1:0, 2:50000, 3:100000, 4:150000, 5:300000}[perf]
                self.gestor.agregar_empleado(EmpleadoTiempoCompleto(res[0], res[1], res[2], bonus))
                self.limpiar_campos()
                self.refrescar_pantalla()

    def registrar_por_horas(self):
        res = self.validar_entradas()
        if res:
            if res[2] < 5500:
                messagebox.showerror("Salary Error", "Hourly rate cannot be less than $5,500 COP.")
                return
            hrs = simpledialog.askinteger("Hours", "Hours worked (must be positive):", minvalue=1)
            if hrs is not None:
                self.gestor.agregar_empleado(EmpleadoPorHoras(res[0], res[1], res[2], hrs))
                self.limpiar_campos()
                self.refrescar_pantalla()

    def registrar_comision(self):
        res = self.validar_entradas()
        if res:
            if res[2] < 1300000:
                messagebox.showerror("Salary Error", "Base salary cannot be less than $1,300,000 COP.")
                return

            ventana_comision = tk.Toplevel(self.ventana)
            ventana_comision.title("Commission Details")
            ventana_comision.geometry("380x200")
            ventana_comision.transient(self.ventana)
            ventana_comision.grab_set()
            ventana_comision.focus_force() # Asegura que la ventana tome el foco

            tk.Label(ventana_comision, text=f"Data for {res[0]}:", font=("Arial", 10, "bold")).pack(pady=10)
            marco_intern = tk.Frame(ventana_comision)
            marco_intern.pack(pady=5)
            
            tk.Label(marco_intern, text="Total Sales in COP (Money amount):").grid(row=0, column=0, sticky="e", padx=5, pady=5)
            entrada_ventas = tk.Entry(marco_intern)
            entrada_ventas.grid(row=0, column=1)

            tk.Label(marco_intern, text="Commission % (e.g. 5):").grid(row=1, column=0, sticky="e", padx=5, pady=5)
            entrada_porcentaje = tk.Entry(marco_intern)
            entrada_porcentaje.grid(row=1, column=1)

            def finalizar():
                try:
                    v = float(entrada_ventas.get())
                    p = float(entrada_porcentaje.get())
                    if v < 0 or p <= 0 or p > 100:
                        messagebox.showerror("Error", "Sales cannot be negative. Commission must be between 1 and 100.", parent=ventana_comision)
                        return
                    self.gestor.agregar_empleado(EmpleadoComision(res[0], res[1], res[2], v, p))
                    self.limpiar_campos()
                    self.refrescar_pantalla()
                    ventana_comision.destroy()
                    messagebox.showinfo("Success", "Commission Employee registered successfully.")
                except ValueError:
                    messagebox.showerror("Error", "Please enter valid numeric amounts.", parent=ventana_comision)

            tk.Button(ventana_comision, text="Register", bg="#e67e22", fg="white", font=("Arial", 10, "bold"), command=finalizar).pack(pady=10)

    def registrar_mixto_bonificado(self):
        res = self.validar_entradas()
        if res:
            if res[2] < 1300000:
                messagebox.showerror("Salary Error", "Base salary cannot be less than $1,300,000 COP.")
                return
            perf = simpledialog.askinteger("Initial Performance", "Level 1-5:", minvalue=1, maxvalue=5)
            if perf is not None:
                bonus = {1:0, 2:50000, 3:100000, 4:150000, 5:300000}[perf]
                self.gestor.agregar_empleado(EmpleadoTiempoCompletoBonificado(res[0], res[1], res[2], bonus))
                self.limpiar_campos()
                self.refrescar_pantalla()

    def agregar_bonificacion_extra(self):
        idx = self.listbox.curselection()
        if idx:
            emp = self.gestor.lista_empleados[idx[0]]
            if isinstance(emp, Bonificable):
                monto = simpledialog.askfloat("Extra Bonus", "Amount (COP) to add to bonus list:", minvalue=1)
                if monto is not None:
                    emp.agregar_bonificacion(monto)
                    self.refrescar_pantalla()
            else: messagebox.showerror("Restriction", "This employee type is not eligible for extra bonuses.")
        else: messagebox.showwarning("Selection Error", "Please select an employee from the list first.")

    def refrescar_pantalla(self):
        self.listbox.delete(0, tk.END)
        v = self.variable_vista.get()
        s, d = (v != "Basic Info"), (v == "Full Details")
        for e in self.gestor.lista_empleados:
            self.listbox.insert(tk.END, e.mostrar_informacion(s, d))
        self.lbl_total.config(text=f"Total Monthly Payroll: ${self.gestor.calcular_total():,.2f} COP")

if __name__ == "__main__":
    root = tk.Tk()
    AplicacionNomina(root)
    root.mainloop()
