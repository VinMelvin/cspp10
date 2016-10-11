operation = input("Enter operation: ")
operation_1 = int(operation[0])
operation_2 = int(operation[2])
if operation[1] == "+":
    print("The result is " + str(operation_1 + operation_2))
elif operation[1] == "-":
    print("The result is " + str(operation_1 - operation_2))
elif operation[1] == "*":
    print("The result is " + str(operation_1 * operation_2))
elif operation[1] == "/":
    print("The result is " + str(operation_1 / operation_2))
elif operation[1] == "%":
    print("The result is " + str(operation_1 % operation_2))
else:
    print ("error")
