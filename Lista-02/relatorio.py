razao_social = []
valor_total = []

while True:
    rsocial = input("Razão social: ")
    total = float(input("Valor total da compra: "))

    razao_social.append(rsocial)
    valor_total.append(total)

    if rsocial == "sair" or total == "0":
        break
print("---- Cadastro encerrado! ----")
print("")
valor_total.sort(reverse=True)
print("Array de compras:", valor_total)
print("")

chave_id = list(zip(razao_social, valor_total))

for razao_social, valor_total in chave_id:
    print("Razão social: ", razao_social, "Valor total: ", valor_total)