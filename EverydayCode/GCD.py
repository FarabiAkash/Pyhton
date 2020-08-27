
def gcdFun(a,b):

    #return a*b
    i=2
    max=0
    gcdVar=1
    if(a-b <1):
        min=a
    else:
        min=b

    num1 = a
    num2 = b
    while(i < (min/2)+1):
        #print(num1,num2)
        #print(i)
        if(num1 % i== 0 and num2 % i== 0):
            #print(i)
            gcdVar= gcdVar*i
            num1= num1 / i
            num2= num2 / i
            #print(num1,num2)
            i=1
            
        i=i+1
        #print("GCD: ",gcdVar)
    return gcdVar





print("GCD: ", gcdFun(85,120))