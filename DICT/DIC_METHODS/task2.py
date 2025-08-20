# text ="this is a python program to find most recursive word this python is simple"
# display most frequent word


text ="this is a python program to find most recursive word this python is simple"
word_count = {}
txt=text.split()
for w in txt:
    if w in word_count:
        word_count[w]+=1
    else:
        word_count[w]=1
print(word_count)

srt_wc = sorted(word_count,reverse=True,key = word_count.get)
print(srt_wc)
    

# 2nd method

max_val = max(word_count.values())
for k,v in word_count.items():
    if v==max_val:
        print(k,v)