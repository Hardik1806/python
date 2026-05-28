n=int(input("please enter the number of words"))
list_1=[]
for i in range(n):
    inp_word=input("please enter the word")
    list_1.append(inp_word)
print(",".join(list_1))

#print(f"{word_1},{word_2},{word_3},{word_4},{word_5}")
input_sentence=input("please enter a sentence")
words=input_sentence.split()
print(",".join(words))

trim_space=input("please enter a sentence")
print(" ".join(trim_space.split()))


