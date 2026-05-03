# From a list [1, 2, 3, 4, 5, 6], create a list of squares only for even numbers.

number = [1,2,3,4,5,6]
square_even_num = [i**2 for i in number if i % 2 ==0]
print(square_even_num)