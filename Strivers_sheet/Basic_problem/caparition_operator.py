# Class containing the compareStrings function
class Solution:
    # Function to compare two strings
    def compareStrings(self, str1, str2):
        # Return true if strings are equal
        return str1 == str2

# Driver code
if __name__ == "__main__":
    # Input first string
    print("enter first string")
    str1 = input()

    # Input second string
    print("enter second string")
    str2 = input()

    # Create Solution object
    obj = Solution()

    # Compare strings and print result
    if obj.compareStrings(str1, str2):
        print("Strings are equal")
    else:
        print("Strings are not equal")
