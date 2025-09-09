# g) Faça um programa que lê um número e, se for positivo, exibe
# "Número positivo"; se for negativo, exibe "Número negativo"; caso
# seja zero, exibe "Zero".

numero = int(input("Digite um número: "))

if numero > 0:
    print("O número é positivo!")
elif numero == 0:
    print("O número é igual a zero!")
else:
    print("O número é negativo!")