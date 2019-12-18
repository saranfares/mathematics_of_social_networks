import pandas as pd

import json
import gensim
import nltk
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import STOPWORDS
from nltk.stem import WordNetLemmatizer
from nltk.stem import SnowballStemmer
from nltk.stem.porter import * 
import numpy as np
from gensim import corpora, models
from pprint import pprint

user_input = open("data/top_user_reviews.txt", "r")
business_input = open("data/top_business_reviews.txt", "r")

user_lines = user_input.readlines()
business_lines = business_input.readlines()

user_reviews = []
business_reviews = []
for line in user_lines:
    user_reviews.append(line)

for line in business_lines:
    business_reviews.append(line)

# stem and stuff
#np.random.seed(2018)
nltk.download('wordnet')

def lemmatize_stemming(text):
    stemmer = SnowballStemmer("english")
    return stemmer.stem(WordNetLemmatizer().lemmatize(text, pos='v'))

def preprocess(text):
    result = []
    for token in gensim.utils.simple_preprocess(text):
        if token not in gensim.parsing.preprocessing.STOPWORDS and len(token) > 3:
            result.append(lemmatize_stemming(token))
    return result


documents = pd.DataFrame.from_dict({"text":user_reviews})
# run preprocess on everything
processed_docs = documents["text"].map(preprocess)

# create a dictionary of words
dictionary = gensim.corpora.Dictionary(processed_docs)

dictionary.filter_extremes(no_below=5, no_above=0.5, keep_n=100000)

print(dictionary)

# create a dictionary of words
bow_corpus = [dictionary.doc2bow(doc) for doc in processed_docs]

tfidf = models.TfidfModel(bow_corpus)
corpus_tfidf = tfidf[bow_corpus]

# LDA
print("______RUNNING FOR USERS______")
lda_model = gensim.models.LdaMulticore(bow_corpus, num_topics=3, id2word=dictionary, passes=2, workers=2)
for idx, topic in lda_model.print_topics(-1):
    print('Topic: {} \nWords: {}'.format(idx, topic))


lda_model = gensim.models.LdaMulticore(bow_corpus, num_topics=10, id2word=dictionary, passes=4, workers=2)
for idx, topic in lda_model.print_topics(-1):
    print('Topic: {} \nWords: {}'.format(idx, topic))


# TF- IDF
lda_model_tfidf = gensim.models.LdaMulticore(corpus_tfidf, num_topics=10, id2word=dictionary, passes=2, workers=4)
for idx, topic in lda_model_tfidf.print_topics(-1):
    print('Topic: {} Word: {}'.format(idx, topic))


documents = pd.DataFrame.from_dict({"text":business_reviews})
# run preprocess on everything
processed_docs = documents["text"].map(preprocess)

# create a dictionary of words
dictionary = gensim.corpora.Dictionary(processed_docs)

dictionary.filter_extremes(no_below=5, no_above=0.5, keep_n=100000)

# create a dictionary of words
bow_corpus = [dictionary.doc2bow(doc) for doc in processed_docs]

tfidf = models.TfidfModel(bow_corpus)
corpus_tfidf = tfidf[bow_corpus]

# LDA
print("______RUNNING FOR RESTAURANTS______")
lda_model = gensim.models.LdaMulticore(bow_corpus, num_topics=3, id2word=dictionary, passes=2, workers=2)
for idx, topic in lda_model.print_topics(-1):
    print('Topic: {} \nWords: {}'.format(idx, topic))


lda_model = gensim.models.LdaMulticore(bow_corpus, num_topics=10, id2word=dictionary, passes=4, workers=2)
for idx, topic in lda_model.print_topics(-1):
    print('Topic: {} \nWords: {}'.format(idx, topic))


# TF- IDF
lda_model_tfidf = gensim.models.LdaMulticore(corpus_tfidf, num_topics=10, id2word=dictionary, passes=2, workers=4)
for idx, topic in lda_model_tfidf.print_topics(-1):
    print('Topic: {} Word: {}'.format(idx, topic))

