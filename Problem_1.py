print("Enter the Binary number you wish to convert:")
bi=input() # bi is the binary number to be converted
i= intnum= 0 # intnum will be the integer equivalent, 
             # i will be the power of 2 depending on the place value.  
temp=bi      # to retain the binary number 
while bi>0: 
    y= bi%10 # y will be the digit from each place value
    intnum+= y*(2**i)
    i+= 1
    bi/=10 # eliminating the digit in the lowest place value
print("The integer equivalent of the binary number '{}' is {}".format(temp,intnum)) 

    
