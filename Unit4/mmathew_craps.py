import random
print("Welcome To Craps\n---------------------------------------")

# function name: bank_account  
#   purpose: The amount of money in the players bank and how much to bet
#   arguments:   

#   returns: 
def bank_account():
    bank = int(100)
    print("You have ${} in your bank".format(bank))
    bet = int(input("Enter a whole number for your bet: "))
#     if bet >= 100:
#         print("You don't have that much money!!!")
#     elif bet < 0:
#         print("Bet a postive number")
bank_account()



# function name: roll2dice
#   purpose: generating two random dice rolls and 
#   prints it out, and returns the sum
#   arguments: none
#   returns: the sum of the two dice
def roll2dice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_sum = dice1 + dice2    
    print("Rolled 2 dice: {} {}, Total of {}".format(dice1,dice2,dice_sum))
    return dice_sum
roll2dice()
# function name: first_roll_result
#   purpose: get the result of the first roll
#   arguments: roll - the sum of the two dice rolled
#   returns: the result
#       if roll is 7,11: return "win"
#       if roll is 2,3,12: return "lose"
#       if otherwise: return "point number"
def first_roll_result():
    roll = roll2dice
    if roll == 7 or roll == 11:
        return "win"
    elif roll == 2 or roll == 3 or roll == 12:
        return "lose"
    else:
        return "point number"
first_roll_result()
# function name: bank_account  
#   purpose: 
#   arguments: 
#   returns: 

input("Press l to terminate.")
