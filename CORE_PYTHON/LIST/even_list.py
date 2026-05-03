# Extract only even numbers from a list [10, 15, 20, 25, 30].

number = [10,15,20,35,30]

even_num = [ i for i in number if i%2 == 0]

print(even_num)