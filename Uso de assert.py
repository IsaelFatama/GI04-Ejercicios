#Uso de la cláusula "assert" para verificar condiciones:


def calcular_descuento(precio, descuento):
    try:
        assert descuento > 0, "El descuento debe ser mayor a cero."
        precio_descuento = precio - (precio * descuento)
        return precio_descuento
    except AssertionError as e:
        print(f"Error: {e}")

# Ejemplo de uso
print(calcular_descuento(100, 0.2))      # Resultado: 80.0
print(calcular_descuento(200, -0.1))     # Resultado: Error: El descuento debe ser mayor a cero.

"""En este ejemplo, utilizamos la cláusula "assert" para verificar una condición dentro del bloque "try". Si la condición es
falsa, se produce una excepción "AssertionError" y se ejecuta el bloque "except". Podemos personalizar el mensaje de error
que se muestra utilizando la sintaxis "assert condición, mensaje"."""