word_list=["Anaconda","Orangutan","Dinosaur","Dog","Crocodile","ELEPHANT","seagull"]
result=[]
for word in word_list:
    ast_word=""
    for letter in word:
        if letter.lower() in "aeiou":
            ast_word+="*"
        else:
            ast_word+=letter
    result.append(ast_word)
print(result)