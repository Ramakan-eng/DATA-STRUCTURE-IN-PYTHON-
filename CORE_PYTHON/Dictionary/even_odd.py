dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f':6}

even_odd = {k:("even" if v%2==0 else "odd" )for k,v in dict1.items()}
print(even_odd)