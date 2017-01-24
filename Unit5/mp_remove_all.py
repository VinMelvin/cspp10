def remove_all(original,target):
    while target in original:
        original.remove(target)
   
            


a = [1,2,1,3,5,1]
remove_all(a,1)
print(a)