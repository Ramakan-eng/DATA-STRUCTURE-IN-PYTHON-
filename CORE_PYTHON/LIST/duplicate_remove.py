# From a list of integers, remove duplicates using list comprehension (without using set)

input_list = [1,1,2,3,4,4,5]

new_list =[]
out_list= [ new_list.append(i) for i in input_list if i not in new_list ]

print(new_list)
