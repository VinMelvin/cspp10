import random

# funcation to shuffles word
def scramble_word(word):
    # split word by list
    # if len(word) >= 4:
    split = list(word)
    first = split[0]
    last = split[-1]
    firstlast_out = split[1:-1]
    #split = list(word)
    random.shuffle(firstlast_out)
    firstlast_out.insert(0,first)
    firstlast_out.append(last)
    word = ''.join(firstlast_out)
    return word


sentence = "I love learning computer science"    
def scramble_phrase(sentence):
    words = sentence.split(" ")
    for word in words:
        if len(word) > 3:
            print(scramble_word(word))
        else:
            print(word)
            #print(" ".join(word))
            # not sure why ".join doesn't work"
    
    
scramble_phrase(sentence)
