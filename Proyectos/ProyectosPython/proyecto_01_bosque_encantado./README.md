# 🌲 El Bosque Encantado - Juego de Rol en Consola

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Interface](https://img.shields.io/badge/Interfaz-Consola-orange?style=for-the-badge)

Una aventura interactiva de toma de decisiones basada en texto que sumerge al usuario en un entorno místico. El juego gestiona la navegación mediante menús estructurados de opción múltiple y flujos de lógica condicional interactiva.

## ✨ Características Destacadas
* **Control de Pantalla Dinámico:** Implementa limpieza automática de terminal adaptada tanto para entornos Windows (`cls`) como Unix/Linux/macOS (`clear`).
* **Validación Robusta de Entradas:** Estructuras de bucle infinito controlado que aseguran que el usuario solo pueda avanzar mediante opciones válidas.
* **Sistema de Recompensas por Azar:** Utiliza el módulo nativo `random` para simular mecánicas de suerte y hallazgos en la exploración de mazmorras/cuevas.

## 🛠️ Estructura de Funciones
* `limpiarPantalla()`: Detecta el sistema operativo subyacente mediante el módulo `os` y limpia la consola para mantener una interfaz limpia.
* `MenuPrincipal()`: Renderiza las opciones iniciales del ecosistema de juego de forma estructurada.
