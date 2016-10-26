# num = 999
# for x in range(1,num+1):
#     print(x)
# print(num)


num = int(input("Enter a non-negative integer: "))
for x in range(num + 1):
    if x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    # elif x % 3 or 5 == 0:
    #     print("FizzBuzz")
print(x)

    
