from textblob import TextBlob
import numpy as np
# aku = TextBlob("I havv goood speling! My namee is Koray Tuğberk Gübür")
# tester=aku.correct();
# print(tester)
w = TextBlob('Platform')
print(w.correct())

# blob = TextBlob("Analytics Vidhya is a great platform to learn data science. \n It helps community through blogs, hackathons, discussions,etc.")
# print(blob)