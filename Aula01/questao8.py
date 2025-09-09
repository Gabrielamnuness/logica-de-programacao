# 8. Operadores Lógicos – Aprovação
# Um aluno será aprovado se:
# • a média for maior ou igual a 7 e
# • a frequência for maior ou igual a 75%.
# Leia a média e a frequência e informe se ele foi aprovado ou reprovado.

n1 = float(input("Digite a primeira nota do aluno: "))
n2 = float(input("Digite a segunda nota do aluno: "))
n3 = float(input("Digite a terceira nota do aluno: "))
quantidade_de_aulas = int(input("Digite a quantidade total de aulas do curso: "))
quantidade_de_faltas = int(input("Digite a quantidade de faltas: "))

media = (n1 + n2 + n3)/3

frequencia = 100 - ((quantidade_de_faltas / quantidade_de_aulas) * 100)

if media >= 7.0 and frequencia > 75:
    print(f"Aluno obteve a {media} e {frequencia}% de frequencia, aluno está Aprovado!")
else:
    print(f"Aluno obteve a {media} e {frequencia}% de frequência, o aluno está Reprovado!")
    
