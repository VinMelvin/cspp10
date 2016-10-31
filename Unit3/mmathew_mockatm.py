bank_account = 10000
print("1. Withdraw \n2. Deposit \n3. Exit")
choice = int(input("Welcome to ATM! Pick from above [1|2|3]: "))
while choice != "3":#student completes while loop
    if choice == "1":#user chooses 'withdraw'
        amount = int(input("How much to withdraw: "))
        if amount > bank_account:
            print("withdraw is too much")
        else:
            print(bank_account == bank_account - amount) #student does this part
    elif choice == "2":
        amount = int(input("How much to deposit: "))
        print(bank_account == bank_account + amount)
    elif choice == "3": #user chooses 'exit'
        print("goodbye")#student does this part too

    print("1. Withdraw \n2. Deposit \n3. Exit")
    choice = input("Pick from above [1|2|3]:")