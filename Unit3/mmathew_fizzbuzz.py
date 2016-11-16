num = int(input("Enter a non-negative integer: "))
num = num + 1
for divisible in range(num):
    if divisible % 3 == 0 and  % 5 == 0:
        print("FizzBuzz")
    elif divisible % 5 == 0:
        print("Buzz")
    elif divisible % 3 == 0:
        print("Fizz")
    else:
        print(divisible)

