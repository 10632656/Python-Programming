#Given a file f with each line in the format:
#factors:multiples
#return a file in the format:
#total_sum:factors:multiples
#f(ifn,ofn) # input file name; output file name

#Each line of the input file should be as follows:
#factors:multiples 
#e.g.
#3 5:1 2 3 4 5 6 7 8 9 15 9  
#Each line of the output file should be as follows:
#result:factors:multiples 
#e.g.
#47:3 5:1 2 3 4 5 6 7 8 9 15 9

def q(ifn,ofn):
  try:
    s='My name is %s and I am %.60f metres tall'  
    with open(ifn) as i_f, open(ofn,'w') as o_f:
      for line in i_f:
        f,m=[[int(x) for x in a.split()] for a in line.split(':')]
        print(f,m)
        print(type(f[0]))
       #sum(f)+sum(m)
        o_f.write(str(sum(f)+sum(m))+':'+line)
       # o_f.write(s[f[0]:m[0]]+':'+line)
  except FileNotFoundError:
    print ("File not Found")

q("input.txt","output.txt")

#Write a function to find the sum of all the multiples of any factor
#contained in file with filename a
#that appears in file with filename l, one number per line.
# (f,l) arre function parameters.

#Problem 1:
#Adapt the files problem to handle incorrect filenames etc.




#Problem 2:
#Adapt the last problem to handle incorrect number formats, separators etc.

#3 5 1 2 3 4 5 6 7 8 9 15 9

#3 5 : 1 2 3 4 5 6 7 8 9 15 9 2O

#Hello : World

# 3 5 0 : 1 2 3 4 5 6 7 8 9

#List and its functions