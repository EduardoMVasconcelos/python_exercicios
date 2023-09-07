n = int(input("Digite a quantidade de valores: "))
contador = 1 
soma = 0

while contador <= n:
    numeros = int(input(f"Digite o {contador}º numero: "))
    soma = soma + numeros
    contador = contador + 1
    
media = soma/n
print(f"A média é igual a: {media}")