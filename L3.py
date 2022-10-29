# using for loop print the square of first 50 natural numbers
from cmath import sqrt


i=1
for i in range(1,50):  #50 times overide 
    result=i**2
    print(result)
    print("======================")
   
   
# using for loop print  multiples of 3  upto 1000  # Arithmetic progression

for i in range(1,1000):
    result=i%3
    if result==0:
        print(i)

#print multiple of 3 until square root of that multiple until it does not exceeds 100 #indirect termination
# quanitity apple - 6, count, weight, >1 kg , cash 
#end limit is not exclusively given
# salary current , icerement 6,7 ,  pay grade-26,   role , KPI - yearly/monthly
# in that case for loop cannot be used # while basic loop syntax
#while condition:
#    statement1
#    statement2
#    ....
# while and for difference in while default value is not 1 as in for, increment we have to give in while loop

sqroot=0
i=0
while sqroot<=10:   #100, 99 = 9. , 102 = 10., 103
    result=i%3      # last value of i
    if result==0:
        print(i)
        sqroot=i**0.5  
    i=i+1
print(i)  
    

   #print("hello while loop")
    

# for variable in range(start,stop,step)  #for loop syntax

#swapping
a=1
b=2
c=a
a=b
b=c

a=1
b=2
a=a+b  #a=3 b=3-2 a=3-1
b=a-b
a=a-b 

#app .net--- xml--- app java, sudo code is like a common language
#data structures - array - 2D, 3d, linked list, quque fifi, stack lifo
# data structures in Python - list, tuple (1-row),dictionary, advanced - dataframe(col, row 2D ,3D), series, ndarray
#function - inbuilt/pre-defined functions (cheat-sheet)  
#classes
#library - plotting (x,y) - pie carts, bar graphs, pictorial representation, .... (Data Visualization)
#permutation, combination, npr, ncr - binomial distribution, data statatics ()
str1="1234test"  #python 4, C= 3 eol, eoc
print(len(str1))
#print(len(a))  #TypeError: object of type 'int' has no len()
"""
i=0;
while(c[i]!=EOL)
{
    count=count+1
}
    
"""
print(str(reversed("hello")))
#for i in range
for i in str1:
    print(i)
str4="i am happy on sunday"
a=len(str4)
print("hi",str4[a-1],a)    #string or character array  char[]
print("hello",str4[-1])   #last index without knowing the lenght of the string
print("hey",str4[-20])
#print(result1)
# integer array, character array 
#Bulk of characters print in one indexing  # In C we cant do #Access the substring in java yes
print("hey1",str4[0:5:10])  #Substring ==> Slicing, time complexity is less
print("hey2",str4[0:5:2]) 
print("hey3",str4[0:5:6]) 
print("hey4",str4[1:9:2]) # String[start,stop,step/increment] start<stop loop n0 - 1,3,5,7,9
#print("hey5",str4[10:9:2])
# String Slicing
#Function Definition
