"""Manejo genérico de excepciones:"""
def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
        return contenido
    except Exception as e:
        print(f"Error: No se pudo leer el archivo ({e}).")

# Ejemplo de uso
print(leer_archivo("archivo.txt"))

"""En este ejemplo, intentamos leer el contenido de un archivo especificado por su nombre. Si ocurre algún tipo de
excepción durante la lectura del archivo, capturamos la excepción genérica "Exception" y mostramos un mensaje de error.
Utilizamos "as e" para capturar la instancia de la excepción y obtener información adicional sobre el error."""