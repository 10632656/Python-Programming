#5. Write a Python program to check the nth-1 string is a proper substring of nth string in a given list of strings.
# Go to the editor
#Input:
#['a', 'abb', 'sfs', 'oo', 'de', 'sfde']
# 0th, 1st
string1="de"
string2="sfde"  #(o,1), (1,2),(2,3)
L1=len(string1)
L2=len(string2)
for i in range(0,L2-L1+1):
    if string1==string2[i:i+L1]:
        print("string1 is a substring of string2")

#print sum of first 10 no's

#i=int(input("enter the number"))
#i=1
for i in range(10):
    result=i+1
    print(result)
   # sum=(int(result))
   # print(sum)