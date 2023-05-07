print("*********************************")
print("Bem vindo aos meses do ano!")
print("*********************************")

mes_atual = int(input("Qual o número do mês? "))
soma = 0; meses = 0

# A variável meses está vazia pois é o dado que será recebido do usuário.
# Em seguida ela é somada com a variável "soma", responsável por armazenar os números anteriores do mês definido.
while meses < mes_atual:
    soma += meses
    meses += 1

    # A soma dos valores menores que o mês atual é igual a X.
    soma += meses
    print("A soma dos meses menores é: {}" .format(soma))

    # O próximo mês é X.
    proximo_mes = mes_atual + 1
    print("O próxima mês será: {}" .format(proximo_mes))

    # O mês atual é X.
    par_impar = mes_atual % 2 == 0
    print("O mês atual é: {}.".format("par" if par_impar else "ímpar"))
    break