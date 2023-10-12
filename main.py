wordcount = 0
apa = False
flag = False
with open('input.txt', 'r') as f:
    for para in f:
        if not para.isalnum():
            wordcount += 1
        para = para.strip()
        for each in para:
            if flag:
                if each == ",":
                    apa = True
                if each == ")" and apa:
                    flag = False
                    wordcount -= 1
                if each == ")":
                    flag = False
            else:
                if each == " ":
                    wordcount += 1
                elif each == "(":
                    flag = True

print(f'word count: {wordcount}')