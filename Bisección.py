# Definimos la función de bisección usando lambda y recursión
biseccion = (lambda f:  
                lambda func, a, b, tol:  
                    (a + b) / 2 if abs(b - a) < tol else  
                    f(f)(func, a, (a + b) / 2, tol) if func(a) * func((a + b) / 2) < 0 else  
                    f(f)(func, (a + b) / 2, b, tol)  
            )(lambda f:  
                lambda func, a, b, tol:  
                    (a + b) / 2 if abs(b - a) < tol else  
                    f(f)(func, a, (a + b) / 2, tol) if func(a) * func((a + b) / 2) < 0 else  
                    f(f)(func, (a + b) / 2, b, tol)  
            )

# Pedimos al usuario que ingrese la función en términos de 'x'
print("Ingrese la función en términos de 'x' (ejemplo: x**2 - 4):")
func_str = input("f(x) = ")

# Convertimos la entrada del usuario en una función lambda
f = eval("lambda x: " + func_str)  

# Pedimos el intervalo [a, b] y la tolerancia
a = float(input("Ingrese el límite inferior del intervalo (a): "))
b = float(input("Ingrese el límite superior del intervalo (b): "))
tol = float(input("Ingrese la tolerancia (ejemplo: 0.001): "))

# Verificamos que la función cambie de signo en el intervalo (f(a) * f(b) < 0)
if f(a) * f(b) > 0:
    print("Error: La función no cambia de signo en el intervalo dado. Intente con otro.")
else:
    raiz = biseccion(f, a, b, tol)  # Llamamos a la función de bisección
    print(f"La raíz aproximada es: {raiz}")

