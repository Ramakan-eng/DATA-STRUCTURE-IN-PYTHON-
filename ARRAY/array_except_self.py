# # 6️⃣ Product of Array Except Self
# Input: [1,2,3,4]
# Output: [24,12,8,6]
# ⚠️ Cannot use division.

class product:
    def brute_force(self,arr:list):
        
        n = len(arr)
        out=[]
        for i in range(n):
            mul =1 
            for j in range(n):
                if i != j : 
                    mul = mul * arr[j]
                    
            out.append(mul)

        print(out)
        return out
    


    def product_except_self(self,arr):
        n = len(arr)
        # Initialize the output array with 1s
        res = [1] * n
        
        # Left Pass: Calculate prefix products
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= arr[i]
            
        # Right Pass: Multiply by suffix products
        suffix = 1
        for i in range(n - 1, -1, -1): # Start from the end
            res[i] *= suffix
            suffix *= arr[i]
            
        return res

# Testing it
p= product()
p.brute_force([1,2,3,4])
print(p.product_except_self([1, 2, 3, 4]))

