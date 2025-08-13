list = [1,2,3,5,6]

for i in range(len(list)-1):
    j = i+1
    differnce = list[j] - list[i]
    if differnce!=1:
        print(list[i]+1,"is missing")
        break