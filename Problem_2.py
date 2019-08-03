print("Enter the Sentence which you wish to examine:")
sen=raw_input() # sen is the string on which the count is to be executed
y= len(sen)     # storing the length of the string 'sen' onto variable 'y'
vow= spa= cons= 0 # 'vow' gives the number of occurences of vowels, 'spa' gives the number
                  # of occurences of spaces and 'cons' gives the number of occurences of consonants   
for x in range(y):
    if sen[x] in ("a","e","i","o","u","A","E","I","O","U"): # checking whether sen[x] is a vowel
        vow+=1
    elif sen[x]==" ": # checking whether sen[x] is a whitespace character
        spa+=1
    elif sen[x]==".": continue    
    else: 
        cons+=1
print("The number of vowels is {}, the number of spaces is {}, the number of consonants is {}.".format(vow,spa,cons))

        

        
        

