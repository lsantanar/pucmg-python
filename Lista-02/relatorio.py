razao_social = []
valor_total = []

while True:
    rsocial = input("Razão social: ")
    total = float(input("Valor total da compra: "))

    razao_social.append(rsocial)
    valor_total.append(total)

    if rsocial == "sair" or total == "0":
        break
print("")
print("Cadastro encerrado!")
# Exibe maior comprador
# maior_comprador = max(valor_total)
# print("Lista de compras: ", razao_social[valor_total.index(maior_comprador)])

print("")
valor_total.sort(reverse=True)
print("Total da compra: ",valor_total)

# print("")
# razao_social.sort(reverse=False)
# print("Total da compra: ",razao_social.index(valor_total))


