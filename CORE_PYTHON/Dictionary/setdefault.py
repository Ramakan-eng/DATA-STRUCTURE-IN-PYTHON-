# Use setdefault() to add key "c" with value 3 only if it doesn’t exist.

d = {"a": 1, "b": 2} 
d.setdefault("c",3)
print(d)
print(d.get("c"))