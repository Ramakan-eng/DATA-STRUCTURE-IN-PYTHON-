words = ["apple","banana","apple","cat"]

# Create a set of word lengths.

# Expected:

# {3,5,6}

length = {len(i) for i in words}
print(length)