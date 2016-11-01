import random
num_guess = input("Enter Guess Number 1 - 100 : ")
num = random.randint(1,101)
num_times = 1
while num_guess != num:
    num_times = num_times + 1
    if num_guess < num:
        print("Too low! Try again.")
    elif num_guess > num:
        print("Too High! Try again.")
    elif num_guess == num:
        print("You got It")
    num_guess = int(input("Enter Guess Number 1 - 100 : "))

print("You got It")
print("Number of Tries " + str(num_times))