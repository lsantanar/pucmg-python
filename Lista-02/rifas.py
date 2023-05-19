# Uma turma de formandos está vendendo rifas para angariar recursos financeiros para sua cerimônia de formatura.
# Construa um programa para cadastrar os nomes das pessoas que compraram a rifa.
# Ao fim, o programa deve sortear o ganhador do prêmio e imprimir o seu nome
import random

print("*********************************")
print("Rifa de formatura")
print("*********************************")

lista_compradores = []

print("Para sair da tela de cadastro digite >>> sair <<<")
print("")

while True:
    nome = input("Nome do comprador: ")
    lista_compradores.append(nome)

    if nome == "sair":
        break
    
print("")
print("Nomes cadastrados! Vamos pro sorteio???")

ganhador_premio = random.choice(lista_compradores)

print("O ganhador foi: ", ganhador_premio)