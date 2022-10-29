#Define a function

def substring(strng,start,stop):   #public classA(string z)
    return strng[start:stop]    # why return type was declared here
str1="Hey i am ok"
c=substring(str1,0,5)
print(c)
l=[1,"harish",85,"p"]
l2=[2,"monday",90,"q"]
l2.insert(1,"Rashmee")
l2.append("test")  
l2.pop()   # by default its last index
print(len(l))
print(type(l[2]))
print(l[1][2:])  #string slicing
#fn def +file+ list + operation , List, tuple, dictionary, list comprehension
#2 list 
print(l2)
l.append()
""" Write a Python program to reverse a string. Go to the editor
Sample String : "1234abcd"
Expected Output : "dcba4321"
Click me to see the sample solution

5. Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
"""