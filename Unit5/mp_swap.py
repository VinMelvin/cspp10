def swap(value,index1,index2):
    switch = value[index1]
    replace = value[index2]
    for index in range(len(value)):
        if value[index] == switch:
            value[index] = replace
            if value[index] == replace:
                value[index] = switch
    
    
    

a = [1,2,3,4,5,6]
swap(a,2,5)
print(a)