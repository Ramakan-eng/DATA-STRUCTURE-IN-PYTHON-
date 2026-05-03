# From a list of numbers, replace even numbers with "even" and odd numbers with "odd".

number_list = [1,2,3,4,5,6]

even_odd_num = ["even" if i%2 == 0  else "odd" for i in number_list ]

print(even_odd_num)
