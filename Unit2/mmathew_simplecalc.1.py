# operation = input("Enter operation: ")
# operation_1 = int(operation[0])
# operation_2 = int(operation[2])
# if operation[1] == "+":
#     print("The result is " + str(operation_1 + operation_2))
# elif operation[1] == "-":
#     print("The result is " + str(operation_1 - operation_2))
# elif operation[1] == "*":
#     print("The result is " + str(operation_1 * operation_2))
# elif operation[1] == "/":
#     print("The result is " + str(operation_1 / operation_2))
# elif operation[1] == "%":
#     print("The result is " + str(operation_1 % operation_2))
# else:
#     print ("error")

operation = input("Enter operation: ")
operation_1 = input("Enter the length of the first term in terms of digits: ")
operation_2 = input("Enter the length of the second term in terms of digits: ")
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


operation[0:operation_1] + operation[
    