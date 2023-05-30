primes = [2,3,4,5,6,7]
for prime in primes :
    print(prime)
    
    #prints out the 0,1,2,3,4
    count = 0
    while count < 5 :
        print(count)
        count +=1  # This same as count = count + 1
        
# for break and continue statement
#prints out 0,1,2,3,4
count =0
while True :
    print(count)
    count+=1
    if count >=5 :
        break
    
     #prints out only odd numbers - 1,3,5,7,9
    for x in range (10):
        #check if x is even
        if x % 2 == 0:
            continue
            print(x)
        
    
        
        
        
    
    

     
            
    
    
    