# Word counter v1.1
wordcount = 0
apa = False
flag = False
with open('input.txt', 'r') as f:
    for para in f:
        para = para.strip()
        if para != '':
            wordcount += 1
        for each in para:
            if flag:
                if each == ",":
                    apa = True
                elif each == ")" and apa:
                    flag = False
                    wordcount -= 1
                elif each == ")":
                    flag = False
            else:
                if each == " ":
                    wordcount += 1
                elif each == "(":
                    flag = True

print(f'word count: {wordcount}')