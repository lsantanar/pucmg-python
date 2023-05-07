# Crie um código que receba um número digitado pelo usuário.
# Verifique se esse valor é positivo, negativo ou igual a zero. A saída deve ser: "Valor Positivo", "Valor Negativo" ou "Igual a Zero".

print("*********************************")
print("Vamos validar algum número digitado?")
print("*********************************")

numero_digitado = int(input("Digite um número: "))

if numero_digitado > 0:
    print("Valor positivo!")

elif numero_digitado < 0:
    print("Valor negativo!")

elif numero_digitado == 0:
    print("Igual a zero!")
