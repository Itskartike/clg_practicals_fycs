#Programe for basic array operator
from array import*
a=array('i',[100,200,400,500,600])
print('The initial element are:',a)

#append the value
a.append(700)
print('Append a value',a)

#inserting a value
a.insert(0,300)
print('Array after insertion value:',a)

#remove an element
a.remove(100)
print('Array after removal:',a)
#reverse the array
a.reverse()
print('array after reverse:',a)
