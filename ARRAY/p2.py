# count the occurence of any particular number 

a = [1,2,2,3,4,4,5,2,5,3,1]
target_number = 2
count = 0
for i in a:
 if i == target_number:
    count += 1
    
print("the count of ",target_number," is ",count)


# count the occurence of any particular number 
a = [1,2,2,3,3,3]
dic = {}
for i in a:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

print(dic)


  

