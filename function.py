from collections import Counter
word = input("Enter a word:")
word=word.lower()
len = len(word)
mydict={}
k=1

def most_frequent(x,y):
 for j in range (x,y):
    if word[i]== chr(j) :
      if chr(j) in mydict:
        a=int(mydict.get(chr(j)))
        b=a+1
        mydict[chr(j)] = b
      else:
        mydict[chr(j)] = k
    else:
     j+=1
 return(mydict)

for i in range (len):
 most_frequent(97 , 123)
i+=1
print(mydict)

my_count = Counter(mydict)
print(my_count)
