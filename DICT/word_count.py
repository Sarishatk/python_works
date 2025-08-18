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
word = text.split()


