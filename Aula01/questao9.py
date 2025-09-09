# 9. Número no Intervalo

# Peça um número inteiro e verifique se ele está entre 10 e 50 (inclusive), utilizando operadores lógi-
# cos (and).

numero = int(input("Digite um número inteiro: "))

resultado = numero >= 10 and numero <= 50
print(resultado)