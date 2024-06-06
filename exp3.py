#task 1 voting eligibility
age= int(input("enter your age "))
if (age>=18):
    print("eligible to vote")
else :
    print("not eligible to vote")



#task 2 leap year prediction 
year = int(input("enter any year"))
if (year%4)==0:
    if (year%100)==0:
        if (year%400)==0:
            print("entered year is leap")
        else:
            print("entered year is not leap")
    else :
        print("year is leap")
else :
    print("year is not leap")            


#task 3  grading system
marks = int(input("enter marks"))

if   (marks<30 and marks>=0):
    print("grade is D")
elif (marks>=30 and marks<60):
    print("grade is C")
elif (marks>=60 and marks<90):
    print("grade is B")  
elif (marks>=90 and marks<=100):
    print("grade is A")
else:
    print("invalid input")
