import random
y = "Melvin"
# funcation to shuffles word
def scramble_word(word):
    # split word by list
    split = list(word)
    first = split[0]
    last = split[-1]
    firstlast_out = split[1:-1]
    split = firstlast_out
    #split = list(word)
    random.shuffle(split)
    print(first,firstlast_out,last)
    x = [first, firstlast_out, last]
    final = ' '.join(x)
    print(final)
    print(split)
    
    
    
    
    
scramble_word("apples")    
    
    
#def scramble_phrase():
    
    
    
