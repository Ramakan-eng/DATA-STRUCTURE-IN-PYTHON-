# Q10

# Create a dictionary from 1 to 10 where values are cubes.

# Expected:

# {
# 1:1,
# 2:8,
# 3:27,
# ...
# }

cubes = {i : i**3 for i in range(1,11)}
print(cubes)