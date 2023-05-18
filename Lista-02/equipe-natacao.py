print("*********************************")
print("Prova dos 25 metros, estilo livre")
print("*********************************")

lista_nomes = []
lista_tempos = []
qtd_atletas = 0

for i in range (7):
    nome = input("Qual o seu nome? ")
    tempo = float(input("Digite o seu tempo de prova (em segundos): "))

    lista_nomes.append(nome)
    lista_tempos.append(tempo)

# ---- nome do nadador com o melhor tempo ----
maior_tempo = max(lista_tempos)
print("Maior tempo: ", lista_nomes[lista_tempos.index(maior_tempo)])

# ---- nome do nadador com o pior desempenho ----
menor_tempo = min(lista_tempos)
print("Menor tempo: ", lista_nomes[lista_tempos.index(menor_tempo)])

# ---- tempo médio dos nadadores ----
tempo_medio = sum(lista_tempos) / len(lista_tempos)
print("O tempo médio dos nadadores foi de: ", tempo_medio)

# ---- quantidade de atletas com o tempo entre 12s e 15s ----
for i in lista_tempos:
    if lista_tempos <= 12 or lista_tempos <= 15:
        qtd_atletas += 1
print("Quantidaded de atletas com tempo entre 12 e 15 segundos: ", qtd_atletas)