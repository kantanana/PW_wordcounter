# PW_wordcounter
This repository contains a word counter that count words excluding citations in the format (text, text) where text can be any ascii characters

## Current

VS 1.2 (latest)
file: main.py
input file: input.txt
desc: making use of re module to remove apa citations, and therafter count the number of words


## Versions

VS 1.1 
file: vs1_1.py
input file: vs1_1.txt
desc: iterated through the string extracted from input file, uses spaces count the number of words, stop counting if there is parathesis containing comma
loophole: if there are multiple consecutive spaces the wordcount would be inaccurate