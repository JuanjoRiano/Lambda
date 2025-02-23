x = int(input())
y = int(input())
mcd = (lambda f:  # Definimos una función f que implementa la recursión
            lambda x, y: x if y == 0 else f(f)(y, x % y)  # Caso base y recursión
      )(
      lambda f:  # Pasamos la función a sí misma para permitir recursión
            lambda x, y: x if y == 0 else f(f)(y, x % y)
      )

# Explicación:
# - `lambda f:` Define una función anónima que recibe otra función `f` como argumento.
# - `lambda x, y: x if y == 0 else f(f)(y, x % y)`:
#     - Caso base: Si `y == 0`, el resultado es `x` (ya que MCD(x, 0) = x).
#     - Si `y != 0`, aplica la recursión llamando a `MCD(y, x % y)`.
#     - `f(f)`: Se pasa la función a sí misma para permitir la recursión.
# - `(lambda f: ...)(lambda f: ...)`: Se autoejecuta con la misma estructura para habilitar la recursión.

print(mcd(x, y))

