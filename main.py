from textblob import TextBlob
import numpy as np
import os
from spellchecker import spellchecker
# a = input("Masukan kalimat= ")
# textBlb = TextBlob (a)            # Making our first textblob
# kalimat=textBlb.correct()
# print("kalimat awal= ", a)
# print("Kalimat benar= ", kalimat)
# I havv goood speling! My namee is Gerry Guinardi
with open("C://xampp/htdocs/Project_NLP/Project_NLP/tester.txt") as f:        # Opening the test file with the intention to read
    text = f.read()                     # Reading the file
    textBlb = TextBlob(text)            # Making our first textblob
    textCorrected = textBlb.correct()   # Correcting the text
    print(textCorrected)


def compare(text1, text2):  
    l1 = text1.split()
    l2 = text2.split()
    good = 0
    bad = 0
    for i in range(0, len(l1)):
        if l1[i] != l2[i]:
            bad += 1
        else:
            good += 1
    return (good, bad)

# Helper function to calculate the percentage of misspelled words
def percentageOfBad(x):
    return (x[1] / (x[0] + x[1])) * 100
