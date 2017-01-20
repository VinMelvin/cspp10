num = []

while True:
    user_input = input("Enter a number: ")
    if user_input == "sum":
        # int(user_input)
        print (sum(num))
    elif user_input == "clear":
        num = []
        print (num)
    elif user_input == "print":
        print(num)
    elif user_input == "length":
        print(len(num))
    elif user_input == "exit":
        break
    else:
        num.append(int(user_input))
        print (num)
    
    