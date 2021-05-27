# 1. Write a function to print "hello_USERNAME!" USERNAME is the input of the function. 
# The first line of the code has been defined as below.

def hello_name(user_name):
    print("Hello " + user_name.title() + "!")

# 2. Print first 100 odd numbers in Python.
odd_numbers = list(range(1,200,2))
for odd_number in odd_numbers:
    print(odd_number)

# print(len(odd_numbers))

# 3. Please write a Python function, max_num_in_list to return the max number of a given list. 
def max_num_in_list(a_list):
    return max(a_list)

def max_num_in_list(a_list):
    max_num = a_list[0]
    for x in a_list:
        if x >= max_num:
            max_num = x
    return max_num

a_list = [1, 6, 62, 24]
print(max_num_in_list(a_list))

# 4. Write a function to return if the given year is a leap year. 
# A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
# The return should be boolean Type (true/false).
def is_leap_year(a_year):
    if a_year % 4 == 0:
        if a_year % 100 == 0:
            if a_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
print(is_leap_year(2000))
print(is_leap_year(2003))

# 5. Write a function to check to see if all numbers in list are consecutive numbers. 
# For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. 
# The return should be boolean Type.

def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list),(max(a_list)+1)))

a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(is_consecutive(a_list))
