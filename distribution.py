"""
distribution.py
Author: Joseph Goff
Credit: Morgan Gardner

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
userinput = input("Please enter a string of text (the bigger the better): ")
print("The distribution of characters in " + '"' + userinput + '"'+ " is:")
userinput = userinput.lower()

characters = {'a':'','b':'','c':'','d':'','e':'','f':'','g':'','h':'','i':'','j':'','k':'','l':'','m':'','n':'','o':'','p':'','q':'','r':'','s':'','t':'','u':'','v':'','w':'','x':'','y':'','z':''}
inputlist = []

for a in userinput:
    if a!= " " and a != "," and a != "?" and a != "!" and a != "." and a != "'" and a != ";" and a != ":":
        characters[a]+=a

"""
for a in characters[a]:
    if a == len(userinput):
        print(characters[a])
characters.sort(lambda x,y: cmp(len(x), len(y))) 
"""
charlist = []
for q in characters:
    if len(characters[q]) > 0:
        charlist.append(characters[q])
    
charlist.sort()

for e in range(len(userinput),0,-1):
    for k in charlist:
        if len(k) == e:
            print(k)