n=int(input("Enter a number:"))
term1=0
term2=1
print(term1)
print(term2)
for i in range(2,n):
    term3=term1+term2
    term1=term2
    term2=term3
    print(term3)
