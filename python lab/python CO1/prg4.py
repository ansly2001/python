# Count the occurrences of each word in a line of text
txt="the quick brown fox jumps over the lazy dog."
words={}
txt=txt.split(" ")
for word in txt:
    if word in words:
        words[word]+=1
    else:
        words[word]=1
print(words)
