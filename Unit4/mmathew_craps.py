import random
print("Welcome To Craps\n---------------------------------------")

# function name: bank_account  
#   purpose: The amount of money in the players bank and how much to bet
#   arguments: 
#   returns: 
# def bank_account():
#     bank = int(100)
#     print("You have ${} in your bank".format(bank))
#     bet = input("Enter a whole number for your bet: ")
#     bet = int(bet) 
    
    
# bank_account()


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
#OPTION 1
# function name: first_roll_result
#   purpose: get the result of the first roll
#   arguments: roll - the sum of the two dice rolled
#   returns: the result
#       if roll is 7,11: return "win"
#       if roll is 2,3,12: return "lose"
#       if otherwise: return "point"
#def first_roll_result():
    




#OPTION 2
# function name: roll_result
#   purpose: get the result of the roll
#   arguments: 
#       roll - the sum of the two dice rolled
#       is_first_roll - true/false depending on which roll it is
#   returns: the result
#       if player wins: return "win"
#       if player lost: return "lose" 