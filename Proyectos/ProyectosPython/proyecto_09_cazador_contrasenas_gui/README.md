# 🔑 Password Hunter - Juego de Ciberseguridad & Lógica (GUI)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![GUI](https://img.shields.io/badge/UI-Tkinter-lightgrey?style=for-the-badge)
![Security](https://img.shields.io/badge/Estandar-Criptograf%C3%ADa-red?style=for-the-badge)

Un videojuego interactivo de escritorio basado en mecánicas de rol y gamificación donde el objetivo principal es generar llaves criptográficas robustas para desbloquear cofres de distintas rarezas.

## ✨ Características Destacadas
* **Validaciones Basadas en Excepciones Propias:** Define una jerarquía robusta de errores personalizados heredando directamente de la superclase `Exception`:
  * `DatoNoNumericoError`
  * `LongitudInvalidaError`
  * `ContrasenaIncorrectaError`
* **Políticas de Seguridad Criptográfica:** El motor de contraseñas valida en tiempo de ejecución directrices OWASP (Presencia obligatoria de mayúsculas, minúsculas, dígitos numéricos, caracteres especiales explícitos y ausencia total de caracteres repetidos).
* **Lógica Transaccional Seguro:** Incorporación de bloques estructurados `try-except-finally` que garantizan la actualización estadística del perfil del jugador (Puntaje y cofres descubiertos) sin importar la ocurrencia de fallos de entrada.