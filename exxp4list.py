
lst=[1,2,3,4,5]


def len_method(lst):
    count = 0
    for _ in lst:
        count += 1
    return count


def count_method(lst, item):
    count = 0
    for i in lst:
        if i == item:
            count += 1
    return count


def index_method(lst, item):
    for i in range(len(lst)):
        if lst[i] == item:
            return i
    return -1


def append_method(lst, item):
    lst[len(lst):] = [item]
    return lst


def insert_method(lst, index, item):
    lst[index:index] = [item]
    return lst


def extend_method(lst1, lst2):
    lst1[len(lst1):] = lst2
    return lst1


def remove_method(lst, item):
    for i in range(len(lst)):
        if lst[i] == item:
            del lst[i]
            break
    return lst


def pop_method(lst, index=None):
    if index is None:
        index = len(lst) - 1
    if index < 0 or index >= len(lst):
        raise IndexError("pop index out of range")
    item = lst[index]
    del lst[index]
    return item


def reverse_method(lst):
    i, j = 0, len(lst) - 1
    while i < j:
        lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j -= 1
    return lst


def sort_method(lst):
    for i in range(len(lst)):
        for j in range(0, len(lst)-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


def copy_method(lst):
    new_lst = []
    for item in lst:
        new_lst.append(item)
    return new_lst


my_list = lst
print("Original list:", my_list)
print("Length of list:", len_method(my_list))
print("Count of '3' in the list:", count_method(my_list, 3))
print("Index of '3' in the list:", index_method(my_list, 3))
print("Appending '6' to the list:", append_method(my_list, 6))
print("Inserting '0' at index 0:", insert_method(my_list, 0, 0))
other_list = [7, 8, 9]
print("Extending the list with another list:", extend_method(my_list, other_list))
print("Removing '2' from the list:", remove_method(my_list, 2))
print("Popping an item from the list:", pop_method(my_list))
print("Reversing the list:", reverse_method(my_list))
print("Sorting the list:", sort_method(my_list))
print("Copying the list:", copy_method(my_list))
