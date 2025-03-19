# csv-a-json

Este proyecto contiene un script de Python que permite convertir datos de un archivo CSV a un archivo JSON de manera eficiente y estructurada. Es útil para transformar datos tabulares en un formato más flexible como JSON, ampliamente utilizado en aplicaciones web y APIs.

---

## Características

- **Conversión directa**: Convierte archivos CSV en archivos JSON manteniendo la estructura de las columnas y filas.
- **Codificación UTF-8**: Asegura compatibilidad con caracteres especiales y evita problemas de codificación.
- **Indentación personalizada**: El archivo JSON generado es fácilmente legible gracias a la indentación especificada.

---

## Requisitos Previos

- **Python 3.6** o superior.
- Tener un archivo CSV listo para convertir. Asegúrate de que el archivo tenga encabezados para las columnas.

---

## Instalación

1. Clona este repositorio o descarga el archivo del script.
2. Verifica que tienes Python instalado ejecutando el siguiente comando en tu terminal:

   ```bash
   python --version
3. Coloca el archivo CSV que deseas convertir en el mismo directorio que el script.

---

## Uso

1. Abre el archivo script.py en tu editor de texto o entorno de desarrollo integrado (IDE).
2. Modifica las variables archivo_csv y archivo_json en el script para especificar los nombres del archivo CSV de entrada y el archivo JSON de salida, respectivamente:

    ```python
csv_a_json('products.csv', 'productos_json.json')
3. Ejecuta el script desde la terminal o tu entorno de desarrollo integrado (IDE):

   ```bash
    python script.py
4. El archivo JSON generado aparecerá en el mismo directorio que el script.

