# f) Escreva um programa que solicita a idade de uma pessoa e, se for
# menor que 12, exibe "Criança"; se estiver entre 12 e 18 (inclusive),
# exibe "Adolescente"; caso contrário, exibe "Adulto".


idade = int(input("Digite a sua idade: "))

if idade < 12:
    print("Você é Criança!")
elif 12 <= idade <= 18:
    print("Você é Adolescente!")
else:
    print("Você é Adulto!")