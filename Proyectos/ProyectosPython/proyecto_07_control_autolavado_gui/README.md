# 🚗 Car Wash Control System (GUI)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![GUI](https://img.shields.io/badge/UI-Tkinter-lightgrey?style=for-the-badge)
![POO](https://img.shields.io/badge/Paradigma-POO--Encapsulado-darkgreen?style=for-the-badge)

Aplicación de escritorio con interfaz gráfica interactiva (GUI) orientada a la administración del tiempo de ingreso y liquidación de tarifas financieras en un centro de lavado automotriz.

## ✨ Características Destacadas
* **Encapsulamiento de Datos Estricto:** Atributos de clase protegidos bajo un esquema de privacidad fuerte en Python (`__placa`, `__tarifa_hora`) evitando mutaciones externas accidentales.
* **Parseo de Tiempo (Horas a Minutos):** Algoritmo de conversión matemática interna para procesar cadenas en formato estricto de tiempo `HH:MM` y realizar cálculos precisos de facturación por minutos.
* **Ecosistema UI Dinámico:** Implementación de listas visuales (`tk.Listbox`), cuadros de diálogo modales (`messagebox`) y controles de validación en tiempo real por medio de expresiones regulares.

## 📐 Arquitectura de Clases
* `AutoLavado`: Entidad lógica pura encargada de las reglas de negocio y cálculo financiero.
* `AppAutolavado`: Orquestador de la UI, ventanas secundarias y layouts visuales.