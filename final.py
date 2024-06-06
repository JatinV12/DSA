print('hello','ji',sep='-',end=' ')
print('jatin')

x=20
y=x
print(x,y,sep='-')

#python docstring __DOC__
'''hello'''
print(print.__doc__)

while x<30 :x=x+1; print(x);print('hello')

name= 'jatin verma'
for item in name:
    print(item)
print(name[::-1])


'''list1 = [lambda x:x*10 for x in range(1,5)]
for item in list1:
    print(item())
'''

list1 = [1,2,[3,[4,5]],6,6,6,6]
print(list1[2])
print(list1[2][1])
print(list1[2][1][0])

print(list1.remove(6))
print(type(list1[0]))

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 3
chunks = []
for i in range(0, len(my_list), n):
 chunks.append(my_list[i:i+n])

print("Chunked List:", chunks)


max_count=0
data = [1, 2, 2, 3, 1, 4, 2]
for i in range(0,len(data)):
   counting = data.count(data[i])
   if max_count<counting:
      max_count=counting
      element=data[i]
   
print(f'{element} occured {max_count} times in list')

my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
chunks=[]
for item in range(0,len(my_tuple),3):
   chunks.append(my_tuple[item:item+3])
print(tuple(chunks))

s1={1,2,6,4,5}
s2={6,7,1,2,6,4,5}
s1.union(s2)