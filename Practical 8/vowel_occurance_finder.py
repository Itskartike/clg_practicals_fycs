#to count the number of vowels

c=0
str1=input("Enter a string")
str2=str1.lower()
for i in range(len(str2)):
               if str2[i]=="a" or str2[i]=="e" or str2[i]=="i" or str2[i]=="o" or str2[i]=="u":
                   c+=1
                   print("Total number of string in vowel ",str1,"is",c)
               
