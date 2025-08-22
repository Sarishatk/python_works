# First Repeated Character
# Input: "programming


word = "programming"
reapted_character = set()
for i in word:
    if i in reapted_character:
        print("the first repeated character is ",i)
        break
    else:
        reapted_character.add(i)