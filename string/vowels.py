# read a text from user and display vowel count an consonant count

text = (input("Enter a word : "))
vowels = "aeiou"
v_count = 0
c_count = 0
for ch in text:
    if ch in vowels:
        v_count+=1
    else:
        c_count+=1
print(f"vowel count id {v_count}")
print(f"consonant count is {c_count}")