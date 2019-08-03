print("Enter the limit of the series:")
N= input() # N represents the number of terms in the series
i=1        # i is used as the counter variable increased by 1 each time
sum=j=0
if N==0:
    print("Invalid limit entered")
    print("Sum is 0")
else:
    print("The series upto {} terms is given below:".format(N))
    for i in range( 1, N+1):
        j= (j*2) + 1 # j represents the number at each Nth stage
        print(j)
        sum+=j       # sum represents the total sum of the series to N terms
        i+=1
    print("The sum of the series is {}.".format(sum))    
