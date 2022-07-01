import nltk
import string
from nltk.corpus import stopwords
stopWords_nltk= stopwords.words('english')
with open ("input.txt","r") as f:
    text = f.read()
    wrd = [word for word in text.split() if word.lower() not in stopWords_nltk]
    table=str.maketrans("","",string.punctuation)
    words=[w.translate(table) for w in wrd]
    print(words)


from nltk.stem import WordNetLemmatizer
wordNetLemmatizer=WordNetLemmatizer()
from nltk.stem import PorterStemmer
porterStemmer=PorterStemmer()

print("{0:20}{1:20}{2:20}".format("Word","WordNet_Lemmatizer","Porter_Stemmer"))
print("{0:20}{1:20}{2:20}".format(".....",".................","....................."))


for word in words:
    print("{0:20}{1:20}{2:20}".format(word, wordNetLemmatizer.lemmatize(word), porterStemmer.stem(word)))

count1 = {}
with open("StemWords.txt",'w') as p:
    for word in words:
        p.write(porterStemmer.stem(word) + '\n')
        if word in count1:
            count1[word] += 1
        else:
            count1[word] = 1

print('\n')
print("Count of stemmed words is: ")
print(len(count1))
print("Frequency of words in stemmed text is: ")
print(count1)
print('\n')

count2 = {}
with open("LemmatizeWords.txt",'w') as q:
    for word in words:
        q.write(wordNetLemmatizer.lemmatize(word) + '\n')
        if word in count2:
            count2[word] += 1
        else:
            count2[word] = 1

print("Count of lemmatized words is: ")
print(len(count2))
print("Frequency of words in lemmatized text is: ")
print(count2)


f.close()
