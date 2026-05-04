data = [
    {"name": "A", "score": 80},
    {"name": "B", "score": 45},
    {"name": "C", "score": 70}
]

list_name = [ f"{dict_items["name"]}_pass" for dict_items in data  if dict_items["score"] >50]
print(list_name)

