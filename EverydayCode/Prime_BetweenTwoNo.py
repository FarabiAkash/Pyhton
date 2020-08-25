def first_prime (number_1, number_2) :
    """Return the first prime number between number_1 and number_2"""
    
    first_priNum=0

    for i in range(number_1,number_2+1):
        for j in range(2, int(i/2)+1):
            if i % j == 0:
                break
        else:
            print (i , "is prime")
            return i
        
first_prime (4, 5)
    
