#display numbers from 0 to 10
i=0
p=0
while (i<=10):
    print(i)
    p = p + i 
    i=i+1
    
print("sum is " ,p)


# print pattern right angle triangle
for i in range(5):
    for j in range(i+1):
        print("*",end = "")
    print("")    


#code to print hello 10 times
for i in range(10):
    print("hello world",i+1)


# print string using for loop 
string = str(input("enter any string"))
for i in  string:
    print(i)

# print character in user defined string indexwise    
    
for i in range(len(string)):
    print(f"The character at index {i} is {string[i]}")    

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


  