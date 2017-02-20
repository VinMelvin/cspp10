from pprint import pprint
diction = {
    
    
    
}

def add():
    user_input = input("What key do you want to add? ")
    value = input("What is the value of the key? ")
    pprint(diction)
    if user_input in diction:
        print("exists as value! TRY AGAIN") 
        add()
    else:
        diction[user_input] = value
        pprint(diction)
        main_fun()

def remove_key():
    user_input = input("Which key do you want to remove? ")
    if user_input in diction:
        del diction[user_input]
        pprint(diction)
        main_fun()
    else:
        print("{} is not a key".format(user_input))
        remove_key()
    
def update():
    user_input = input("What key do you want to change? ")
    if user_input in diction:
        value_update = input("What is the new value? ")
        diction[user_input] = value_update
    else:
        print("Key not found! Try again!")
        update()
    
def pp_print():
    pprint(diction)
    main_fun()
    
def main_fun():
    key = input("what would you like to do? ")
    while True:
        if key == "add":
            add()
        elif key == "remove key":
            remove_key()
        elif key == "pprint":
            pp_print()
        elif key == "exit":
            print('Done')
            break
        
main_fun()

    
    
