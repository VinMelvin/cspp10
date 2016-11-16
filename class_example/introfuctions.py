# import random

# def roll_doubles(num_sides):
#     dice1 = random.randint(1,num_sides)
#     dice2 = random.randint(1,num_sides)
#     print("You rolled a {} and {}".format(dice1,dice2))
#     if dice1 == dice2:
#         print("DOUBLES")
    
# #function call
# for x in range(4,10):
#     roll_doubles(x) 
    
#write function below
def compare3(a,b,c):
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    elif c > a and c > b:
        print(c)

#dont change tests below
compare3(1,2,3)
compare3(7,3,10)
compare3(-6,-22,-6)
    
    
    