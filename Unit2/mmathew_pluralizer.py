pluralizer = input("Enter Singular Noun: ")
number = str(input("Enter A non-negative number: "))

if number == "1":
    print(number + " " + pluralizer)
    
elif number == "0":
    print(number + " " + pluralizer + "s")
    
elif pluralizer[-2:]== "fe":
    print(number + " " + pluralizer[:-2] + "ves")

elif pluralizer[-1:]== "y":
    print(number + " " + pluralizer[:-1] + "ies")
    
elif pluralizer[-2:]== "sh":
    print(number + " " + pluralizer + "es")
    
elif pluralizer[-2:]== "ch":
    print(number + " " + pluralizer + "es")
    
elif pluralizer[-2:]== "us":
    print(number + " " + pluralizer[:-2] + "i")
    
elif pluralizer[-2:]== "ay":
    print(number + " " + pluralizer + "s")
    
elif pluralizer[-2:]== "oy":
    print(number + " " + pluralizer + "s")
    
elif pluralizer[-2:]== "ey" :
    print(number + " " + pluralizer + "s")
    
elif pluralizer[-2:]== "uy" :
    print(number + " " + pluralizer + "s")
    
# Taking It Further Code -------------------------------------

elif pluralizer[-1]=="s":
    print(number + " " + pluralizer + "es")
    
elif pluralizer[-1]=="x":
    print(number + " " + pluralizer + "es")
    
elif pluralizer[-1]=="z":
    print(number + " " + pluralizer + "es")
    
elif pluralizer[-1]=="f":
    print(number + " " + pluralizer + "ves")
    
elif pluralizer[-1]=="o":
    print(number + " " + pluralizer + "es")
    
elif pluralizer[-2]=="is":
    print(number + " " + pluralizer + "es")

elif pluralizer[-2]=="on":
    print(number + " " + pluralizer + "a")

# Taking It Further Code End---------------------------------------
elif number > "1":
    print(number + " " + pluralizer + "s")
    
else:
    print("Error")


