################ 2 ##################
import nltk

def pos_tagging(input_text):
    words = nltk.word_tokenize(input_text)

    tagged_default = nltk.pos_tag(words)
    tagged_universal = nltk.pos_tag(words, tagset='universal')

    return tagged_default, tagged_universal

def main():
    input_text = input("Enter a sentence: ")
    tagged_default, tagged_universal = pos_tagging(input_text)

    print("Default Tagset (Penn Treebank):")
    print(tagged_default)

    print("\nUniversal Tagset:")
    print(tagged_universal)


if __name__ == "__main__":
    main()