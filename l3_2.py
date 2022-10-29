sqroot=0
i=0
while sqroot<=10:   #100, 99 = 9. , 102 = 10., 103
    result=i%3      # last value of i
    if result==0:
        print(i)
        sqroot=sqrt(i)   
    i=i+1
