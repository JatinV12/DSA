x = 10
#assignment operator 
y = 20


#arithmetic operator
z=x+y
print(z)
z= x-y
print("subtraction is ",z)
z= x*y
print("multiplication is ",z)
z=x/z
print("division is ",z)

#relational operator


if (x<y):
 print("inside if statement")
 
print("outside if statement")

if (x>=y):
 x=x+y
 print(x)

if (x>0  and y>0):
 print("both variables are positive")

if (x>10 or y>10):
 print("atleast one of the variable is greater than 10")

if ( not y<10): 
 print("y is not less than 10")

#bitwise operator

a = 10
b = 4


print("a & b =", a & b)


print("a | b =", a | b)


print("~a =", ~a)


print("a ^ b =", a ^ b)
