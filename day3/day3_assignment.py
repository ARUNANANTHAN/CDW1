import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
from sklearn.metrics import accuracy_score

# Load dataset
dataset_path = "/content/Spam-Classification.csv"
data = pd.read_csv(dataset_path)

# Rename the columns for consistency
data.rename(columns={"CLASS": "label", "SMS": "message"}, inplace=True)

# One-hot encode labels (spam = 1, ham = 0)
data = pd.get_dummies(data, columns=["label"], prefix=["label"])

# Check the columns after encoding
print(data.columns)

# Preprocess the messages
messages = data['message']
labels = data[['label_ham', 'label_spam']]  # Check the correct names after one-hot encoding

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(messages, labels, test_size=0.2, random_state=42)

# Tokenize the text data
tokenizer = Tokenizer(num_words=10000, oov_token="<OOV>")
tokenizer.fit_on_texts(X_train)

X_train_sequences = tokenizer.texts_to_sequences(X_train)
X_test_sequences = tokenizer.texts_to_sequences(X_test)

# Pad the sequences to the same length
max_length = 100
X_train_padded = pad_sequences(X_train_sequences, maxlen=max_length, padding="post", truncating="post")
X_test_padded = pad_sequences(X_test_sequences, maxlen=max_length, padding="post", truncating="post")

# Build the LSTM model
model = Sequential([
    Embedding(input_dim=10000, output_dim=64, input_length=max_length),
    LSTM(64, return_sequences=False),
    Dropout(0.5),
    Dense(32, activation='relu'),
    Dropout(0.5),
    Dense(2, activation='softmax')  # Softmax for multi-class classification (ham or spam)
])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(X_train_padded, y_train, epochs=5, batch_size=32, validation_data=(X_test_padded, y_test))

# Evaluate the model
loss, accuracy = model.evaluate(X_test_padded, y_test)
print(f"Test Accuracy: {accuracy * 100:.2f}%")

# Function to predict spam or ham
def predict_message(message):
    sequence = tokenizer.texts_to_sequences([message])
    padded_sequence = pad_sequences(sequence, maxlen=max_length, padding="post", truncating="post")
    prediction = model.predict(padded_sequence)[0]
    return "Spam" if prediction[1] > prediction[0] else "Ham"

# Test the prediction function with a sample message
sample_message = "Congratulations! You've won a $1000 Walmart gift card. Call now!"
result = predict_message(sample_message)
print(f"The message '{sample_message}' is classified as: {result}")