salario = float(input("Digite o salário do funcionário em 1995: "))
ano = 1995
ano_atual = int(input("Digite o ano atual: "))
aumento = 1.5 / 100  

while ano < ano_atual:
    ano = ano + 1
    salario = salario* 1 + aumento
    aumento = aumento *2

print(f"O salario em {ano} é de R$ {salario:.2f}")