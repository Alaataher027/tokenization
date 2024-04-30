import csv
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

csv_file = 'imdp_dataset3.csv'

with open(csv_file, 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        # first column of each row
        text = row[0]

        # tokenize text
        tokens = word_tokenize(text)

        # stemming the token
        stemmed_tokens = [stemmer.stem(token) for token in tokens]

        print(stemmed_tokens)

