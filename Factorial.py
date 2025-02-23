from functools import reduce

x = int(input())

factorial_itera = lambda n: 1 if n == 0 else reduce(lambda x, y: x * y, range(1, n + 1))
# Explicación:
# - Si n == 0, devuelve 1 (porque 0! = 1).
# - Si n > 0, usa reduce() para calcular el producto de todos los números de 1 a n.
# - reduce(lambda x, y: x * y, range(1, n+1)) multiplica todos los números de 1 a n.
#   Ejemplo con n = 5:
#   reduce(lambda x, y: x * y, [1, 2, 3, 4, 5]) se resuelve como:
#   ((((1 * 2) * 3) * 4) * 5) = 120

print(factorial_itera(x))  # Salida: 120


#(usando el combinador Y)
factorial_recur = (lambda f:  # f es una función anónima que permite la recursión indirecta
                lambda n: 1 if n == 0 else n * f(f)(n - 1)  # Caso base y llamada recursiva
            )(
            lambda f:  # Se pasa a sí misma para permitir la recursión
                lambda n: 1 if n == 0 else n * f(f)(n - 1)
            )

# Explicación:
# - Se usa un truco de recursión sin nombres explícitos, ya que lambda no permite referencias directas a sí misma.
# - La primera lambda recibe f, que es otra lambda.
# - f se pasa a sí misma (f(f)) para permitir que la función lambda pueda llamarse recursivamente.
# - Si n == 0, devuelve 1.
# - Si n > 0, multiplica n por el resultado de llamar a la función recursivamente con (n - 1).
# - Es un equivalente funcional a:
#   def factorial(n):
#       return 1 if n == 0 else n * factorial(n - 1)

print(factorial_recur(x))  # Salida: 120

