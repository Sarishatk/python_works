# check the word is kankaru or not


source_word  = "hlo"

target_word = "hlo"

kangaru=(set(source_word).intersection(set(target_word)))

if list(kangaru) == list(target_word):

    print("it is a kankaru word")

else:

    print("not an kankaru word")

# it is not a proper progarm beacuse we can put targer word = obserrrvvvvv now it show it is kankaru word beacuse set duplications are not allowed