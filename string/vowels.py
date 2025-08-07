# read a text from user and display vowel count an consonant count

# text = (input("Enter a word : ")).casefold()
# vowels = "aeiou"
# v_count = 0
# c_count = 0
# for ch in text:
#     if ch in vowels:
#         v_count+=1
#     elif ch.isalpha():
#         c_count+=1
# print(f"vowel count is : {v_count}")
# print(f"consonant count is : {c_count}")



# chck the text is pangram or not
text = "Quick nymph bugs vex fjord waltz".casefold()
alpha = "abcdefghijklmnopqrstuvwxyz"
is_pangarm = True 
for ch in alpha:
    if ch not in text:
        is_pangarm = False
print(is_pangarm)