contador = 1
par = 0
impar = 0

while contador <= 10:
    numero = int(input("Digite um numero inteiro: "))
    contador = contador + 1
    
    if numero % 2 == 0:
        numero = par
        par = par + 1
        
    elif numero % 2 != 0:
        numero = impar 
        impar = impar + 1
        
print(f"A quantidade de numeros pares é igual a {par}")
print(f"A quantidade de numeros impares é igual a {impar}")