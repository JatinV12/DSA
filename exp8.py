def multiple_values():
    value1 = 1089
    value2 = 'Hyo'
    value3 = (1, 80, 3)
    return value1, value2, value3

result1, result2, result3 = multiple_values()

print("Result 1:", result1)
print("Result 2:", result2)
print("Result 3:", result3)


# task 1
def calculator(num1, num2):
    addition = num1 + num2
    subtraction = num1 - num2
    multiplication = num1 * num2
    division = num1 / num2 if num2 != 0 else "Cannot divide by zero"
    return addition, subtraction, multiplication, division


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))


add_result, sub_result, mul_result, div_result = calculator(num1, num2)


print("Addition:", add_result)
print("Subtraction:", sub_result)
print("Multiplication:", mul_result)
print("Division:", div_result)



#task 2

def create_2d_dict():
    
    two_d_dict = {
        'row1': {'a': 1, 'b': 2, 'c': 3},
        'row2': {'d': 4, 'e': 5, 'f': 6},
        'row3': {'g': 7, 'h': 8, 'i': 9}
    }
    
    
    return two_d_dict['row1'], two_d_dict['row2'], two_d_dict['row3']


row1, row2, row3 = create_2d_dict()


print("Row 1:", row1)
print("Row 2:", row2)
print("Row 3:", row3)
