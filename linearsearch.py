list1 = [10,20,30,40,50,60,70]

def linearsearch(number):
    for i in range(len(list1)):
        if list1[i] == number:
            print(f'number found {list1[i]} at {i}')
            return 
    print('number not found')

linearsearch(20)
def mid(start,end):
    return (start+end)/2

def binarysearch(number):
    start=0
    end=len(list1)-1
    middle = int(mid(start,end))
    while start<=end:
        if list1[middle]<number:
            start=middle+1
            middle=int(mid(start,end))
        elif list1[middle]>number:
            end=middle-1
            middle=int(mid(start,end))
        else:
            print(f'{number} found at {middle}')
            return
    print("number not found ")


binarysearch(20)
mini=min(list1[3:6])
print(mini)