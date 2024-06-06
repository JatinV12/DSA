#WAP TO SHOW THE USE OF UPDATE METHOD ,CLEAR METHOD, POP METHOD IN DICTIONARY
my_dict = { 
           }



for i in range(2):
    key = input("Enter key: ")
    value = input("Enter value: ")
    my_dict[key] = value


print("Original Dictionary:")
print(my_dict)


my_dict.update({"new_key": "new_value"})
print("\nAfter Update:")
print(my_dict)


my_dict.clear()
print("\nAfter Clear:")
print(my_dict)


for i in range(2):
    key = input("Enter key: ")
    value = input("Enter value: ")
    my_dict[key] = value



print(my_dict)


key_to_pop = input("Enter key to pop: ")
popped_value = my_dict.pop(key_to_pop, "Key not found")
print("\nPopped Value:", popped_value)
print("Dictionary after pop:")
print(my_dict)
