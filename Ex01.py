user = str(input("Enter a username:\t"))
password = int(input("Enter a password:\t"))

if (user== "Elias" and password == 1234) or (user == "Hello" and password == 5678):

    adm = str(input("Want to access as administrator?\t(sim/nao)"))

    if adm == 'sim' or adm == "Sim" or adm== "SIM":
        print("Total access")

    else: 
        print("Restrict access")

        if user == "Hello" and password == 5678:
            print("External acess")

else : 
    print("Invalid username or password")

  