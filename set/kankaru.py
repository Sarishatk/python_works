# check the word is kankaru or not


source_word  = "observe"

target_word = "observ"

kangaru=(set(source_word).intersection(set(target_word)))
if kangaru == set(target_word):
    print("it is a kankaru word")
else:
    print("not an kankaru word")