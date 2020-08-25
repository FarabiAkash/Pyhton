def reverse (name) :
    # todo 
    # return reversed_name
    n=len(name)
    rev_name=""
    
    while n>0:
        rev_name=rev_name+name[n-1]
        n -=1
        
    return rev_name

reverse("all")
