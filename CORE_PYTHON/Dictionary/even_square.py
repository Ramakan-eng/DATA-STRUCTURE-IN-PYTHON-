# Q8

# Given:

nums = [1,2,3,4,5]

# Create a dictionary containing only even numbers and their squares.

# Expected:

# {
# 2:4,
# 4:16
# }

even_square = { i : i*i for i in nums if i%2==0}

print(even_square)