import nltk
nltk.download('stopwords')
nltk.download('punkt')
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize

MAIN_DIR = "data/"
f = open(MAIN_DIR + "top_user_reviews.txt","r")
top_revs = f.readlines()

words_d = {}
words = set()
tot_words = 0
stop_words = set(stopwords.words('english'))
print(stop_words) 
for r in top_revs:
    r = r.lower()
    r = r.replace(".","")
    r = r.replace(")","")
    r = r.replace("$","")
    r = r.replace("-","")
    r = r.replace("(","")
    r = r.replace(",","")
    r = r.replace("?","")
    r = r.replace(":","")
    r = r.replace("also","")
    r = r.replace("i'm","")

    word_tokens = r.split(" ")
    filtered = [] 
    for w in word_tokens:
        w = w.replace(" ", "")
        if w not in stop_words:
            filtered.append(w)

    for word in filtered:
        if word not in words and word != "":
            words_d[word] = 0
            words.add(word)
        if word!="":
            words_d[word]+=1
            tot_words+=1

words_idf = {}
for term in words:
    # idf(t) = log(N/(df + 1)) where n is the number of terms in the whole set
    idf = tot_words/words_d[term]
    words_idf[term] = idf

count =0 
for k, v in sorted(words_idf.items(), key=lambda item: item[1]):
    print("term: ", k, ", idf: ", v)
    count +=1
    if count == 20: break;
