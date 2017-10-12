##Exercise 3: Write a program that reads a file and prints the letters in decreasing order of frequency.
## Your program should convert all the input to lower case and only count the letters a-z. 
##Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. Find text samples from several different languages and see how letter frequency varies between languages. Compare your results with the tables at wikipedia.org/wiki/Letter_frequencies.

import string #this recogises all things that are punctuation
fname = input('Enter file name: ')
try:
    fhandle = open(fname) #etiquette for avoiding wrong file name'
except:
    print( 'File cannot be opened:', fname)
    exit()

letters = dict()

for line in fhandle:
    line = line.translate(line.maketrans('', '', string.punctuation)) #gets rid of punctuation)
    line = line.lower()
    line = line.split()

    for t in line:
        word = list(t)
        for letter in word:
            letters[letter] = letters.get(letter,0) + 1 #I think this counting is more elegant

letterlist = []
for letter, count in letters.items():
    letterlist.append( (count, letter) ) #if you swap this to letter , count it sorts on a-z, rather than count,letter,
letterlist.sort(reverse=False) #True made them in ascending order not descending

for count, letter in letterlist:
    print(letter, count)