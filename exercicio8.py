n = 1
contador = 1 
soma = 0

while n > 0:
    numeros = int(input(f"Informe o {contador}º numero: "))
    n = numeros
    contador = contador + 1
    soma = soma + numeros
    
print(f"A soma dos numeros é de: {soma}")