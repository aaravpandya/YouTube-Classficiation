import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Embedding, LSTM, SpatialDropout1D
from sklearn.model_selection import train_test_split
from keras.utils.np_utils import to_categorical
from keras.callbacks import EarlyStopping
from keras.layers import Dropout
import tensorflow as tf
import keras as k
import re
from nltk.corpus import stopwords
from nltk import word_tokenize
STOPWORDS = set(stopwords.words('english'))
from bs4 import BeautifulSoup
from sklearn import metrics
from keras.models import load_model
from keras.utils import plot_model
import tensorflow as tf


df = pd.read_csv('output.csv',encoding="latin-1")
df.dropna(inplace=True)
df = df.reset_index(drop=True)
brackets = re.compile('[/(){}\[\]\|@,;]')
bad_symbols = re.compile('[^0-9a-z #+_]')

def recall(y_true,y_pred):
    
    TP = tf.count_nonzero(tf.where((y_pred * y_true )>0.5))
    TN = tf.count_nonzero(tf.where(((y_pred - 1) * (y_true - 1)) >0.9))
    FP = tf.count_nonzero(tf.where((y_pred * (y_true - 1)) >0.9))
    FN = tf.count_nonzero(tf.where(((y_pred - 1) * y_true)>0.9))
    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    f1 = 2 * precision * recall / (precision + recall)
    return f1

def clean_text(text):
    """
        text: a string
        
        return: modified initial string
    """
    text = text.lower()
    text = brackets.sub(' ', text) 
    text = bad_symbols.sub('', text) 
    # text = text.replace('x', '')
    # text = re.sub(r'\W+', '', text)
    text = ' '.join(word for word in text.split() if word not in stopwords.words('english'))
    return text
df['description'] = df['description'].apply(clean_text)
df['description'] = df['description'].str.replace('\d+', '')



dict_size = 50000
seq_length = 250
embed_size = 100

tokenizer = Tokenizer(num_words=dict_size, filters='!"#$%&()*+,-./:;<=>?@[\]^_`{|}~', lower=True)
tokenizer.fit_on_texts(df['description'].values)
w_to_i = tokenizer.word_index

X = tokenizer.texts_to_sequences(df['description'].values)
X = pad_sequences(X, maxlen=seq_length)
Y = pd.get_dummies(df['label']).values


X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.10, random_state = 42)
# print(X_train.shape,Y_train.shape)
# print(X_test.shape,Y_test.shape)

model = Sequential()
model.add(Embedding(dict_size, embed_size, input_length=X.shape[1]))
model.add(SpatialDropout1D(0.2))
model.add(LSTM(100, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(6, activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

epochs = 3
batch_size = 64

history = model.fit(X_train, Y_train, epochs=epochs, batch_size=batch_size,validation_split=0.1,callbacks=[EarlyStopping(monitor='val_loss', patience=3, min_delta=0.0001)])
model.save("rnn.h5")
model = load_model("rnn.h5")
plot_model(model, to_file='model.png', show_shapes=True,show_layer_names=True)
Y_pred = model.predict(X_test)

print("RNN Precision Score -> ",metrics.precision_score(Y_pred.argmax(axis=1), Y_test.argmax(axis=1), average="weighted")*100)
print("RNN Recall Score -> ",metrics.recall_score(Y_pred.argmax(axis=1), Y_test.argmax(axis=1), average="weighted")*100)
print("RNN F1 Score -> ",metrics.f1_score(Y_pred.argmax(axis=1), Y_test.argmax(axis=1), average="weighted")*100)
print("RNN  Score -> ",metrics.precision_score(Y_pred.argmax(axis=1), Y_test.argmax(axis=1), average="weighted")*100)
