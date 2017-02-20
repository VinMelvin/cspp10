# # word = "hello"
# # num = "what your name "
# # print(word[1:-1])
# import random
# word = "hello"
# print(list(word[1:-1]))

# some_list = [1,2,3,4]
# random.shuffle(some_list)
# print(some_list)

# # sentence = "ello everyone in the class"
# # print(sentence.split(" "))
# # # print(sentence[1:-1])
# # for x in range(sentence):
    
# #     print(sentence[1:-1])

# # word = "hello"
# # words = list.word
# # 0

# # word.append(last)

# import random as r
# #function:scramble_word
# #purpose:scramble a word but not the last or first letters
# #arguments:the word
# def scramble_word(words):
#     if  len(words) > 3:
#         list_w = list(words)
#         fl = list_w[0]
#         ll = list_w[-1]
#         w = list_w[1:-1]
#         r.shuffle(w)
#         product = "".join(w)
#         result = fl + product + ll
#         return result
# def scramble_phrase(s):
#      words = s.split(" ")
#      fw = words[0]
#      sw = words[1]
#      lw = words[2]
#      list
#      scramble_word(fw)
#      scramble_word(sw)
#      scramble_word(lw)
#      print (fw + " " + sw + " " + lw)
     
         
         
      

      
import random
    
# scramble_phrase("laughing over summer")
text = "Take in a file and shuffle all the middle letters in between"

words = text.split(" ")

def shuffle(word):
    # get your word as a list
    word = list(word)

    # perform the shuffle operation
    random.shuffle(word)
    # return the list as a string
    word = ''.join(word)

    return word

for word in words:
    if len(word) > 3:
        s = word[0] + shuffle(word[1:-1]) + word[-1]
        
        
    else:
        print(word)