#if statement task 1
#task 1 checking elegible for driving license or not 
age = int(input('enter your age'))
driving = input('do you know how to drive ')

if(age>=18):
    if(driving == 'Yes'):
        print('you are eligible to apply driving license')
    else :
        print('you are not eligible to apply driving license')
else :
        print('you are not eligible to apply driving license')


#task 2  check person data 


age = 25
gender = "female"
has_degree = True


if age >= 18:
    if gender == "female":
        if has_degree:
            print("You are a female adult with a degree.")
        else:
            print("You are a female adult without a degree.")
    else:
        print("You are an adult, but not female.")
elif age < 18:
    if gender == "female":
        print("You are a female minor.")
    else:
        print("You are a minor, but not female.")
else:
    print("Invalid age or gender.")



#task3 Calculate salary based on performance rating and years of experience
    
years_of_experience = 5
performance_rating = 4
base_salary = 50000


if years_of_experience >= 5:
    if performance_rating >= 4:
        salary = base_salary * 1.10  # 10% bonus for high performance
    elif performance_rating == 3:
        salary = base_salary * 1.05  # 5% bonus for average performance
    else:
        salary = base_salary  # No bonus for low performance
elif years_of_experience >= 3:
    if performance_rating >= 4:
        salary = base_salary * 1.08  # 8% bonus for high performance
    elif performance_rating == 3:
        salary = base_salary * 1.03  # 3% bonus for average performance
    else:
        salary = base_salary  # No bonus for low performance
else:
    if performance_rating >= 4:
        salary = base_salary * 1.05  # 5% bonus for high performance
    elif performance_rating == 3:
        salary = base_salary * 1.02  # 2% bonus for average performance
    else:
        salary = base_salary  # No bonus for low performance

print("Final salary:", salary)
