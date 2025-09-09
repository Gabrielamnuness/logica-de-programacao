# d) Desenvolva um programa que pergunta se o usuário deseja uma
# bebida quente ou fria. Se escolher quente, exibe "Café"; se escolher
# frio, exibe "Refrigerante".

quente = "Café"
frio = "Refrigerante"

print("Seja bem vindo (a)!")
print("Escolha sua bebida")

escolha_bebida = input("Digite quente para Café ou frio para Refrigerante: ")

if escolha_bebida == "quente":
    print("Aqui está seu Café!")
else:
    print("Aqui está seu Refrigerante!")

# escolha_bebida = input("Escolha: \nquente para Café \nou \nfrio para Refrigerante: ")

# match escolha_bebida:
#     case "quente":
#         print("Aqui está seu Café!")
#     case "frio":
#         print("Aqui está seu Refrigerante!")


# print("Escolha uma opção:")
# print("1 - Bebida quente")
# print("2 - Bebida fria")

# opcao = input("Digite o número da sua escolha: ")

# if opcao == "1":
#     print("Café")
# elif opcao == "2":
#     print("Refrigerante")
# else:
#     print("Opção inválida! Escolha 1 ou 2.")
    
# encontrei três formas com match e com if e else.