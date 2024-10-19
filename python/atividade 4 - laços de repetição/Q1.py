# Tabuada de um número inteiro positivo
numero = int(input("Digite um número inteiro positivo: "))
limite = int(input("Digite o valor limite da tabuada: "))

print(f"\nTabuada do {numero} até {limite}:")
for i in range(1, limite + 1):
    print(f"{numero} x {i} = {numero * i}")
