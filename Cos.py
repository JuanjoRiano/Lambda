from math import factorial, radians

# Función lambda recursiva para calcular cos(x) con n términos de Taylor
cos_taylor = (lambda f: 
                lambda x, n: 
                    1 if n == 0 else f(f)(x, n - 1) + ((-1)**n * x**(2*n) / factorial(2*n))
            )(lambda f: 
                lambda x, n: 
                    1 if n == 0 else f(f)(x, n - 1) + ((-1)**n * x**(2*n) / factorial(2*n))
            )

# Solicitar entrada del usuario
x_grados = float(input("Ingrese el valor de x en grados: "))  # Convierte a float
x = radians(x_grados)  # Convierte grados a radianes
n = int(input("Ingrese el número de términos de la serie de Taylor: "))  # Cantidad de términos

# Calcular cos(x) usando el polinomio de Taylor
resultado = cos_taylor(x, n)

# Mostrar el resultado
print(f"cos({x_grados}°) ≈ {resultado} (usando {n} términos)")

