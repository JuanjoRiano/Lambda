# Lambda Para Matemáticas

Este repositorio contiene cinco programas en Python que implementan distintos algoritmos matemáticos utilizando funciones lambda y recursión.

## 1. Euclides.py
Este programa calcula el **Máximo Común Divisor (MCD)** de dos números enteros utilizando el **algoritmo de Euclides**.

### Funcionamiento:
1. Solicita al usuario dos números enteros como entrada:
   ```python
   x = int(input())  # Se solicita el primer número entero.
   y = int(input())  # Se solicita el segundo número entero.
   ```
2. Define una función lambda recursiva para calcular el MCD:
   ```python
   mcd = (lambda f: lambda x, y: x if y == 0 else f(f)(y, x % y))(
       lambda f: lambda x, y: x if y == 0 else f(f)(y, x % y))
   ```
   - Si `y == 0`, la función devuelve `x`, ya que el MCD de cualquier número y `0` es el mismo número.
   - Si `y != 0`, se llama recursivamente a `MCD(y, x % y)`, aplicando la definición del algoritmo de Euclides.
3. Imprime el MCD calculado:
   ```python
   print(mcd(x, y))  # Se imprime el resultado final.
   ```

## 2. Factorial.py
Este programa calcula el **factorial de un número** usando dos enfoques: **iterativo** con `reduce()` y **recursivo** con combinadores Y.

### Funcionamiento:
1. Solicita al usuario un número entero:
   ```python
   x = int(input())  # Se solicita un número entero al usuario.
   ```
2. **Cálculo iterativo:**
   ```python
   from functools import reduce  # Importamos reduce para realizar la multiplicación acumulativa.
   factorial_itera = lambda n: 1 if n == 0 else reduce(lambda x, y: x * y, range(1, n + 1))
   ```
   - Si `n == 0`, devuelve `1` (caso base del factorial).
   - Si `n > 0`, `reduce()` multiplica todos los valores de `1` a `n`.
3. **Cálculo recursivo:**
   ```python
   factorial_recur = (lambda f: lambda n: 1 if n == 0 else n * f(f)(n - 1))(
       lambda f: lambda n: 1 if n == 0 else n * f(f)(n - 1))
   ```
   - Si `n == 0`, devuelve `1`.
   - Si `n > 0`, aplica la definición clásica del factorial `n! = n * (n-1)!`.

## 3. Primo.py
Este programa determina si un número es **primo**.

### Funcionamiento:
1. Solicita un número entero como entrada:
   ```python
   x = int(input())  # Se solicita un número entero.
   ```
2. Define una función lambda para verificar la primalidad:
   ```python
   is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
   ```
   - Comprueba que `n > 1` (los primos son mayores que 1).
   - Usa `all()` para verificar que `n` no sea divisible por ningún número entre `2` y `√n`.

## 4. Bisección.py
Este programa implementa el **método de bisección** para encontrar la raíz de una función dentro de un intervalo.

### Funcionamiento:
1. Solicita al usuario la función, los límites y la tolerancia:
   ```python
   func_str = input("f(x) = ")  # Se pide la función en forma de string.
   f = eval("lambda x: " + func_str)  # Se convierte el string en una función lambda.
   ```
2. Define la función lambda recursiva para la bisección:
   ```python
   biseccion = (lambda f: lambda func, a, b, tol: (a + b) / 2 if abs(b - a) < tol else 
       f(f)(func, a, (a + b) / 2, tol) if func(a) * func((a + b) / 2) < 0 else 
       f(f)(func, (a + b) / 2, b, tol))(
       lambda f: lambda func, a, b, tol: (a + b) / 2 if abs(b - a) < tol else 
       f(f)(func, a, (a + b) / 2, tol) if func(a) * func((a + b) / 2) < 0 else 
       f(f)(func, (a + b) / 2, b, tol))
   ```
   - Si la diferencia entre `b` y `a` es menor que `tol`, devuelve el valor medio.
   - Si `f(a) * f((a + b) / 2) < 0`, significa que la raíz está en el intervalo izquierdo.
   - En caso contrario, busca en el intervalo derecho.

## 5. Cos.py
Este programa calcula el **coseno de un ángulo** usando la **serie de Taylor**.

### Funcionamiento:
1. Solicita el ángulo en grados y el número de términos:
   ```python
   from math import factorial, radians
   x_grados = float(input("Ingrese el valor de x en grados: "))
   x = radians(x_grados)  # Se convierte el ángulo a radianes.
   n = int(input("Ingrese el número de términos: "))  # Se pide la cantidad de términos.
   ```
2. Define la función lambda recursiva para la serie de Taylor:
   ```python
   cos_taylor = (lambda f: lambda x, n: 1 if n == 0 else f(f)(x, n - 1) + ((-1)**n * x**(2*n) / factorial(2*n)))
   ```
   - Si `n == 0`, devuelve `1`, el primer término de la serie.
   - Si `n > 0`, suma el término correspondiente de Taylor `(-1)^n * x^(2n) / (2n)!`.
3. Imprime el resultado:
   ```python
   print(f"cos({x_grados}°) ≈ {cos_taylor(x, n)} (usando {n} términos)")
   ```

