# 5️⃣ Maximum Subarray Sum (Kadane’s Algorithm)
# Find contiguous subarray with maximum sum.
# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6





class Subarray:
    def subarraysum(self,num):
        n = len(num)
        max_sum = 0
        for i in range(n):
            for j in range(i,n):
                current_sum = 0
                for k in range(i ,j+1):
                    print(num[k],end=" ")
                    
                    current_sum += num[k]
                    if max_sum<current_sum:
                        max_sum = current_sum
                print()    
        print("maximum sum of subarray by brouteforce ",max_sum)            
        return max_sum            
                
               
    def by_Kadanes_algo(self, num):
        max_sum = 0
        current_sum = 0
        for i in range(len(num)):
            
            current_sum += num[i]

            if max_sum < current_sum:
                max_sum = current_sum
            
            if current_sum < 0:
                current_sum=0

        print("maximum sum of subarray by kadane's algorithms : ",max_sum)
        return max_sum




t = Subarray()
t.subarraysum([-2,1,-3,4,-1,2,1,-5,4])
# t.subarraysum([3,-9,18,45])
t.by_Kadanes_algo([-2,1,-3,4,-1,2,1,-5,4])
# t.by_Kadanes_algo([3,-9,18,45])
