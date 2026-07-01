# Create a dictionary where:

# key = number
# value = square

square = {i:(i*i) for i in range(1,6)}
print(square)

even_square = {i : i*i for i in range(11) if i % 2== 0}
print(even_square)

d={}
for i in range(11):
    if i%2==0:
        d[i]=i*i
print(d)