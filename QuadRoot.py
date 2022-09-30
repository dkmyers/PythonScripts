from math import sqrt

def quadRoot(a, b, c):
    #ax^2 + bx + c = 0
    #x = (-b +/- sqrt((b^2)-4ac)/2a)
    retVals = [None, None]
    try:
        retVals[0] = (-b + sqrt((b*b) - 4*a*c))/(2*a)
    except ValueError:
        #Typically Value error is the result of using sqrt() with a negative parameter
        print("First root is invalid due to having a negative square root.")
    try:    
        retVals[1] = (-b - sqrt(b*b - 4*a*c))/(2*a)
    except ValueError:
        print("Second root is invalid due to having a negative square root.")
    return retVals

print("Test:", quadRoot(34,68,-510))
