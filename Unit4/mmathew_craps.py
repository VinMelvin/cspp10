import random
print("Welcome To Craps\n---------------------------------------")

# function name: bank_account  
#   purpose: The amount of money in the players bank and how much to bet
#   arguments:   

#   returns: 

def bank_account():
    bank = int(100)
    print("You have ${} in your bank".format(bank))
    return bank

# function name: bank_account  
#   purpose: The amount of money in the players bank and how much to bet
#   arguments:   

#   returns:    
def bet_number(bank):
    bet = int(input("Enter a whole number for your bet: "))
    while (bet > bank):
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
#   purpose: 
#   arguments: 
#   returns: 

# input("Press Enter to terminate.")

def house():
    bank = bank_account()
    while bank > 0:
        bet = bet_number(bank)
        dice_number = roll2dice()
        first_roll = first_roll_result(dice_number)
        if first_roll == "win":
            bank = bank + bet
            print("Your balance is {}".format(bank))
        elif first_roll == "lose":
            bank = bank - bet
            print("Your balance is {}".format(bank))
        else:
            #print("You have reached the point number")
            point_num = point_number(dice_number)
            
            if point_num == "point Win":
                bank = int(bank) + bet
                print("Your balance is {}".format(bank))
            elif point_num == "point Lose":
                bank = bank - bet 
                print("Your balance is {}".format(bank))
                
                
          
            
            
            
        
house()
