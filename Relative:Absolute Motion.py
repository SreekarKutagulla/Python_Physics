
A = float(input( " Put in speed of object A; if object is stationary, enter 0: "))
B = float(input( " Put in speed of object B; if object is stationary, enter 0: "))

if A > 0 and B > 0:
    jello = input( " Are they running in opposite directions? " )

if jello == "yes":
    Q1 = input(" Is A relative to B? ")
    
    if Q1 == "yes":
        print( "The speed of A relative to B is " + str(A - (-B)))

    else:
        print( "The speed of B relative to A is " + str(B - (-A)))

if jello == "no":
    Q1 = input(" Is A relative to B? ")
    
    if Q1 == "yes":
        print( "The speed of A relative to B is " + str(A - B))

    else:
        print( "The speed of B relative to A is " + str(B - A))
    
