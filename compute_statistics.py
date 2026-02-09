"""
Módulo para calcular estadísticas básicas: Media, Mediana, Moda,
Desviación Estándar y Varianza Poblacional.
"""

import sys
import time


def calculate_statistics(numbers):
    """
    Realiza los cálculos estadísticos de una lista de números.
    """
    if not numbers:
        return None

    qty = len(numbers)
    avg = sum(numbers) / qty

    # Mediana
    ordered = sorted(numbers)
    middle = qty // 2
    if qty % 2 == 0:
        median = (ordered[middle - 1] + ordered[middle]) / 2
    else:
        median = ordered[middle]

    # Moda
    counts = {}
    for val in numbers:
        counts[val] = counts.get(val, 0) + 1
    top_freq = max(counts.values())

    if top_freq == 1 and qty > 1:
        mode = "#N/A"
    else:
        mode = [k for k, v in counts.items() if v == top_freq][0]

    # Varianza y Desviación
    var = sum((x - avg) ** 2 for x in numbers) / qty
    return qty, avg, median, mode, var**0.5, var


def main():
    """
    Función principal para procesar el archivo y mostrar resultados.
    """
    if len(sys.argv) < 2:
        print("Uso: python compute_statistics.py archivo.txt")
        return

    fname = sys.argv[1]
    start = time.time()
    data = []

    try:
        with open(fname, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    clean_val = line.strip()
                    if clean_val:
                        data.append(float(clean_val))
                except ValueError:
                    print(f"Error de dato: '{line.strip()}' ignorado.")

        res = calculate_statistics(data)
        duration = time.time() - start

        if res:
            out = (
                f"FILE: {fname}\nCOUNT: {res[0]}\nMEAN: {res[1]}\n"
                f"MEDIAN: {res[2]}\nMODE: {res[3]}\nSD: {res[4]}\n"
                f"VAR: {res[5]}\nTIME: {duration:.4f}s\n"
            )
            print(out)
            with open("StatisticsResults.txt", "a", encoding="utf-8") as f:
                f.write(out + "-" * 30 + "\n")

    except FileNotFoundError:
        print(f"Error: El archivo '{fname}' no existe.")


if __name__ == "__main__":
    main()
