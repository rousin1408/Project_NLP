from textblob import TextBlob
import numpy as np
import os
from spellchecker import spellchecker
a = input("Masukan kalimat= ")
textBlb = TextBlob (a)            # Making our first textblob
kalimat=textBlb.correct()
print("kalimat awal= ", a)
print("Kalimat benar= ", kalimat)
# I havv goood speling! My namee is Gerry Guinardi

