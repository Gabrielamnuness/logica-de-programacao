# 5. Comparação de Idades
# Peça a idade de duas pessoas e mostre:
# • quem é o mais velho
# • quem é o mais novo
# • se possuem a mesma idade

irmao1 = int(input("Digite a idade do primeiro irmão: "))
irmao2 = int(input("Digite a idade do segundo irmão: "))

if irmao1 > irmao2:
    print(f"O irmão 1 é o mais velho e irmão 2 é o mais novo!")
elif irmao1 == irmao2:
    print(f"O irmão 1 e o irmão 2 tem a mesma idade!")
else:
    print(f"O irmão 2 é mais velho e irmão 1 é o mais novo!")

