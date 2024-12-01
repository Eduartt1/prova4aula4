num1 = int(input("Digite um número: ")) 
num2 = int(input("Digite um número: "))

inicio = num1
final = num2
soma_pares = 0
numeros_pares = []

for numero in range(num1, num2):
    if numero % 2 == 0:
        soma_pares += numero
        numeros_pares.append(numero)

else:
    if soma_pares == 0:
        print(f"Entre {num1} e {num2}, não há números pares.")
    else:
        print(f"Os números pares entre {num1} e {num2} é {numeros_pares} e a soma deles é {soma_pares}.")
