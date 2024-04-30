import csv
import nltk

def pos_tagging(text):
    words = nltk.word_tokenize(text)
    tagged = nltk.pos_tag(words)
    return tagged

def apply_pos_tagging_to_dataset(dataset_path, text_column):
    tagged_rows = []

    with open(dataset_path, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        fieldnames = reader.fieldnames + ['Tagged_Text']

        for row in reader:
            tagged_text = pos_tagging(row[text_column])
            row['Tagged_Text'] = tagged_text
            tagged_rows.append(row)

    # write tagged data to a new CSV file
    with open('tagged_imdp_dataset2.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(tagged_rows)

if __name__ == "__main__":
    dataset_path = "imdp_dataset2.csv"

    text_column = "review"

    apply_pos_tagging_to_dataset(dataset_path, text_column)
