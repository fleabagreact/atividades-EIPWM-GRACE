nome = input("Digite o nome: ")

n = int(input("Digite o número de letras a serem exibidas: "))

if len(nome) < n:
    print("Erro: O nome possui menos letras do que o valor de n.")
else:
    print("As primeiras", n, "letras do nome são:", nome[:n])