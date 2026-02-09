"""
Módulo para contar la frecuencia de palabras.
Crea un archivo de resultados independiente por cada archivo de prueba.
"""

import sys
import time
import os


def process_words(file_path):
    """
    Lee el archivo especificado y cuenta la frecuencia de cada palabra.
    Retorna un diccionario con las palabras y sus conteos.
    """
    w_map = {}
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            for line in file:
                words = line.strip().split()
                for word in words:
                    clean_w = word.lower()
                    w_map[clean_w] = w_map.get(clean_w, 0) + 1
        return w_map
    except FileNotFoundError:
        print(f"Error: El archivo {file_path} no existe.")
        return None


def main():
    """
    Función principal que coordina la lectura, el conteo y la escritura
    de resultados en archivos independientes.
    """
    if len(sys.argv) < 2:
        return

    path = sys.argv[1]
    start_t = time.time()
    counts = process_words(path)

    if counts is not None:
        base = os.path.basename(path).split('.')[0]
        out_name = f"{base}_results.txt"
        header = f"{'PALABRA':<20} | {'FRECUENCIA':<10}"
        out = f"ARCHIVO: {path}\n{header}\n" + "-" * 35 + "\n"
        sorted_items = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        for word, freq in sorted_items:
            out += f"{word:<20} | {freq:<10}\n"
        out += f"\nTIEMPO: {time.time() - start_t:.4f}s\n"
        print(f"Guardado en: {out_name}")
        with open(out_name, "w", encoding="utf-8") as f_out:
            f_out.write(out)


if __name__ == "__main__":
    main()
