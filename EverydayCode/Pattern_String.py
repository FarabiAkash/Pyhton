def pattern (str_1, str_2) : 
    """
    
    """
    patter_char=""
    
    for i in range(0,5) :
        
        patter_char=patter_char + str_1+ "|" + str_2 + str_1 + "-" + str_2
    
    return patter_char
    # todo
    # return the pattern
    
    
pattern("a","b")
