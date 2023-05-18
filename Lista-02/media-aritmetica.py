print("*********************************")
print("Número de alunos")
print("*********************************")

lista_alunos = []

while True:
    idade_alunos = int(input("Digite a idade do aluno: "))
    lista_alunos.append(idade_alunos)

    if idade_alunos <= 0:
        print("")
        print("Você digitou uma idade inválida!")
        print("")
        break

print("Idades armazenadas: ", lista_alunos)

soma = sum(lista_alunos)
media = soma / len(lista_alunos)

print("Média aritmética: ", media)
