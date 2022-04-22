import nltk
#nltk. download ("punkt")
#nltk.download ('averaged_perceptron_tagger')
from nltk import pos_tag, word_tokenize, RegexpParser
string = 'John stays in India. He is working in Syntel Private Ltd.'
#Tokenizing
string_token = word_tokenize(string)
#Putting POS tags
string_tag = nltk.pos_tag(string_token)
print(string_tag)

from nltk.chunk import ne_chunk
nltk. download("maxent_ne_chunker")
nltk. download("words")
string_ner = ne_chunk(string_tag)
print(string_ner)
