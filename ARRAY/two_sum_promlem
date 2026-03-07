# 4️⃣ Two Sum Problem
# Given array and target, return indices of two numbers whose sum = target.
# Example:

# Input: [2,7,11,15], target=9
# Output: [0,1]
class TwoSum:

    def brute_force(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


    def hash_map(self, nums, target):
        hashmap = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in hashmap:
                return [hashmap[complement], i]

            hashmap[num] = i


t = TwoSum()

print("Brute:", t.brute_force([2,7,11,15],9))
print("Hash:", t.hash_map([2,7,11,15],9))

