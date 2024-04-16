############# 1 ##############
import spacy

def tokenize_sentences(text, language):
    # Load the SpaCy language model for the specified language
    nlp = spacy.blank(language)

    # Process the text using the loaded language model
    doc = nlp(text)

    # Tokenize the text into sentences
    sentences = [sent.text for sent in doc.sents]

    return sentences


if __name__ == "__main__":
    text = input("Enter the text: ")
    language = input("Enter the language (e.g., 'fr' for French, 'de' for German): ")

    # Tokenize the text into sentences using the specified language
    sentences = tokenize_sentences(text, language)

    print("Tokenized Sentences:")
    for i, sentence in enumerate(sentences, 1):
        print(f"Sentence {i}: {sentence}")



