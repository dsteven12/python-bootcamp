nums = [1, 2, 3]
print([x * 10 for x in nums])
print([x / 3 for x in nums])

# Python Simplicity
nums = [1, 2, 3, 4, 5]
# Longer version of below code
# doubled_nums = []

# for num in nums:
#     doubled_num = num * 2
#     doubled_nums.append(doubled_num)
    
# print(doubled_nums)

# Refactored code from above
doubled_nums = [num * 2 for num in nums]
print(doubled_nums)

name = "darryl"
str=""
print(str.join([char[0].upper()for char in name]))