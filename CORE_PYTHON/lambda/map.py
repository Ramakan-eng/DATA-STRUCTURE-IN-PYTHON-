nums = [1,2,3,4,5]
m = lambda x:x*x
square = list(
    map(
        m,
        nums
    )
)

print(square)