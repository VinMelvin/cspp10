operation = input("Enter operation: ")
answer = str(operation)
if answer[1] == "+":
    print("Answer " + str(answer[0]) + str(answer[2]))
elif answer[1] == "-":
    print("Answer " + str(answer[0] - answer[2]))
elif answer[1] == "*":
    print("Answer " + str(answer[0] * answer[2]))
elif answer[1] == "/":
    print("Answer " + str(answer[0] / answer[2]))
elif answer[1] == "%":
    print("Answer " + str(answer[0] % answer[2]))
