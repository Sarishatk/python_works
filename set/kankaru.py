# check the word is kankaru or not


# source_word  = "hlo"

# target_word = "hlo"

# for i in range(len(source_word)):
#     if source_word[i] == target_word:
#         print("it is kankaru word")
#     else:
#         print("not a kankaru word")
# it is not a proper progarm beacuse we can put targer word = obserrrvvvvv now it show it is kankaru word beacuse set duplications are not allowed



# 2nd method

source_word = "CHICKEN"
target_word = "KEN"
pos = 0
for ch in source_word:
    if ch==target_word[pos]:
        pos+=1
    if pos == len(target_word):  # if all target letters are found
            break
if pos == len(target_word):
    print("it is kankaru word")
else:
    print("not a kankaru word")

