def linearsearch(l, key):
    for index,element in enumerate(l):
        if element == key:
            print("item found",index)
            break
    else:
        print("item not found")
linearsearch([20,340,34,87],30)

        