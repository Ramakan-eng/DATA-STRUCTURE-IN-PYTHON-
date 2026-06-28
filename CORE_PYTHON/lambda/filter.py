# Using lambda and filter(), extract even numbers.

# Input:

# [1,2,3,4,5,6,7,8]

# Expected:

# [2,4,6,8]

l = [1,2,3,4,5,6,7,8]

even = lambda x : x%2==0

print(list(filter(even,l)))