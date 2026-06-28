# Given:

words = ["apple","banana","cat"]

# Create a dictionary:

# {
# "apple":5,
# "banana":6,
# "cat":3
# }

length = {i : len(i) for i in words}
print(length)