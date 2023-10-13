# Word counter 1.2
import re
wordcount = 0
text = ''
with open('input.txt', 'r') as f:
    for para in f:
        para = para.strip()
        para = re.sub(r'\([^\)]+\, [^\)]+\)', '', para)
        para = re.sub(r'[.,!?;:()"\'-]', '', para)
        para = re.sub(r'\s+', ' ', para)
        words = para.split()
        text += para
        text += ' '
        wordcount += len(words)

print(text)
print(f'wordcount: {wordcount}')        