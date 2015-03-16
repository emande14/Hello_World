# Welcome to the Pig Latin Translator!!!
# This was created with direction from http://www.codecademy.com/
# Just a way to get familiar with simple python commands and GitHub uploading
# Let's begin!

pyg = 'ay' #pig latin suffix

original = raw_input('Enter a word:') 

if len(original) > 0 and original.isalpha(): # checks that input is numeric and exists
    word = original.lower() #converts entry to lowercase
    first = word[0] #the first letter of the entered word
    new_word = word+first+pyg 
    print new_word[1:] #pig latin!
else:
    print 'Try entering a word. Also, numbers are not supported.'
