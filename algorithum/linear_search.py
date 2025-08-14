def linearsearch(l, key):
    for index,element in enumerate(l):
        if element == key:
            print("item found",index)
            break
    else:
        print("item not found")
linearsearch([20,340,34,87],30)

        

# Search for a given number in a list of integers:
# arr = [4, 7, 1, 9, 12, 8], search for 9.


def search_given_number(l ,key):
    for index,elemet in enumerate(l):
        if key == elemet:
            print(f"item found at {index} th index ")
            break
    else:
        print("item not found")
search_given_number([4, 7, 1, 9, 12, 8],9)