# Create a dictionary from a list:

# ["apple", "banana", "cherry"]

# Where:

# key = word
# value = length of word

list_str = ["apple", "banana", "cherry"]

new_dict = { i:len(i) for i in list_str}

print(new_dict)


