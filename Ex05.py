''' . Classificação etária e preço do ingresso
Em um cinema, o preço do ingresso varia de acordo com a faixa etária do cliente.

Crie um programa que leia a idade de uma pessoa e exiba sua classificação e o preço do ingresso correspondente:

Faixa etária	Classificação	Preço do ingresso
0 a 12 anos	     Criança	      R$ 10,00
13 a 17 anos	Adolescente	      R$ 15,00
18 a 59 anos	  Adulto	      R$ 20,00
60 anos ou mais	  Idoso	          R$ 12,00 '''


age = int(input("Add your age:\t"))

cat1 = age > 0 and age <= 12
cat2 = age > 12 and age <= 18
cat3 = age > 18 and age <= 59

if age < 0 or age > 140:
  print("Invalid age")

elif cat1 == True:
    print("Childish")
    print("Ticket price: R$10,00 ")

elif cat2 == True:
   print("Adolescent")
   print("Ticket price: R$15,00 ")

elif cat3 == True:
   print("Adult")
   print("Ticket price: R$20,00 ")

else:
   print("Elderly")
   print("Ticket price: R$12 ")


    

  

  

