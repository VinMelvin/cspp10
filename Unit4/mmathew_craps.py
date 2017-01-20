import random
print("Welcome To Craps\n---------------------------------------")

# function name: bank_account  
#   purpose: The amount of money in the players bank 
#   arguments: none

#   returns: the amount of money the player has

def bank_account():
    bank = int(100)
    print("You have ${} in your bank".format(bank))
    return bank

# function name: bank_account  
#   purpose: The amount of money in the players bank and how much to bet
#   arguments:bank - the amount of money the player has in his bank

#    returns: 
#         if bank is a whole number : returns bet
#         if not it will say "Enter a valid bet:" and returns bet
def bet_number(bank):
    bet = int(input("Enter a whole number for your bet: "))
    while True:
        if bet <= bank:
            return bet
        # elif bet <= 0:
        #     bet = int(input("Positive numbers only: ")) 
        #     print(bet)
        #     return bet
        else:
            bet = int(input("Enter a valid bet: "))
            return bet




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

# function name: first_roll_result
#   purpose: get the result of the first roll
#   arguments: roll - the sum of the two dice rolled
#   returns: the result
#       if roll is 7,11: return "win"
#       if roll is 2,3,12: return "lose"
#       if otherwise: return "point number"
def first_roll_result(roll):
        if roll == 7 or roll == 11:
            print("win")
            return "win"
        elif roll == 2 or roll == 3 or roll == 12:
            print("lose")
            return "lose"
        else:
            print("You have reached the point number ({})".format(roll))
            return "point number"
            
# function name: bank_account  
#   purpose: Checking if the pointnumber will win or lose the game
#   arguments: point - point number of the game
#   returns: 
        # if "win" : returns "point Win"
        # if "lose": returns "point lose"
def point_number(point):
    while True:
        
        newroll = roll2dice()
      
        if newroll == point:
            print("win")
            return "point Win"
        elif newroll == 7:
            print("lose")
            return "point Lose"
    
    
    
    

# function name: bank_account  
#   purpose: function for the main game
#   arguments: none
#   returns: none

# input("Press Enter to terminate.")

def house():
    bank = bank_account()
    # making a variable for bank
    while bank > 0:
        bet = bet_number(bank)
        # bet is checking if player bet is valid
        dice_number = roll2dice()
        # variable for the dice roll
        first_roll = first_roll_result(dice_number)
        # checking if won, lost or pointnumber
        if first_roll == "win":
            bank = bank + bet
            print("Your balance is {}".format(bank))
            print("----------------------------------------")
            # what happens when first_roll player wins
        elif first_roll == "lose":
            bank = bank - bet
            print("Your balance is {}".format(bank))
            print("----------------------------------------")
            # what happens when first_roll player loses
        else:
            
            point_num = point_number(dice_number)
            # when reach point number
            
            if point_num == "point Win":
                bank = int(bank) + bet
                print("Your balance is {}".format(bank))
                print("----------------------------------------")
                # what happens when pointnum player wins
            elif point_num == "point Lose":
                bank = bank - bet 
                print("Your balance is {}".format(bank))
                print("----------------------------------------")
                # what happens when pointnum player loses
                
                
          
            
            
            
        
house()
print("Thank You For Playing")
# Game Ends