# 1️⃣ Find Maximum & Minimum
# Given an array of numbers, return max and min.



arr = [6,3,2,8,1,4]


# maximum
max = arr[0]
for i in range(1,len(arr)):
    if arr[i]>max:
        max = arr[i]
print("max is ",max)


# minimum
min = arr[0]
for i in range(1,len(arr)):
    if arr[i]<min:
        min = arr[i]
print("min is ",min)



# both 
max_value = arr[0]
min_value = arr[0]
for i in range(1,len(arr)):
    if arr[i]>max_value:
        max_value = arr[i]
    if arr[i]< min_value:
        min_value = arr[i]
print("max is ",max_value)
print("min is ",min_value)