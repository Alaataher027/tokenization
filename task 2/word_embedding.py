import csv
from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize

def tokenize_text(text):
    return word_tokenize(text)

def train_word2vec_model(dataset_path, text_column, embedding_size=100, window=5, min_count=1, workers=4):
    # Load the dataset and tokenize the text
    sentences = []
    with open(dataset_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            sentences.append(tokenize_text(row[text_column]))

    # train model
    model = Word2Vec(sentences, size=embedding_size, window=window, min_count=min_count, workers=workers)

    return model

def save_word_embeddings(model, output_path):
    model.save(output_path)

if __name__ == "__main__":
    # Path to the dataset
    dataset_path = "imdp_dataset3.csv"

    # Name of the column containing the text data
    text_column = "review"

    word2vec_model = train_word2vec_model(dataset_path, text_column)

    output_path = "word2vec_model.bin"
    save_word_embeddings(word2vec_model, output_path)


# import csv
# import nltk
# import numpy as np
#
# # Function to tokenize text
# def tokenize_text(text):
#     return nltk.word_tokenize(text)
#
# # Function to generate training data
# def generate_training_data(tokenized_sentences, window_size):
#     X_train = []
#     y_train = []
#
#     for sentence in tokenized_sentences:
#         for i, target_word in enumerate(sentence):
#             for context_word in sentence[max(i - window_size, 0): min(i + window_size, len(sentence)) + 1]:
#                 if target_word != context_word:
#                     X_train.append(target_word)
#                     y_train.append(context_word)
#
#     return X_train, y_train
#
# def train_word2vec_model(dataset_path, text_column, embedding_size=100, window_size=5):
#     # Load the dataset and tokenize the text
#     tokenized_sentences = []
#     with open(dataset_path, 'r', newline='', encoding='utf-8') as csvfile:
#         reader = csv.DictReader(csvfile)
#         for row in reader:
#             tokenized_sentences.append(tokenize_text(row[text_column]))
#
#     # Generate training data
#     X_train, y_train = generate_training_data(tokenized_sentences, window_size)
#
#     # Compute vocabulary size
#     vocab_size = len(set(X_train + y_train))
#
#     # Initialize word embeddings randomly
#     word_vectors = {}
#     for word in set(X_train + y_train):
#         word_vectors[word] = np.random.uniform(-1, 1, embedding_size)
#
#     # Train word embeddings
#     for i in range(len(X_train)):
#         target_word = X_train[i]
#         context_word = y_train[i]
#
#         # Predicted context word
#         predicted_context = np.dot(word_vectors[target_word], word_vectors[context_word])
#
#         # Error
#         error = predicted_context - 1
#
#         # Update word vectors
#         word_vectors[target_word] -= 0.01 * error * word_vectors[context_word]
#
#     return word_vectors
#
# if __name__ == "__main__":
#     # Path to the dataset
#     dataset_path = "imdp_dataset3.csv"
#
#     # Name of the column containing the text data
#     text_column = "review"
#
#     # Train Word2Vec model
#     word_vectors = train_word2vec_model(dataset_path, text_column)
#
#     # Print word vectors for some words
#     words_to_print = ['good', 'bad', 'excellent']
#     for word in words_to_print:
#         print(f"Word: {word}, Vector: {word_vectors[word]}")
#
