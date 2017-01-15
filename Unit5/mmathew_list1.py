num = []

while True:
    user_input = int(input("Enter a number: "))
    if user_input == 0:
        break 
    elif user_input > 0:
        num.append(user_input)
    elif user_input <= -1:
        num.remove(user_input/-2)