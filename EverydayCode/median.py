while True:
    N=int(input())
    if N==-1:
        break

    A=[]
    for i in range(N):
        #print(i)
        a=int(input())
        A.append(a)
        #print(A)
    A.sort()
    #print(A)

    medianN=0
    medianNumber=0

    if(N%2==0):
        medianN=int(N/2)
            #print(medianN)

        medianNumber=int( (A[medianN] + A[medianN-1] )/2)
    else:
        medianN=int(N/2)
            #print(medianN)
        medianNumber=int(A[medianN] )

    print(medianNumber)