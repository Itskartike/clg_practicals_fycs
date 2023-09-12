#create a list
print(list(range(0,20,2)))

#traversing a list
#for
list1=[250,500,100,250,2000]
for i in list1:
    print(i)

#index
for i in range(len(list1)):
    print(i+1,list[i])

#Concatenation + oprator in useed

list2=["C","C++","Python"]
con_list=list1+list2
print("Concatenated List=",con_list)

#Repitition * oprator is used
rep_list=list2*3
print("Repeated list=",rep_list)

#aliasing of list
ali_list=list1
print("After aliasing=",ali_list)
list1[2]=600
print(ali_list)
print(list1)

#sorting
print("List after sorting",sorted(list1))

#reverce
print(list(reversed(list1)))
print(list1.reverse())
print(reversed(list1))
 
