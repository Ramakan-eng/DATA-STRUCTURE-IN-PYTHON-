# Update a dictionary:
# d1 = {"a": 1}
# d2 = {"b": 2}

# Merge d2 into d1 using update().

d1 = {"a": 1}
d2 = {"b": 2}

d1.update({"b":2})
d1.popitem()
print(d1)