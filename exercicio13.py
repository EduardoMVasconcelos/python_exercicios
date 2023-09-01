tabuada = int(input("Montar a tabuada de: "))
numero1 = int(input("Começar por: "))
numero2 = int(input("Terminar em: "))

contador = 1

print(f"Vou montar a tabuada do {tabuada} começando pelo {numero1} e terminando no {numero2}.")
while numero1 <= numero2:
    print(f"{tabuada} x {numero1} = {tabuada * numero1}")
    numero1 = numero1 + 1
    contador = contador + 1