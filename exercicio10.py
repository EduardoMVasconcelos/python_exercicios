contador = 1
n = 1
soma = 0
print("Mercearia")

while contador > 0:
    valor = float(input(f"Produto {n}: R$ "))
    contador = valor
    soma = soma + valor
    n = n + 1 
    
print(f"Total: R$ {soma}")
dinheiro = float(input("Dinheiro: R$ "))
print(f"Troco {dinheiro-soma}")