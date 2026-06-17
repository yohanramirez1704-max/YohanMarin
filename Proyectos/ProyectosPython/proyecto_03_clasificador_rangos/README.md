# 📈 Clasificador Dinámico de Rangos Numéricos

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Stability](https://img.shields.io/badge/Control_de_Errores-Try%2FExcept-red?style=for-the-badge)

Herramienta lógica de terminal diseñada para interactuar con datos ingresados por el usuario, categorizando los números en rangos preestablecidos (Bajo, Medio, Alto) bajo una política estricta de tolerancia a fallos.

## ✨ Características Destacadas
* **Control de Excepciones Profesional:** Captura asertiva de fallos de tipo (`ValueError`) para evitar la interrupción abrupta del hilo de ejecución si se introducen cadenas de texto o caracteres vacíos.
* **Filtros de Entrada Acotados:** Restringe el procesamiento numérico estrictamente a valores mayores a 0 y menores a 5000.
* **Estructuración Fluida:** Uso estratégico de pausas cronometradas mediante `time.sleep` para optimizar la lectura del usuario.