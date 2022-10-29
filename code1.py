allowedweight=10
actualbaggage= int(input("Please enter the weight of your baggage: "))

while (actualbaggage>allowedweight):
    extraweight=actualbaggage-allowedweight
    #print(extraweight, "Please removed this extra weight")
    print("Please removed this extra weight by",extraweight,"Kg as this is exceeding allowed weight which is only",allowedweight,"kg")
    removedbaggage= int(input("User enter the removed weight for further checks"))
    extraweight=actualbaggage-removedbaggage
    print(actualbaggage)
   
