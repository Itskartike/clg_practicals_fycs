import numpy as np
#only using num
a=np.linspace(2.0,3.0,num=5)
print(a)
#using num and endpoint
b=np.linspace(1.0,5.0,num=5,endpoint=False)
print(b)

#using num and retstep
c=np.linspace(1.0,2.0,num=5,retstep=True)
print(c)
