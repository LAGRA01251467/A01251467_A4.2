# A01251467_A4.2
# Software Engineering Graded Task: Python Exercises

Este repositorio contiene la resolución de tres programas desarrollados en Python, enfocados en el manejo de archivos, lógica algorítmica y cumplimiento de estándares de calidad de código (PEP-8).

* **Nombre:** Luis Alberto Gutiérrez Rivera
* **Matrícula:** A01251467

---

## 🛠️ Descripción de los Programas

### 1. Estadísticas de Datos (`compute_statistics.py`)
Calcula medidas de tendencia central y dispersión a partir de archivos con datos numéricos.
* **Resultados:** Media, Mediana, Moda, Desviación Estándar y Varianza.
* **Archivo de salida:** `StatisticsResults.txt`

### 2. Conversión de Números (`convert_numbers.py`)
Convierte números decimales extraídos de archivos de texto a sus representaciones Binaria y Hexadecimal mediante algoritmos manuales (sin funciones integradas de conversión).
* **Archivo de salida:** `ConversionResults.txt`

### 3. Conteo de Palabras (`word_count.py`)
Identifica la frecuencia de cada palabra distinta en archivos de texto.
* **Resultados:** Genera un archivo independiente por cada caso de prueba (TC).
* **Archivos de salida:** `TCx_results.txt` (donde x es el número del caso de prueba).

---

## 💎 Calidad de Código
Todos los scripts han sido evaluados con la herramienta **Pylint**, obteniendo una calificación de **10.00/10**, lo que garantiza:
* Cumplimiento total del estándar **PEP-8**.
* Documentación adecuada mediante *docstrings*.
* Nombres de variables significativos y estructura modular.

---

## 🚀 Instrucciones de Ejecución

Para ejecutar los programas, utiliza los siguientes comandos en tu terminal:

```bash
# Ejercicio 1
python compute_statistics.py tests/TC1.txt

# Ejercicio 2
python convert_numbers.py tests/TC1.txt

# Ejercicio 3
python word_count.py tests/TC1.txt
