#Excercise 1

basket={"Apple":5,"Banana":7}
Price={"Apple":35,"Banana":30}
total=0
for i,u in basket.items():
    for j,t in Price.items():
        if i==j:
            total=total+(u*t)
            break
print(total)

#Ex4 
#Create a basket class with the ability to addItem(self,item,qty)
#and to query the quantity of an item


class basket:
     def __init__(self):
         self.__dictBasket= {}
        # self.__qty=qty

     def addItem(self,items,qty):
       self.__dictBasket[items]=qty
     def getQty(self):
         return self.__dictBasket
       
      
x= basket() 
x.addItem("Apple",5)
x.getQty

         
     