ware_house = {"laptop","mouse","key-board","wifi-adapter","mic","speaker","projector"}

actual_items = {"laptop","key-board"}

# missing items

missing = ware_house.difference(actual_items)
print(missing)


# chck anagram

word1 = "listen".split()
word2 = "silent".split()
print(set(word1)==set(word2) and len(word1)==len(word2))