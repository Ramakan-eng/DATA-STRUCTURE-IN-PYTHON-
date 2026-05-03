# Flatten a 2D list:

# [[1, 2], [3, 4], [5, 6]]

# into a single list using list comprehension.

nes_list = [[1, 2], [3, 4], [5, 6]]

flatten_list = [ i for sublist in nes_list  for i in sublist]

print(flatten_list)