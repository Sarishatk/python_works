# text = (input("Enter any word : "))
# for i in range(0,len(text)):
#     print(text[i])

    # OR


# text = "malayalam"
# for ch in text:
#     print(ch)




# print if string contain digit or not

# word = "helo 0 jhon 28 how are you"
# for ch in word:
#     if ch.isdigit():
#         print(ch)


# find the number of vowels count

word = "pneumonoultramicroscopicsilicovolcanoconiosi"
vowels = "aeiou"
v_count = 0
for ch in word:
    if ch in vowels:
     v_count +=1
print(v_count)