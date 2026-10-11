accn = int(input("Enter the account number:\t"))
password = int(input("Enter the account password:\t"))

if accn == 1010 and password == 7777 :

    saque = str(input("Wishes to make a withdraw?\t(yes/no)"))

    if saque == "yes" or saque == "Yes":
        print("avaliable for withdraw")
    else:
        print("consultation only")

elif accn == 2020 and password == 8888:
        print("exclusive access for deposits")

else: 
    print("Invalid account or password")



