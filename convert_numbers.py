"""
Módulo para convertir números decimales a Binario y Hexadecimal.
Cumple con los estándares PEP-8 y maneja archivos de entrada.
"""

import sys
import time


def to_binary(num):
    """Convierte un número a binario manualmente."""
    if num == 0:
        return "0"
    res = ""
    val = abs(int(num))
    while val > 0:
        res = str(val % 2) + res
        val //= 2
    return "-" + res if num < 0 else res


def to_hexadecimal(num):
    """Convierte un número a hexadecimal manualmente."""
    if num == 0:
        return "0"
    chars = "0123456789ABCDEF"
    res = ""
    val = abs(int(num))
    while val > 0:
        res = chars[val % 16] + res
        val //= 16
    return "-" + res if num < 0 else res


def main():
    """Función principal para la conversión de bases numéricas."""
    if len(sys.argv) < 2:
        return

    fname = sys.argv[1]
    start = time.time()
    results = []

    try:
        with open(fname, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    val = line.strip()
                    if val:
                        n_val = int(float(val))
                        results.append((n_val, to_binary(n_val),
                                       to_hexadecimal(n_val)))
                except ValueError:
                    print(f"Dato inválido: {line.strip()}")

        duration = time.time() - start
        header = f"{'DEC':>10} | {'BIN':>20} | {'HEX':>10}"
        output = f"FILE: {fname}\n{header}\n" + "-" * 45 + "\n"

        for item in results:
            output += f"{item[0]:>10} | {item[1]:>20} | {item[2]:>10}\n"

        output += f"\nTIME: {duration:.4f}s\n"
        print(output)

        with open("ConversionResults.txt", "a", encoding="utf-8") as f_out:
            f_out.write(output + "=" * 45 + "\n")

    except FileNotFoundError:
        print(f"Error: {fname} no encontrado.")


if __name__ == "__main__":
    main()
