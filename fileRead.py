myfile = open('abc.txt', 'w')
myfile.write("Rashmee/n")
myfile.write("Saxena/n")
print(myfile)
myfile.close

myfile = open('abc.txt', 'r')
statement1 = myfile.readline()
print(statement1)
statement2 = myfile.readline()
print(statement2)
print(myfile)
myfile.close

myfile = open('abc.txt', 'a')
#myfile.write("butter")
#myfile.write("bread")
print(myfile)
myfile.close

myfile = open('abc.txt', 'rb')
statement1 = myfile.readline()
print(statement1)
statement2 = myfile.readline()
print(statement2)
print(myfile)
myfile.close

 myfile = open('abc.txt', 'r+')
statement1 = myfile.readline()
print(statement1)
statement2 = myfile.readline()
print(statement2)
myfile.write("Bread/n")
myfile.write("Butter/n")
print(statement2)
print(myfile)
myfile.close 

