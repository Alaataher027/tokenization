################ 3 ##################
from nltk.corpus import stopwords

def get_stopwords(language):
    try:
        stop_words = stopwords.words(language)
        print(f"Stopwords in {language}:")
        print(stop_words)
    except OSError:
        print(f"Stopwords for {language} not available in NLTK. Please check if the language is supported.")

def main():
    languages = ["english", "spanish", "french", "german", "italian", "russian", "swedish", "arabic"]
    for language in languages:
        get_stopwords(language)
        print()

if __name__ == "__main__":
    main()
