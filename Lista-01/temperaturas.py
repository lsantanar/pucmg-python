print("*********************************")
print("Registro de Temperaturas")
print("*********************************")

temperaturas = [-3.55, -10.55, 10.12, 11.44, 22.22]
temp_negativas = 0
temp_positivas = 0

# A menor temperaturas das informadas:
menor_temperatura = min(temperaturas)
print("        ")
print("Menor temperatura registrada: ", menor_temperatura)
print("        ")

# A média das temperaturas que forem > que 0 e < que 20:
media = sum(temperaturas) / len(temperaturas)

while media > 0:
    print("Média da temperatura >>>> 0: ", str(media))
    if media < 20:
        print("Média da temperatura <<<< 20: ", str(media))
    break
print("        ")

# A quantidade de números negativos:
for item in temperaturas:
    if item < 0:
        temp_negativas += 1
print("Números negativos: ", temp_negativas)

# A quantidade de números positivoss:
for item in temperaturas:
    if item > 0:
        temp_positivas += 1
print("Números positivos: ", temp_positivas)