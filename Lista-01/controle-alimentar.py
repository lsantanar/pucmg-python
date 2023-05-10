print("*********************************")
print("Tabelinha do Emagrecimento")
print("*********************************")

qtd_kg = float(input("Quantos KG quer perder? "))
qtd_meses = int(input("Em quantos meses? "))
print("   ")
print("...")
print("   ")

print("Que legal!!! Você deseja perder", str(qtd_kg), "kg em", str(qtd_meses), "meses. Eles serão divididos dessa forma:")

kg_mes = qtd_kg / qtd_meses

for i in range (qtd_meses):
    print(f"No {i+1} mês você irá perder: {kg_mes:.1f}kg")


# O código abaixo está fora do contexto da atividade...
# Sendo apenas o complemento de uma ideia da atividade anterior. 

print("   ")
lista_alimentar = input("Você gostaria de uma lista de bons alimentos? ")

verduras = ["Alface", "Tomate", "Pimentão"]
legumes = ["Beterraba", "Quiabo", "Moranga"]
fast_food = ["Hambúrguer", "Pizza", "Cachorro Quente"]

if lista_alimentar == "sim":
    print("É muito importante comer ", verduras[1], "e legumes como:", legumes, ".")