#Accept a list of words and return length of longest word. 

word=dict()
words=input("enter a list of words: ").split(" ")
for wd in words:
    if wd not in word:
        word[wd]=len(wd)
    else:
        continue
print("list of words with length.\n",word)
lengths=word.values()
print("length of longest word: ",max(lengths))