#Replicador de input (um número a será impresso a vezes)

a = int(input("digite um número\t"))
for c in range(0, a-1): 

 print(a)

#Somatório de inputs

s = 0
for c in range(0, 4):
    n = int(input("digite um número:"))
    s = s+ n
print(s)

#Contador (o ultimo número dentro de range é ignorado seu antecessor é contado)

for c in range(0, 3):
    print(c)
print("fim")

#Contador com operadores + , - , * 

for c in range(0,3 *3):
    print(c)
print("Hello")

#Contador pulando números (no caso de 2 em 2)

for c in range(0,7, 2):
    print(c)
print("End")

#Algoritimo de (i) até (b) de (x) em (x) ex: i = 20 / b= 200 / x = 10

i = int(input("digite um número:\t"))
b = int(input("digite outro:\t"))
x = int(input("digite mais um: \t"))

for c in range(i, b+1, x):
 print(c)




