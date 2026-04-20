
# Define two constant integers
x = 10
y = 10

# Evaluate the sum of x and y using match-case (Python 3.10+)
match x + y:
    case 15:  # If the sum equals 15
        print("Result is 15.")
    case 20:  # If the sum equals 20
        print("Result is 20.")
    case _:   # Default case (no match)
        print("No match found.")



day = int(input("Enter a number (1-7): "))

# Match-case (Python 3.10+ feature) to act like a switch
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        # Default case if no match
        print("Invalid")




