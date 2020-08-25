def sum_numbers (m, n=0) :
    
    res=0
    
    
    for i in range(n,m):
        if(i%5 == 0):
            res= res+i
    
    return res
    #TODO
    
    
sum_numbers (20,3)
