import csv
import json

def csv_a_json(archivo_csv, archivo_json):
    with open(archivo_csv, encoding='utf-8') as csvf:
        lector_csv = csv.DictReader(csvf)
        filas = list(lector_csv)

    with open(archivo_json, 'w', encoding='utf-8') as jsonf:
        json.dump(filas, jsonf, indent=4, ensure_ascii=False)

csv_a_json('products.csv', 'productos_json.json')
