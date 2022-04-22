import nltk
#nltk. download ("punkt")
#nltk.download ('averaged_perceptron_tagger')
from nltk import pos_tag, word_tokenize, RegexpParser
sentence = "Reliance Retail acquires majority stake in designer brand Abraham & Thakore."
tokens = word_tokenize(sentence)
tags = pos_tag(tokens)
grammer = "NP: {<NN><NN>}" #"NP:{<DT>?<JJ>*<NN>}" #"NP: (<DT>?<JJ.*>*<NN.*>+)"  #"NP: {<NN><NN>}"
chunker = RegexpParser (grammer)
result = chunker.parse (tags)
print (result)
result.draw()
