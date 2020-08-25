def fib (n) :
    
    """
    function fib (n) that takes in a number and returns the nth Fibonacci number
    The simplest is the series 0, 1, 1, 2, 3, 5, 8, etc.

    """
    pre_num=0
    next_num=1
    feb_num=0
    
    if(n==1):
        feb_num = pre_num
        
    elif(n==2):
        feb_num = next_num
    else:
        for i in range(n-2):
            feb_num = pre_num + next_num
            pre_num = next_num
            next_num= feb_num  
    
    return feb_num
    #todo
    
fib(6)  
