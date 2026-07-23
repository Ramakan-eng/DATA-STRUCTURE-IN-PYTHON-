nums = [7, 4, 1, 5, 3, 0, 343]  
n = len(nums)

for i in range(1,n):
    key = nums[i]
    j = i-1
    while j>=0 and nums[j] > key :
        nums[j+1]  = nums[j]
        j =j-1

    nums[j+1] = key


print(nums)
