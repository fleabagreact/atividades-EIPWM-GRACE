# Programa com funções para somatória, números pares e ímpares

def somatoria(listaNum):
    return sum(listaNum)

def pares(listaNum):
    return len([num for num in listaNum if num % 2 == 0])

def impares(listaNum):
    return len([num for num in listaNum if num % 2 != 0])

n = int(input("Digite a quantidade de números: "))
listaNum = []

for i in range(n):
    num = int(input(f"Digite o número {i+1}: "))
    listaNum.append(num)

print(f"Soma dos números: {somatoria(listaNum)}")
print(f"Quantidade de números pares: {pares(listaNum)}")
print(f"Quantidade de números ímpares: {impares(listaNum)}")
