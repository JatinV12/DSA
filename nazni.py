slash=0
for i in range(5):
    for j in range(6):
        if (j== 0 or j==5 or j==slash):
           print("*",end="")
           
        else:
            print(end=" ")

    slash=slash+1      
    print("")       

print(" ")
print(" ")

mid1=4
mid2=4
for i in range(5):
  for j in  range(9):
      if (j==mid1 or j==mid2 or (i==2 and j>mid1 and j<mid2)):
          print("*",end="")
      
      else:
          print(end=" ")
  mid1=mid1-1
  mid2=mid2+1
  print()


print(" ")
print(" ")

backslash=5
for i in range(6):
    for j in range(6):
        if (i==0 or i==5 or j==backslash):
           print("*",end="")
           
        else:
            print(end=" ")

    backslash=backslash-1      
    print("")

print(" ")
print(" ")



slash=0
for i in range(5):
    for j in range(6):
        if (j== 0 or j==5 or j==slash):
           print("*",end="")
           
        else:
            print(end=" ")

    slash=slash+1      
    print("")


print(" ")
print(" ")

for i in range(5):
    for j in range(9):
        if (j==4 or i==0 or i==4):
            print("*",end="")
        else:
            print(end=" ")
    print("")

print(" ")

