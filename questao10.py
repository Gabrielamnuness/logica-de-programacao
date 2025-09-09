# 10. Votação
# Peça a idade do usuário e informe:
# • Se pode votar (idade ≥ 16)
# • Se pode dirigir (idade ≥ 18)
# Use condições lógicas e exiba todas as permissões.


idade = int(input("Digite sua idade: "))

if idade >= 16:
    print("Pode votar!")
else:
    print("Não pode votar.")

if idade >= 18:
    print("Pode dirigir!")
else:
    print("Não pode dirigir.")