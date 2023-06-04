#MULTIPLES EXCEPCIONES EN UNA FUNCIÓN:
def dividir_numeros(numero1, numero2):
    try:
        resultado = numero1 / numero2
        return resultado
    except ZeroDivisionError:
        print("Error: No es posible dividir entre cero.")
    except TypeError:
        print("Error: Los operandos deben ser números.")

# Ejemplos de uso
print(dividir_numeros(10, 2))      # Resultado: 5.0
print(dividir_numeros(5, 0))       # Resultado: Error: No es posible dividir entre cero.
print(dividir_numeros("10", 2))    # Resultado: Error: Los operandos deben ser números.

"""En este ejemplo, capturamos dos tipos diferentes de excepciones. Si se produce una ZeroDivisionError, mostramos un
mensaje de error específico. Si se produce una TypeError, significa que se están pasando operandos no numéricos a la
función de división, y también mostramos un mensaje de error adecuado."""