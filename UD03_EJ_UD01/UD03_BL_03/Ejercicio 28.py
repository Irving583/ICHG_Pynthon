"""Un programa que suma independientemente los pares y los
impares de los números comprendidos entre 100 y 200, y luego muestre por pantalla ambas
sumas."""


suma_pares = 0
suma_impares = 0
for num in range(100, 201):
    if num % 2 == 0:
        suma_pares += num
    else:
        suma_impares += num
print(f"Suma de números pares entre 100 y 200: {suma_pares}")
print(f"Suma de números impares entre 100 y 200: {suma_impares}")
