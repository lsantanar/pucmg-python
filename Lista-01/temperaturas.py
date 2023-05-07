print("*********************************")
print("Registro de Temperaturas")
print("*********************************")

temperaturas = [-3.55, -10.55, 10.12, 11.44, 22.22]
temperaturas_negativas = [-3.55, -10.55]
temperaturas_positivas = [10.12, 11.44, 22.22]

# A menor temperaturas das informadas:
menor_temperatura = min(temperaturas)
print("A menor temperatura é: ", menor_temperatura)

# A média das temperaturas que forem > que 0 e < que 20:
media = sum(temperaturas) / len(temperaturas)

for item in temperaturas:
    if media > 0:
        print("A média da temperatura acima de 0 é : ", str(media))


   
