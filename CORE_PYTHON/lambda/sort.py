# Using lambda and sorted(), sort:

students = [
("Ram",80),
("Sita",95),
("Gopal",70)
]

# by marks.
# sort = lambda x : x[1]

students.sort(key = lambda x : x[1])
print(students)

sorted_by_name = sorted(students , key = lambda x : x[0])
print(sorted_by_name)