# Search for a number in a list containing duplicates and return all indexes where it appears.
# Example: arr = [5, 3, 7, 5, 2, 5], search for 5 → output indexes: [0, 3, 5].


arr = [5, 3, 7, 5, 2, 5]
search_element = 5
position =[]
for i in range(len(arr)):
    if arr[i] == search_element:
        position.append(i)
print(position) 