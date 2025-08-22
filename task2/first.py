#1.  Count vowels in a word
# Input: "pneumonia" → Output: 5

# h


# 2. Count consonants in a word
# Input: "hello" → Output: 3 (h, l, l)

# input = "hello"
# vowels = "aeiou"
# for i in input:
#     if i not in vowels:
#      print(i,end=",")



# Check if a word is palindrom
# Input: "madam" → Output: True
# Input: "hello" → Output: False

user_input = input("enter a string: ")
reverse_d = user_input[::-1]
if user_input==reverse_d:
    print("the string is palindrome")
else:
    print("the string is not palindrome")


# reverse a string without using slice function

string = "hello"
reversed_stringv = "".join(reversed(string))
print(reversed_stringv)




# Find first non-repeated character

# Input: "swiss" → Output: "w"

