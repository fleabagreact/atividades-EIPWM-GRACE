nomes = []

for i in range(3):
    nome = input(f"Digite o nome {i + 1}: ")
    nomes.append(nome)

nomes.sort()

print("Nomes em ordem alfabética:")
for nome in nomes:
    print(nome)