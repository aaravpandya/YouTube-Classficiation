import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.preprocessing import LabelEncoder
from collections import defaultdict
from nltk.corpus import wordnet as wn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import model_selection, naive_bayes, svm
from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score
import re


dataset = pd.read_csv("output2.csv",encoding = "latin-1")
dataset.dropna(inplace=True)
dataset["description"] = dataset["title"]+dataset["description"]
dataset["description"] = [line.lower() for line in dataset["description"]]


dataset["description"]= [word_tokenize(entry) for entry in dataset["description"]]
# wnl = WordNetLemmatizer()
# dataset["description"] = [wnl.lemmatize(line) for line in dataset["description"]]


for i,w in enumerate(dataset["description"]):
    if(i%1000==0):
        print(i)
    l = []
    wnl = WordNetLemmatizer()
    for word, tag in pos_tag(w):
        if word not in stopwords.words('english') and word.isalpha():
            word_Final = wnl.lemmatize(word)
            l.append(word_Final)
    dataset.loc[i,'text_final'] = str(l)

print(dataset["text_final"].head)
dataset.to_csv("pre_processed_data2.csv",index=False)
dataset.dropna(inplace=True)

X_train, X_test, Y_train, Y_test = model_selection.train_test_split(dataset['text_final'],dataset['label'],test_size=0.3)

Encoder = LabelEncoder()
Y_train = Encoder.fit_transform(Y_train)
Y_test = Encoder.fit_transform(Y_test)


Tfidf_vect = TfidfVectorizer(max_features=5000)
Tfidf_vect.fit(dataset['text_final'])

X_tfidf = Tfidf_vect.transform(X_train)
X_test_tfidf = Tfidf_vect.transform(X_test)



nb = naive_bayes.MultinomialNB()
nb.fit(X_tfidf,Y_train)


nb_pred = nb.predict(X_test_tfidf)



print("NB Recall",recall_score(nb_pred, Y_test, average="weighted")*100)
print("NB Precision",precision_score(nb_pred, Y_test,average="weighted")*100)
print("NB F1",f1_score(nb_pred, Y_test,average="weighted")*100)



SVM = svm.SVC(C=1.0, kernel='linear', degree=3, gamma='auto')
SVM.fit(X_tfidf,Y_train)


svm_pred = SVM.predict(X_test_tfidf)



print("SVM Precision",precision_score(svm_pred, Y_test, average="weighted")*100)
print("SVM Recall",recall_score(svm_pred, Y_test, average="weighted")*100)
print("SVM F1",f1_score(svm_pred, Y_test, average="weighted")*100)

