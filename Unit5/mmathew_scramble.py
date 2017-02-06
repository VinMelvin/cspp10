import random
word = "Melvin"
# funcation to shuffles word
def scramble_word(word):
    # split word by list
    if len(word) >= 4:
        split = list(word)
        first = split[0]
        last = split[-1]
        firstlast_out = split[1:-1]
        #split = list(word)
        random.shuffle(firstlast_out)
        firstlast_out.insert(0,first)
        firstlast_out.append(last)
        final = ''.join(firstlast_out)
        print(final)
    
scramble_word(word)    


sentence = "I love learning computer science"    
def scramble_phrase(sentence):
    if sentence.split(" ") >= 4:
        print(sentence)
    
    
scramble_phrase(sentence)
