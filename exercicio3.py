base = int(input("informe a base: "))
expoente = int(input("informe o expoente: "))
contador = 0
potencia = 1

while contador < expoente:
    potencia = potencia * base
    contador = contador + 1 
print(f"Potencia = {potencia}")