import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize,word_tokenize
import nltk.corpus
from nltk import FreqDist
sample = """Muad'Dib learned rapidly because his first training was in how to learn.
And the first lesson of all was the basic trust that he could learn.
It's shocking to find how many people do not believe they can learn,
and how many more believe learning to be difficult."""

# # Tokenzation

sample_tokens = nltk.word_tokenize(sample)
print(sample_tokens)
type(sample_tokens),len(sample_tokens)


# ### Finding frequency of words

sample_freq = FreqDist(sample_tokens)
for i in sample_freq:
    print(i,':',sample_freq[i])

# ### Apply bigram,trigram and n-gram

list(nltk.bigrams(sample_tokens))
list(nltk.trigrams(sample_tokens))
list(nltk.ngrams(sample_tokens,4)) #ngrams(tokens,n)
