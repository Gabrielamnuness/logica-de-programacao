# 6. Média Aritmética
# Leia três notas de um aluno, calcule a média e exiba se ele está aprovado (média ≥ 7) ou reprovado.

n1 = float(input("Digite a primeira nota do aluno: "))
n2 = float(input("Digite a segunda nota do aluno: "))
n3 = float(input("Digite a terceira nota do aluno: "))

media = (n1 + n2 + n3)/3

if media >= 7.0:
    print(f"A média do aluno é {media}, aluno está Aprovado!")
else:
    print(f"A média do aluno é {media}, aluno está Reprovado!")
