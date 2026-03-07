# 3️⃣ Remove Duplicates (Without using set)
# Input: [1,1,2,2,3]
# Output: [1,2,3]

# This code removes duplicate but giving time complexity of 
# O(n^2) because of the in operator in list which is O(n) and 
# we are using it inside a loop which is also O(n)

a = [1,1,2,2,3,3,4]
l=[]
for i in a:
    if i not in l:
        l.append(i)
print(l)    


# this code removes duplicate but giving time complexity of O(n) 
# because of the in operator in set which is O(1) and
# we are using it inside a loop which is O(n)
a = [1,1,2,2,3,3,4]
seen=set()
result=[]
for i in a:
    if i not in seen:
        seen.add(i)
        result.append(i)
print(result)

