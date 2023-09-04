#to count no. of word & Character in a string
s1=input("Enter a string")
count=0
word=1
for i in s1:
    count+=1
    if (i==" "):
        word+=1
print('character=',count)
print('Word=',word)
