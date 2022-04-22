import nltk
from nltk.corpus import inaugural
from nltk.util import ngrams
from nltk.corpus import stopwords
from nltk import word_tokenize, sent_tokenize
f = open("corpus.txt", "r")
corpus = f.read()
#### Tokenizationa ####
from nltk.tokenize import word_tokenize,sent_tokenize
sents = nltk.sent_tokenize(corpus)
print("The number of sentences is", len(sents))
words = nltk.word_tokenize(corpus)
print("The number of tokens is", len(words))
average_tokens = round(len(words)/len(sents))
print("The average number of tokens per sentence is",average_tokens)
unique_tokens = set(words)
print("The number of unique tokens are", len(unique_tokens))
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))
final_tokens = []
for each in words:
    if each not in stop_words:
        final_tokens.append(each)
print("The number of total tokens after removing stopwords are", len((final_tokens)))

sents = nltk.sent_tokenize (corpus)
stop_words = set (stopwords.words ('english'))
unigram=[]
bigram=[]
trigram=[]
fourgram=[]
tokenized_text = []
for sentence in sents:
    sentence = sentence.lower()
    sequence = word_tokenize (sentence)
    for word in sequence:
        if (word =="."):
            sequence. remove (word)
        else:
            unigram.append (word)
    tokenized_text.append(sequence)
    bigram.extend (list(ngrams (sequence, 2)))
    trigram.extend (list(ngrams (sequence, 3)))
    fourgram.extend(list(ngrams (sequence, 4)))
    
def removal (x):
    y =[]
    for pair in x:
        count = 0
        for word in pair:
            if word in stop_words:
                count = count or 0
            else:
                count = count or 1
        if (count==1):
            y.append(pair)
    return (y)

bigram = removal (bigram)
trigram = removal (trigram)
fourgram = removal (fourgram)
freq_bi = nltk.FreqDist(bigram)
freq_tri = nltk.FreqDist(trigram)
freq_four = nltk.FreqDist(fourgram)

print ("Most common n-grams without stopword removal and without add-1 smoothing: \n")
print("Most common bigrams:", freq_bi.most_common (5))
print("InMost common trigrams:",freq_tri.most_common (5))
print (" InMost common fourgrams:",freq_four.most_common (5))

#### Next Word Prediction ####

str1 = 'after that alice said the'
str2 = 'alice felt so desperate that she was’
token_1 = word_tokenize(str1)
token_2 = word_tokenize(str2)
ngram_1 = {1:[], 2:[], 3:[]}   #to store the n-grams formed  
ngram_2 = {1:[], 2:[], 3:[]}
for i in range(3):
    ngram_1[i+1] = list(ngrams(token_1, i+1))[-1]
    ngram_2[i+1] = list(ngrams(token_2, i+1))[-1]
print("String 1: ", ngram_1,"\nString 2: “,ngram_2)

#Add-1 smoothing is performed here.
            
ngrams_all = {1:[], 2:[], 3:[], 4:[]}
for i in range(4):
    for each in tokenized_text:
        for j in ngrams(each, i+1):
            ngrams_all[i+1].append(j);
ngrams_voc = {1:set([]), 2:set([]), 3:set([]), 4:set([])}
for i in range(4):
    for gram in ngrams_all[i+1]:
        if gram not in ngrams_voc[i+1]:
            ngrams_voc[i+1].add(gram)
total_ngrams = {1:-1, 2:-1, 3:-1, 4:-1}
total_voc = {1:-1, 2:-1, 3:-1, 4:-1}
for i in range(4):
    total_ngrams[i+1] = len(ngrams_all[i+1])
    total_voc[i+1] = len(ngrams_voc[i+1])                       
    
ngrams_prob = {1:[], 2:[], 3:[], 4:[]}
for i in range(4):
    for ngram in ngrams_voc[i+1]:
        tlist = [ngram]
        tlist.append(ngrams_all[i+1].count(ngram))
        ngrams_prob[i+1].append(tlist)
    
for i in range(4):
    for ngram in ngrams_prob[i+1]:
        ngram[-1] = (ngram[-1]+1)/(total_ngrams[i+1]+total_voc[i+1])             #add-1 smoothing
for i in range(4):
    ngrams_prob[i+1] = sorted(ngrams_prob[i+1], key = lambda x:x[1], reverse = True)
    
pred_1 = {1:[], 2:[], 3:[]}
for i in range(3):
    count = 0
    for each in ngrams_prob[i+2]:
        if each[0][:-1] == ngram_1[i+1]:      

#to find predictions based on highest probability of n-grams  
                 
            count +=1
            pred_1[i+1].append(each[0][-1])
            if count ==5:
                break
    if count<5:
        while(count!=5):
            pred_1[i+1].append("NOT FOUND")           
#if no word prediction is found, replace with NOT FOUND
            count +=1
for i in range(4):
    ngrams_prob[i+1] = sorted(ngrams_prob[i+1], key = lambda x:x[1], reverse = True)
    
pred_2 = {1:[], 2:[], 3:[]}
for i in range(3):
    count = 0
    for each in ngrams_prob[i+2]:
        if each[0][:-1] == ngram_2[i+1]:
            count +=1
            pred_2[i+1].append(each[0][-1])
            if count ==5:
                break
    if count<5:
        while(count!=5):
            pred_2[i+1].append("\0")
            count +=1

print("Next word predictions for the strings using the probability models of bigrams, trigrams, and fourgrams\n")
print(str1)
print("Bigram model predictions: {}\nTrigram model predictions: {}\nFourgram model predictions: {}\n" .format(pred_1[1], pred_1[2], pred_1[3]))
print(str2)
print("Bigram model predictions: {}\nTrigram model predictions: {}\nFourgram model predictions: {}" .format(pred_2[1], pred_2[2], pred_2[3]))
