# Print FIBONACCI Number
def fib_rec(num):
    if num<=1:
        return num
    else:
        return(fib_rec(num-1)+fib_rec(num-2))

term=int(input("Enter Number of terms:"))
for i in range(term):
               print(fib_rec(i))
