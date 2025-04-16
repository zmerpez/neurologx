import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Conv1D, LSTM, Dense, Dropout
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import csv
# Load CSV logs
df = pd.read_csv("data/logs_export.csv", error_bad_lines=False)

# Combine all text fields into one
df['text'] = df['timestamp'].astype(str) + ' ' + df['level'] + ' ' + df['component'] + ' ' + df['message']

# Encode labels
label_encoder = LabelEncoder()
df['label_encoded'] = label_encoder.fit_transform(df['label'])

# Tokenize text
tokenizer = Tokenizer(num_words=10000)
tokenizer.fit_on_texts(df['text'])
sequences = tokenizer.texts_to_sequences(df['text'])
X = pad_sequences(sequences, maxlen=200)
y = tf.keras.utils.to_categorical(df['label_encoded'])

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Build CNN + LSTM model
model = Sequential([
    Embedding(input_dim=10000, output_dim=128, input_length=200),
    Conv1D(64, 5, activation='relu'),
    LSTM(64),
    Dropout(0.5),
    Dense(64, activation='relu'),
    Dense(y.shape[1], activation='softmax')
])

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()

# Train
model.fit(X_train, y_train, epochs=5, batch_size=32, validation_data=(X_test, y_test))

# Save
model.save("data/log_classifier_model.h5")
