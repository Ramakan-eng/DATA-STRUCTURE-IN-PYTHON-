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
