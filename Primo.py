x = int(input())
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

# Explicación:
# - `lambda n:` define una función anónima que toma un número `n`.
# - `n > 1`: Un número primo debe ser mayor que 1.
# - `all(n % i != 0 for i in range(2, int(n**0.5) + 1))`:
#     - `range(2, int(n**0.5) + 1)`: 
#         - Solo necesitamos revisar hasta la raíz cuadrada de `n` (`√n`) en vez de hasta `n`.
#         - Esto hace que el código sea más eficiente.
#     - `n % i != 0`: 
#         - Verifica que `n` no sea divisible por `i`.
#         - Si `n` es divisible por algún `i`, entonces **no es primo**.
#     - `all(...)`: 
#         - Evalúa si todas las condiciones dentro de él son `True`.
#         - Si encontramos un solo divisor en el rango, `all()` devolverá `False`, indicando que `n` no es primo.

print(is_prime(x))  


