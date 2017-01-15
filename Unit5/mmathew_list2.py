num = []

while True:
    user_input = input("Enter a number: ")
    if user_input == "exit":
        break 
    elif user_input == user_input:
        num.append(user_input)
    elif user_input == "sum":
        for x in range(len(num)):
            num = num[x]
            num[x] == num[x] + num
            print(num)
    elif user_input == "clear":
        num = []
    elif user_input == "print":
        print(num)
    elif user_input == "length":
        print(len(num))
    
    