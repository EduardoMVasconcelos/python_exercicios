quantidade = int(input("Digite a quantidade de pessoas na turma: "))
contador = 1
soma = 0

while contador <= quantidade:
    idade = int(input(f"Digite a idade do {contador}º aluno: "))
    soma = soma + idade
    contador = contador + 1

media = soma/quantidade

if media <= 25:
    print("Jovem")

elif media > 25 and media <= 60:
    print("Adulta") 

elif media > 60:
    print("Idosa")
