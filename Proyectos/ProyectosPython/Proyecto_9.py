import tkinter as tk
from tkinter import messagebox
import random
import string

# --- Definición de Excepciones Personalizadas ---
class DatoNoNumericoError(Exception):
    pass

class LongitudInvalidaError(Exception):
    pass

class ContrasenaIncorrectaError(Exception):
    pass

# --- Clase Contraseña ---
class Contraseña:
    def __init__(self, longitud):
        self.longitud = longitud
        # Caracteres exactos de la guía
        self.caracteres_especiales = "¿¡?=)(/¨*+-%&$#!." 
        self.valor = self.generar_password()

    def generar_password(self):
        # Genera una contraseña 100% aleatoria. 
        pool = string.ascii_uppercase + string.ascii_lowercase + string.digits + self.caracteres_especiales
        # Usamos random.sample para garantizar que no haya caracteres repetidos
        if self.longitud > len(pool):
            return ''.join(random.choices(pool, k=self.longitud))
        return ''.join(random.sample(pool, self.longitud))

    def es_valida(self):
        # La clase Contraseña se encarga de su propia validación
        pwd = self.valor
        if len(pwd) < 8:
            return False, "Longitud menor a 8 caracteres."
        if not any(c.isupper() for c in pwd):
            return False, "Falta al menos una letra mayúscula."
        if not any(c.islower() for c in pwd):
            return False, "Falta al menos una letra minúscula."
        if not any(c.isdigit() for c in pwd):
            return False, "Falta al menos un número."
        if not any(c in self.caracteres_especiales for c in pwd):
            return False, "Falta un carácter especial válido."
        if len(set(pwd)) != len(pwd):
            return False, "Contiene caracteres repetidos."
        
        return True, "Cumple con todos los requisitos."

# --- Clase Cofre ---
class Cofre:
    def abrir(self, es_valida):
        if es_valida:
            tipos = {"Común": 10, "Raro": 25, "Legendario": 50}
            nombre = random.choice(list(tipos.keys()))
            return nombre, tipos[nombre]
        else:
            return "Maldito", -20

# --- Clase JuegoCazador ---
class JuegoCazador:
    def __init__(self, root):
        self.root = root
        self.root.title("Cazador de Contraseñas")
        self.puntaje = 0
        self.intentos = 0
        self.historial = {"Común": 0, "Raro": 0, "Legendario": 0, "Maldito": 0}

        # Mostrar características obligatorias en pantalla
        reglas = (
            "--- REGLAS DE LA CONTRASEÑA ---\n"
            "1. Longitud mínima de 8 caracteres.\n"
            "2. Al menos una letra mayúscula y una minúscula.\n"
            "3. Al menos un número.\n"
            "4. Un carácter especial: ¿¡?=)(/¨*+-%&$#!.\n"
            "5. NO debe tener caracteres repetidos."
        )
        tk.Label(root, text=reglas, justify="left", fg="darkblue").pack(pady=10)
        
        tk.Label(root, text="Ingresa la LONGITUD deseada para generar la contraseña:").pack(pady=5)
        self.entry = tk.Entry(root, width=15)
        self.entry.pack(pady=5)
        
        tk.Button(root, text="Generar y Abrir Cofre", command=self.jugar, bg="lightgreen").pack(pady=10)
        
        self.lbl_stats = tk.Label(root, text="Puntaje: 0 | Intentos: 0", font=('Arial', 10, 'bold'))
        self.lbl_stats.pack(pady=5)
        
        self.lbl_historial = tk.Label(root, text="Cofres: Común: 0 | Raro: 0 | Legendario: 0 | Maldito: 0")
        self.lbl_historial.pack(pady=5)

        tk.Button(root, text="Salir del Juego", command=self.root.destroy, bg="red", fg="white").pack(pady=10)

    def jugar(self):
        entrada = self.entry.get()
        self.entry.delete(0, tk.END) # Limpiar campo
        
        try:
            # 1. Validación de datos numéricos
            if not entrada.isdigit():
                raise DatoNoNumericoError("Debes ingresar un número entero para la longitud.")
            
            longitud = int(entrada)
            self.intentos += 1
            
            # 2. Validación de longitud mínima (Con penalización añadida)
            if longitud < 8:
                raise LongitudInvalidaError("La longitud que ingresaste es menor a 8 caracteres.")
            
            # Instanciamos la contraseña
            nueva_pwd = Contraseña(longitud)
            pwd_generada = nueva_pwd.valor
            es_valida, mensaje_validacion = nueva_pwd.es_valida()
            
            # 3. Validación de contraseña incorrecta
            if not es_valida:
                raise ContrasenaIncorrectaError(mensaje_validacion)
            
            # Si pasa todo, abrimos cofre bueno
            nombre_cofre, puntos = Cofre().abrir(True)
            self.puntaje += puntos
            self.historial[nombre_cofre] += 1
            
            msj_exito = (f"Contraseña generada: {pwd_generada}\n\n"
                         f"¡Felicidades! La contraseña es válida.\n"
                         f"Has abierto un cofre {nombre_cofre}.\n"
                         f"Puntos ganados: +{puntos}")
            messagebox.showinfo("¡Cofre Abierto!", msj_exito)

        except ContrasenaIncorrectaError as e:
            # Penalización por contraseña generada incorrecta
            nombre_cofre, puntos = Cofre().abrir(False)
            self.puntaje += puntos
            self.historial[nombre_cofre] += 1
            
            msj_error = (f"Contraseña generada: {pwd_generada}\n\n"
                         f"La contraseña generada al azar falló:\n{e}\n\n"
                         f"¡Abriste un cofre {nombre_cofre}!\n"
                         f"Penalización: {puntos} puntos.")
            messagebox.showwarning("Cofre Maldito", msj_error)

        except LongitudInvalidaError as e:
            # ¡Nueva penalización por equivocación del usuario!
            nombre_cofre, puntos = Cofre().abrir(False)
            self.puntaje += puntos
            self.historial[nombre_cofre] += 1
            
            msj_penalizacion = (f"¡Cuidado! {e}\n\n"
                                f"Por no seguir las reglas abriste un cofre {nombre_cofre} por equivocación.\n"
                                f"Penalización: {puntos} puntos.")
            messagebox.showwarning("¡Castigo por Longitud!", msj_penalizacion)

        except DatoNoNumericoError as e:
            # A los datos no numéricos solo les mostramos el error (para no romper el flujo)
            messagebox.showerror("Error de Entrada", str(e))
            
        finally:
            # Actualizar estadísticas siempre
            self.lbl_stats.config(text=f"Puntaje: {self.puntaje} | Intentos: {self.intentos}")
            self.lbl_historial.config(text=f"Cofres: Común: {self.historial['Común']} | Raro: {self.historial['Raro']} | "
                                           f"Legendario: {self.historial['Legendario']} | Maldito: {self.historial['Maldito']}")

# --- Ejecución Principal ---
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("450x450")
    app = JuegoCazador(root)
    root.mainloop()