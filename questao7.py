# 7. Comparação de Valores
# Peça ao usuário dois números e verifique:
# • se o primeiro é maior que o segundo
# • se o primeiro é menor que o segundo
# • se os dois são iguais

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 > n2:
    print(f"O primeiro número, {n1}, é maior que o segundo, {n2}.")
elif n1 < n2:
    print(f"O primeiro número, {n1}, é menor que o segundo, {n2}.")
else:
    print(f"Os dois número são iguais!")
    
