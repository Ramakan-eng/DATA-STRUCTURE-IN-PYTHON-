words = ["apple", "banana", "cherry", "kiwi"]

length_map = {key : len(key) for key in words if len(key) >5}

print(length_map)