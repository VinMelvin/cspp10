    
import random

# function for rolling 2 dice
# name: roll2dice
# arguments: none
# returns: the sum
def roll2dice():
    # generate a random number from 1 to 6
    dice1 = random.randint(1,6)
    # generate another random number from 1 to 6
    dice2 = random.randint(1,6)
    # get the sum of the two rolls
    dice_sum = dice1 + dice2
    # print the sum
    print("Rolled {} and {}, total: {}".format(dice1, dice2, dice_sum))
    # return the sum
    return dice_sum

# function for getting a user's bet
# name: get_bet
# arguments: bank - current player balance
# returns: the bet
def get_bet(bank):
    # ask the player how much they want to bet
    bet = int(input("Enter your bet:"))
    # if player's bet is more than they have
    #   available in bank, then get new bet
    while (bet > bank):
        bet = int(input("Enter a valid bet: "))
    # if player's bet is valid, then return
    #   the bet
    return bet

# function that finds the range given a dice roll
# name: get_range
# arguments: sum of dice
# returns: the range:
#           "over7" if over 7
#           "under7" if under 7
#           "equal7" if equal to 7
def get_range(dice_sum):
    # if the sum is over 7, return "over7"
    if dice_sum > 7:
        return "over7"
    # if the sum is under 7, return "under7"
    elif dice_sum < 7:
        return "under7"
    # if the sum is 7, return "equal7"
    else:
        return "equal7"

# function for getting the user's choice of range
# name: choose_range
# arguments: none
# returns: player's choice of range
#       "over7", "under7", or "equal7"
def choose_range():
    # present user with choices "over7", "under7",
    #   or "equal7"
    print("Choose from the following")
    print("1. over 7 \n2. under 7 \n3. equal to 7")
    # return their choice
    choice = input("Choose from [1|2|3]")
    if choice == "1":
        return "over7"
    elif choice == "2":
        return "under7"
    else:
        return "equal7"

# function for the main game
def overunder7():
    #initialize the player's bank
    bank = 100
    #loop as long as the player has SOME amount of money
    while bank > 0:
        #ask for a bet and save it
        bet = get_bet(bank)
        #ask for the range and save it
        user_range = choose_range()
        #roll 2 dice and save it
        dice = roll2dice()
        #figure out the range of the dice and save it
        round_range = get_range(dice)
        #check to see if the user won or lost
        #update their bank accordingly
        if user_range == round_range: #user won
            print("You win!")
            if user_range == "equal7":
                bank = bank + 4 * bet
            else:
                bank = bank + bet
            
        else: #user lost
            print("You lost!")
            bank = bank - bet
            
        #print new bank value
        print("Your balance is ${}".format(bank))
        
        #ask if they want to do another round
        new_round = input("Do you want to continue? [y|n]").lower()
        if new_round != "y":
            break
    
    print("Game over, you have ${} in your bank".format(bank))
    
    
overunder7()
# import random

# def roll2dice():
#     dice1 = random.randint(1,6)
#     dice2 = random.randint(1,6)
#     dice_sum = dice1 + dice2
#     print ("Rolled 2 dice: {} and {}, {} in total!".format(dice1,dice2,dice_sum))
#     return dice_sum
    
# def first_roll(dice_sum):
#     if dice_sum == 2 or dice_sum == 3 or dice_sum == 12:
#         print ("You lost!")
#         return "lose"
        
#     elif dice_sum == 7 or dice_sum == 11:
#         print ("You win!")
#         return "win"
#     else:
#         print ("{} is now your point number.".format(dice_sum))
#         return dice_sum
    
    
# def p1_bet(user_bank):
#     while True:
#         ask_bet = int(input("How much would you like to bet?: "))
#         if ask_bet <= user_bank:
#             return ask_bet
#         elif ask_bet < 0:
#             while ask_bet < 0:
#                 print ("No negative numbers!")
#                 ask_bet = int(input("How much would you like to bet?: "))
#         elif ask_bet > user_bank:
#             while ask_bet > user_bank:
#                 print ("You don't have that much!")
#                 ask_bet = int(input("How much would you like to bet?: "))
        
        
# def point_number(dice_sum):
#     while True:
#         dice1 = random.randint(1,6)
#         dice2 = random.randint(1,6)
#         dice_sum_check = dice1 + dice2
#         point_number = dice_sum_check
#         print ("Rolled 2 dice: {} and {}, {} in total.".format(dice1,dice2,dice_sum_check))
#         if point_number == dice_sum:
#             print ("You win")
#             return "point win"
#         elif point_number == 7:
#             print ("You lost")
#             return "point lose"


# def craps():
    
#     user_bank = 100
    
    
#     print ("Welcome to Craps!")
#     print ("\_______________/")


#     while user_bank > 0:
#         ask_bet = p1_bet(user_bank)
#         dice_sum = roll2dice()
#         dice_sum_first_roll = first_roll(dice_sum)
#         if dice_sum_first_roll == "win": 
#             user_bank = user_bank + ask_bet
#             print ("Your bank amount is now {}.".format(user_bank))
#             print ("-----------------------------")
#         elif dice_sum_first_roll == "lose": 
#             user_bank = user_bank - ask_bet
#             print ("Your bank amount is now {}.".format(user_bank))
#             print ("-----------------------------")
#         else:
#             point_number_var = point_number(dice_sum)
        

#             if point_number_var == "point win":
#                 user_bank = user_bank + ask_bet
#                 print ("Your bank amount is now {}.".format(user_bank))
#                 print ("-----------------------------")
#             elif point_number_var == "point lose":
#                 user_bank = user_bank - ask_bet
#                 print ("Your bank amount is now {}.".format(user_bank))
#                 print ("-----------------------------")


# craps()
# #print ("get out")