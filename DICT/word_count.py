text = "hai hello how are you are"
word = text.split()
wc = {}
for w in word:
    if w in wc:
        wc[w]+=1
    else:
        wc[w]=1  
print(wc)



# text = "ABCABB"
# Display first recursive character

text = "ABCABB"
wc = {}

for ch in text:
    if ch in wc:  
        print("First recursive character is:", ch)
        break
    else:
        wc[ch] = 1
