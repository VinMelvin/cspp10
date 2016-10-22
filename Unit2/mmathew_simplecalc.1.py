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

#Taking It Futher
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
expression = input("Enter expression: ")
term_1 = int(input("Enter the length of the first term in terms of digits: "))
term_2 = int(input("Enter the length of the second term in terms of digits: "))
if expression[term_1] == "+":
    print("The result is " + str(int(expression[0:term_1]) + int(expression[term_1+1:])))
elif expression[term_1] == "-":
    print("The result is " + str(int(expression[0:term_1]) - int(expression[term_1+1:])))
elif expression[term_1] == "*":
    print("The result is " + str(int(expression[0:term_1]) * int(expression[term_1+1:])))
elif expression[term_1] == "/":
    print("The result is " + str(int(expression[0:term_1]) / int(expression[term_1+1:])))
elif expression[term_1] == "%":
    print("The result is " + str(int(expression[0:term_1]) % int(expression[term_1+1:])))
else:
    print ("error")
    



    