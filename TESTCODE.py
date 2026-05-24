def get_item(lst, idx):
    try:
     return lst[idx]
    except:
     return 'Out of bounds'
print('Will this run?')
print(get_item([1, 2, 3], 5))