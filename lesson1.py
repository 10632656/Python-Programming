import abc
from re import T
from tkinter import E


a=5 #test
print(a, end=' ' )
print(a,a+5, sep='')
print(a,a+5, sep='and')
a="lesson1"
print(a)
a='test' #test
print(a)
print("a")
a=5.5
b=False #test 

"""c=a+b
print(c)
i=6
s="abc"
#d=i+s
#print(s+d)"""
#int and double - Arithmetic 
#double and boolean 
#String and boolean 
#print (s+b)
##-----print(sum(start =1))

#conditional statement 

if a==4:
    print("a is correct",a)
    #System.out.println
    # print("a is correct","%a")
    #curly braces are not used, instead we use colon for if and else
    #conditions are not given inside circular bracets
else:
    print("a is not right",a)
               
    
#enter an integer - check if the integer is +,- or zero
#n=int(7)
n=7
if n<0:
    print("n is a negative number")
elif n==0:
    print("n is zero")
    
elif n>0:
    print ("n is a positive")
else:
    print("n is not a valid input")
    
    #dummy variable like temprature 999
    
#Conditional Statement on string, validate if user gets the access if matches with given input string
name="Harish"  #dynamic declaration
password="123"
""" A B C   #truth table # 5 cont  a (4 t,4 f),b(2,2,2,2),c(2,2,2,2),d(2,2,2,2),e(2,2,2,2) = if no of condition is n thn 2^n (power n) 2^7  2^3 2^4 32*8 = 246
    T T T
    T T F
    T F T
    T F F
    F T T
    F T F
    F F T
    F F F
     """
if name=="Harish" and password=="123":
    print("Welcome!",name)


#if we have an integer , conditional statement check whether it is an even or odd


num=11

if num%2==0:     #modular operation Remainder result 
    print("number is even ...",num)
else:
    print("number is odd")
    
#if an integer is 2 digit or a 3 digit

#one digit = ones 1-9
#two digit = 10es 10-99
#three digit =  100es 100-99 
# for a particular segment -- 1- time of execution, parallel progrming
num2=89
if num2>=0 and num2<=9:
    print("number is one digit",num2)
elif(num2>=10 and num2<=99):
    print("number is two digit",num2)
elif(num2>=100 and num2<=999):
    print("number is three digit",num2)
    
    
    #modular operation  
    # Total 8 Arithematic Operations +,-,/,*,%,//(integral devision), **,divmod
    
d=2
result=a//2   #Quotient result Integral devision
print(result)
e=4
result=d**e   #2^3 , pow function can also be used , power
result=pow(5,2)
print(result)
result=divmod(e,d)   #give quotient and remainder
print(result)
print("for loop")
#loops for, while #start,stop,step(increment) # start default value is zero always when notgiven
for i in range(5):
    print(i)  # by default end is the new line, by default increment is 1
    
    #compilation error - segmenation fault, core dumped (in C)
    
# using for loop print the square of first 50 natural numbers
# using for loop print  multiples of 3  upto 1000  


