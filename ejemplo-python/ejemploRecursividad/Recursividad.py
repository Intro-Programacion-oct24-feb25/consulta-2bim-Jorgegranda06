def fibonacci(n):
    # Caso base
    if n <= 1:
        return n
    # Caso recursivo
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Ejemplo de uso
numero = 10
print(f"El término {numero} de la secuencia de Fibonacci es: {fibonacci(numero)}")