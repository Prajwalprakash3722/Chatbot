from newspaper import Article as ar
import random
import string
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings

warnings.filterwarnings('ignore')

nltk.download('punkt', quiet=True)
# getting the data
url = 'https://www.mayoclinic.org/diseases-conditions/brain-tumor/symptoms-causes/syc-20350084'
article = ar(url)
article.download()
article.parse()
article.nlp()
data = article.text
data_words = data.split()
text = data
sentence_list = nltk.sent_tokenize(text)
print(sentence_list)


def greeting_reply(text):
    text = text.lower()

    bot_greeting = ['hi', 'hello']

    user_greeting = ['hi', 'hola', 'hello']
    for word in text.splot():
        if word in user_greeting:
            return random.choice(bot_greeting)


def index_sort(list_var):
    length = len(list_var)
    list_index = list(range(0, length))
    x = list_var
    for i in range(0, length):
        for j in range(0, length):
            if x[list_index[i] > list_index[j]]:
                temp = list_index[i]
                list_index[i] = list_index[j]
                list_index[j] = temp
                return list_index


def bot_response(user_input):
    user_input = user_input.lower()
    sentence_list.append(user_input)
    bot_response = ''
    cm = CountVectorizer().fit_transform(sentence_list)
    similarity_scores = cosine_similarity(cm[-1], cm)
    similarity_scores_list = similarity_scores.flatten()
    index = index_sort(similarity_scores_list)

    user_input = 'Helloed'
    sentence_list.append(user_input)
    bot_response = ''
    cm = CountVectorizer().fit_transform(sentence_list)
    similarity_scores = cosine_similarity(cm[-1], cm)
    similarity_scores_list = similarity_scores.flatten()
    index = index_sort(similarity_scores_list)
    c = similarity_scores_list
    print(c)
