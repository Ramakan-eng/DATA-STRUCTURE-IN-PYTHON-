# Check if the given String is Palindrome or not


# 14

# Problem Statement: Given a string, check if the string is palindrome or not. A string is said to be palindrome if the reverse of the string is the same as the string.

# Examples
# Example 1:
# Input: Str =  “ABCDCBA”
# Output: Palindrome
# Explanation: String when reversed is the same as string.

# Example 2:
# Input: Str = “TAKE U FORWARD”
# Output: Not Palindrome
# Explanation: String when reversed is not the same as string.


def  string_palindrome_by_broute(string_char):
    reverse_string = ""
    n = len(string_char)
    for i in range(n-1,-1,-1):
        reverse_string = reverse_string + string_char[i]
        
    if reverse_string == string_char :
        print(f"{string_char} is a string palindrome")
        return "palindrome"
    else : 
        print (f"{string_char} is not a palindrom string")

string_palindrome_by_broute("ABCDCBA")


def palindrome_by_two_pointer(string_chr):
    p1,p2= 0,len(string_chr)-1
    # actual_string = string_chr
    while p1 < p2:
        if string_chr[p1] != string_chr[p2]:
            return False

        p1 = p1 + 1
        p2 = p2 - 1 

    return True
  
str_in = "abcdcba"
result = palindrome_by_two_pointer(str_in)
if result == True:
    print(f"{str_in} is a  palindrome string")
else:
    print(f"{str_in} is not in a palindrome string")