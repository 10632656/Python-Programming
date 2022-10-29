#files in python
from typing import Tuple


L=[1,"abc",3,"test",6,"iuy",7,9]
#[0,1,....,-2,-1]
#print(L[0])  #to print/access first element of the list
#slicing - using it we can access mulitple elements of a list at a same time
#print(L[0:3])  # print indexes upto 0,1,2
#print(L[-1:-6:-1]) # reverse order start should always be greater then end position
# positive increment : the start should be towards left(position) and end must be towards right (position), if we
#want to see the output
# negative increment: start should be towards the right and end must be towards the left 
# start is negative 
# slicing - string - it is a character array and list is a composite array , slicing works on indexing
result=L.index(9)
#print(result)
#print(len(L))
result=L.pop(1)  #by default it takes last item to delete
#print(L,result)
#Pop will create permanent deletion of the list item
L2=[1,1,L]  # list follows LIFO with dependency on the direction (right to left) 
# Queue follows LIFO # Stack follows LIFO
# 
print(L2.pop())
L.append(5)
print(L)
L.insert(0,4)  #Inserting is different than appending, insert (only one item can be insert at a time) we can give the position where to add the item in the list
#whereas in append it will only take single argument and oonly will add the item at the last of the list
print(L)
L3=[123,34,12,8,439]
L3.sort()  #ascending order
print(L3)
L3.sort(reverse=True)
print(L3)
#L.extend() # index in range 
L3.remove(8) #pop target index position, remove target the value passed it checks if present in the list, however both have single argument
#print(L3)
#L3.clear()
#print(L3)
print(L3.count(34))
#print(L3)
#Discrete, number theory, Algebra, rank, matrix, igon value analysis, 
#Linked List = traversing, sorting, insertion/adding/removal an element (in between or at last)
# Tuple is an immutable list 
T1=(1,2,9,7)
print(T1.count(0))
#print(T1)
T1=(T1,T1)
print(T1.count(T1))
T1.