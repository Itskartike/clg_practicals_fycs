#TO FIND COMMON ELEMENT IN TWO LIST

def common(a,b):
    a_set=set(a)
    b_set=set(b)
    if(a_set & b_set):
        print(a_set & b_set)
    else:
        print("no common element")
list1=[100,200,300,400,500]
list2=[500,600,700,800]
common(list1,list2)
    
