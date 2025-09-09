# h) Desenvolva um programa que pergunta ao usuário qual o dia da
# semana (1 a 7) e, com base nessa entrada, exibe o nome do dia
# correspondente.


# dia = int(input("Digite um número de 1 a 7: "))

# if dia == 1:
#     print("Domingo")
# elif dia == 2:
#     print("Segunda-feira")
# elif dia == 3:
#     print("Terça-feira")
# elif dia == 4:
#     print("Quarta-feira")
# elif dia == 5:
#     print("Quinta-feira")
# elif dia == 6:
#     print("Sexta-feira")
# elif dia == 7:
#     print("Sábado")
# else:
#     print("Número inválido! Digite de 1 a 7.")
    
d1 = "Domingo"
d2 = "Segunda"
d3 = "Terça"
d4 = "Quarta"
d5 = "Quinta"
d6 = "Sexta"
d7 = "Sábado"

dia = input("Escolha o dia da semana: \nd1 para Domingo, \nd2 para Segunda, \nd3 para Terça, \nd4 para Quarta, \nd5 para Quinta, \nd6 para Sexta, \nd7 para Sábado: ")

match dia:
    case "d1": 
        print("Hoje é", d1)
    case "d2": 
        print("Hoje é", d2)
    case "d3": 
        print("Hoje é", d3)
    case "d4": 
        print("Hoje é", d4)
    case "d5": 
        print("Hoje é", d5)
    case "d6": 
        print("Hoje é", d6)
    case "d7": 
        print("Hoje é", d7)
    