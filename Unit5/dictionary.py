from pprint import pprint
diction = {
    
    
    
}

def add():
    user_input = input("What key do you want to add? ")
    Key_value = input("What is the value of the key? ")
    diction[user_input] = Key_value
    pprint(diction)
    for user_input in diction:
        if diction[user_input] == Key_value:
            print("exists as value! TRY AGAIN") 
            add()
    else:
        main_fun()

def main_fun():
    key = input("what would you like to do? ")
    if key == "add":
        add()
        
main_fun()
    
    
    
