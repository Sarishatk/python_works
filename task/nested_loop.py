# print patter
# 1 1 1
# 2 2 2
# 3 3 3


for row in range(1,5):
    for col in range(1,4):
        print(row,end="\t")
    print()
    

for row in range(1,6):
    for col in range(1,row+1):
        print(col,end="\t")
    print()