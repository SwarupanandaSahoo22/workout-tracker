# list comprehension = a concise way for creating lists in python
#                      compact and easier to read than traditional loops
#                      ["expression" for "value" in "iterable" if condition]




# doubles = [x * 2 for x in range(1, 11)]
# print(doubles)

# quadriples = [y * 4 for y in range(1, 11)]
# print(quadriples)

# squares = [z * z for z in range(1,11)]
# print(squares)



# nums = [1, -2, 3, -4, 5, -6, -7, 8, -9, 10]
# postive_nums = [num for num in nums if num >= 0]
# negative_nums = [num for num in nums if num <= 0]
# even_nums = [num for num in nums if num % 2 == 0]
# odd_nums = [num for num in nums if num %2 != 0]

# print(odd_nums)

grades = [30, 45, 60, 59, 70, 85, 71, 52, 92, 87, 81]
passing_grades = [grade for grade in grades if grade >= 60]
print(passing_grades)