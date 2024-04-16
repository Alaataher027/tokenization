## alaa taher ##
import nltk

input_text = input("Enter the text: ")

print("Choose one of the following options:")
print("Choice number: 1. Print tokenized words")
print("Choice number: 2. Print tokenized sentences")
print("Choice number: 3. Print output using split function")

choice = input("Enter your choice number: ")

if choice == '1':
    # considers punctuation marks, spaces, and other delimiters to separate words.
    tokenized_words = nltk.word_tokenize(input_text)
    print(tokenized_words)
elif choice == '2':
    # identifies sentence boundaries based on punctuation marks and capitalization patterns.
    tokenized_sentences = nltk.sent_tokenize(input_text)
    print(tokenized_sentences)
elif choice == '3':
    # splits the input text into words based on space
    split_output = input_text.split()
    print(split_output)
else:
    print("Invalid choice.")
