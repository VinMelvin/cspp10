num = []

while True:
    user_input = input("Enter a number: ")
    if user_input == 0:
        break 
    elif user_input > 0:
        num.insert(1,user_input)
        print(num)
    elif user_input < 0:
        use = user_input - user_input - user_input
        num.remove(use)
        print(num)
    else:
        print("Thanx")
        


