# Crie um código que pergunte ao usuário seu nome e sua idade.
# Verifique se a idade é maior ou menor que 18.
# Exiba da seguinte forma: Fulano é maior de 18 e tem XX anos
# ou Fulano não é maior de 18 e tem XX anos.

print("*********************************")
print("Consulta para permissão de entrada.")
print("*********************************")

nome = input("Qual o seu nome? ")
idade = int(input("Digite a sua idade: "))

if idade > 18:
    print(nome + " é maior de 18 e tem " + str(idade) + " anos.")
else:
    print(nome + " é menor de idade e tem " + str(idade) + " anos.")
