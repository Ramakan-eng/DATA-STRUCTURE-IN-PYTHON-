# Given:

names = ["ram","sita","ram","gopal"]

# Create a set of uppercase names.

# Expected:

# {"RAM","SITA","GOPAL"}

upper = {i.upper() for i in names }
print(upper)