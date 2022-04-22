from nltk.stem import PorterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import LancasterStemmer
words = ['run', 'runner', 'running', 'ran', 'runs', 'easily', 'fairly']

def portstemming(words):
    ps=PorterStemmer()
    print("Porter Stemmer")
    for word in words:
        print(word,"--->",ps.stem(word))
    
    
def snowballstemming(words):
    snowball = SnowballStemmer(language='english')
    print("Snowball Stemmer")
    for word in words:
        print(word,"--->",snowball.stem(word))
        
def lancasterstemming(words):
    lancaster = LancasterStemmer()
    print("Lancaster Stemmer")
    for word in words:
        print(word,"--->",lancaster.stem(word))
        

print("Select operation.")
print("1.Porter Stemmer")
print("2.Snowball Stemmer")
print("3.Lancaster Stemmer")


while True:
    choice = input("Enter choice(1/2/3): ")
    if choice in ('1', '2', '3'):
        if choice == '1':
            print(portstemming(words))
        elif choice == '2':
            print(snowballstemming(words))
        elif choice == '3':
            print(lancasterstemming(words))
            
        next_calculation = input("Do you want to do stemming again? (yes/no): ")
        if next_calculation == "no":
            break
            
    else:
        print("Invalid Input")

'''
import nltk
from nltk.stem import WordNetLemmatizer
lemma = WordNetLemmatizer()
text = "studies studying cries cry"
token = nltk.word_tokenize (text)
for w in token:
    print ("Lemma for {} is {}".format (w, lemma.lemmatize(w)))

'''
