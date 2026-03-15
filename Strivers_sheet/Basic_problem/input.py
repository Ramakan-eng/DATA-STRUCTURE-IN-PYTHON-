# Complete the function printNumber which takes an integer input from the user and prints it on the screen.

class Solution:
    def printNumber(self):
        print("Enter the number to print :",end="")
        num = input("")
        print(num)
        return num
    
obj = Solution()
obj.printNumber()