while True :
    marks= int(input("enter marks "))
    if marks>=90:
        print("grade is A")
    elif marks>=80 and  marks<90 :
        print("grade is B",marks)
    elif marks>=70 and  marks<80 :
        print("grade is c",marks)   
    elif marks<70 :
        print("grade is f",marks)
    
    choice = input("do you want to reppaet this").lower()
    if choice!= "yes":
        break


factorial=int(input("enter any numver"))
temp= factorial
while (temp-1)!=0:
    factorial= factorial*(temp-1)
    temp=temp-1
print(factorial)