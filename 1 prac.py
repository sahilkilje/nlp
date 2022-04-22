import nltk
from nltk import word_tokenize
text = "Hello World. NLP Practical"
word_tokenize(text)

'''
import nltk #library
f = open("data.txt", "r")
text = f.read()
sentences = nltk.sent_tokenize(text)
#whole paragraph break into sentence.
for sentence in sentences:
    print (sentence)
    print ()
'''

'''
import nltk #library
from nltk.tokenize import word_tokenize
f = open("data.txt", "r")
text = f.read()
sentences = nltk.sent_tokenize(text)
#whole paragraph
for sentence in sentences:
    print("Sentence is:", sentence)
    print("Tokens are:", word_tokenize (sentence))
    print()
'''
