#Uso de un bloque try-except global:

def operacion_compleja():
    try:
        # Código con posibles excepciones
        pass
    except Exception:
        # Manejo de excepciones
        pass

def ejecutar_operacion():
    try:
        operacion_compleja()
    except Exception:
        print("Ocurrió un error al ejecutar la operación.")

# Ejemplo de uso
ejecutar_operacion()

"""En este ejemplo, tenemos una función "operacion_compleja()" que contiene código con posibles excepciones. En la función
"ejecutar_operacion()", llamamos a "operacion_compleja()" dentro de un bloque "try-except" para manejar cualquier excepción
que pueda ocurrir durante la ejecución de la operación."""