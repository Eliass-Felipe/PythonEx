'''Exercício Prático: Entrada no Cinema (Filme +16)

Escreva um programa que peça a idade do cliente e se ele possui o ingresso (Sim/Não).
1. Validação da Entrada (Mensagem de Erro):
	• Se a idade for menor que 0 ou maior que 120, mostre a mensagem: "Erro: Idade inválida!"
2. Análise de Entrada no Cinema (Se a idade for válida):
	• Se a idade for maior ou igual a 16:
		• Se o ingresso for "Sim": mostre "Acesso liberado! Bom filme."
		• Caso contrário (Não): mostre "Acesso negado: Você precisa comprar um ingresso."
	• Se a idade for menor que 16, mostre: "Acesso negado: Filme não recomendado para a sua idade."
'''


age = int(input("Enter your age:\t"))

if age < 0 or age > 140:
    print("Invalid age")

elif age >= 16:
    ticket = str(input("Do you have a ticket?(yes/no)\t"))

    if ticket == "yes" and "Yes" and "YES":
        print("Access granted")

    else:
        print("You need to buy the ticket")

else:
    print("You are too young for this movie")  








