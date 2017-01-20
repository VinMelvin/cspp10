def replace_all(original,to_replace,replace_with):
    while True:
        original.remove(to_replace)
        original.append(replace_with)
    
    
    
a = [1,2,1,3,5,1]
replace_all(a,1,"d")
print(a)