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





# Check if a given string exists in a list of names:
# names = ["Alice", "Bob", "Charlie", "David"], search for "Charlie".


def find_name(i ,key):
    for index,element in enumerate(i):
        if key == element:
            print(f"item find at {index}th index and name is {element} ")
            break
    else:
        print("nit found")
find_name(["Alice", "Bob", "Charlie", "David"],"Charlie")




# Find if a given character exists in a string:
# "HELLO", search for 'E'.





def find_name(i ,key):
    for index,element in enumerate(i):
        if key == element:
            print(f"item find at {index}th index and name is {element} ")
            break
    else:
        print("nit found")
find_name("HELLO","E")

