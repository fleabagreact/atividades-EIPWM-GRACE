# Organizar n números em ordem crescente
n = int(input("Digite a quantidade de números: "))
numeros = []

for i in range(n):
    num = int(input(f"Digite o número {i+1}: "))
    numeros.append(num)

numeros.sort()
print("Números em ordem crescente:", numeros)