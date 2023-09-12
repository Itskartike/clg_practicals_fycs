n=int(input("Enter the number of element you want in the list:"))
print("Entered",n,"Numbers")
a=[]
b=[]
for i in range(0,n):
    x=int(input())
    a.append(x)
    print("Ad list =",a)
for i in range(0,n):
    if(a[i]>100):
        b.append("Over")
    else:
        b.append(a[i])
        print("New list=",b)
