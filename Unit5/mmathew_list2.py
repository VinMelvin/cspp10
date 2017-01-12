num = []

while True:
    user_input = input("Enter a number: ")
    if user_input == "exit":
        break 
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
    elif user_input == int(user_input):
        num.insert(1,user_input)
    