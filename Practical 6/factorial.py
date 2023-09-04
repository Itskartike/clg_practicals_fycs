def factorial(n):
    if (n==1 or n==0):
        return 1
    else:
        return (n*factorial(n-1))
num=int(input("Enter a number:"))
print("Number:",num)
print("Factorial using Recurssion:",factorial(num))
