import streamlit as st
import pandas as pd
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
import numpy as np
import matplotlib.pyplot as plt

# Load model and tokenizer
model = tf.keras.models.load_model("../data/log_classifier_model.h5")

# Load data
df = pd.read_csv("../data/logs_export.csv")
df['text'] = df['timestamp'].astype(str) + ' ' + df['level'] + ' ' + df['component'] + ' ' + df['message']

# Tokenize
tokenizer = Tokenizer(num_words=10000)
tokenizer.fit_on_texts(df['text'])
sequences = tokenizer.texts_to_sequences(df['text'])
X = pad_sequences(sequences, maxlen=200)

# Predict
preds = model.predict(X)
pred_labels = np.argmax(preds, axis=1)
df['Predicted_Label'] = pred_labels

# Dashboard
st.title("🔍 Log Classifier Dashboard")

st.write("### Sample Predictions")
st.dataframe(df[['timestamp', 'level', 'component', 'message', 'label', 'Predicted_Label']].head(10))

st.write("### Label Distribution")
st.bar_chart(df['Predicted_Label'].value_counts())

# Live input
st.write("### Predict Your Own Log")
input_text = st.text_area("Paste your log message here")

if input_text:
    seq = tokenizer.texts_to_sequences([input_text])
    padded = pad_sequences(seq, maxlen=200)
    pred = model.predict(padded)
    st.success(f"Predicted class: {np.argmax(pred)}")
