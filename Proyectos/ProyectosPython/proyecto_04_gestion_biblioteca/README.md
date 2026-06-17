# 📚 Sistema de Control de Biblioteca "Lexus"

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Architecture](https://img.shields.io/badge/Dise%C3%B1o-Modular-purple?style=for-the-badge)

Un software modular simulado de administración bibliotecaria enfocado en la validación posicional de códigos estructurados para realizar cálculos automáticos de préstamos y recolección financiera de libros.

## ✨ Características Destacadas
* **Validación de Códigos mediante Slicing:** Descompone cadenas de 6 dígitos numéricos usando técnicas avanzadas de rebanado de strings para verificar identificadores (Tipo de libro y área de conocimiento).
* **Simulador Financiero Integrado:** Lógica de negocio segmentada que calcula multas monetarias en base a días de retraso o tarifas preestablecidas según la categoría del libro.
* **Generador de Reportes de Cierre:** Al finalizar la jornada, el sistema compila la contabilidad financiera total y el contador neto de préstamos efectuados.

## 🛠️ Funciones Core
* `validar_codigo(codigo)`: Inspecciona la integridad del formato (Longitud, pertenencia numérica, tipos válidos del 1-3 y áreas del 101-108).
* `procesar_prestamo(tipo)` / `procesar_recoleccion(tipo)`: Controladores funcionales de la lógica de negocio del inventario.