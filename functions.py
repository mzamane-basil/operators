# def function name (optional parameters):
#      return value
def addtwo(a,b):
    return a + b

print("the sum is ",addtwo(10,8))
# Area of a rectangle
def AreaRectangle (L,W):
    return L*W
print (AreaRectangle(10,5))             
print (AreaRectangle(5,5))
print (AreaRectangle(25,5))
# a program to compute simple interest using a function
def SI(p,r,t):
    return (p*r*t)/100
print (SI(1500,5/100,6))