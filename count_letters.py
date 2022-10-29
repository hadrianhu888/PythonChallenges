def count_letters_in_words(word):
    word_length = len(word)
    print("The word length of the word {word} is {word_length} characters.\n")
    return word_length

def main():
    words = ["one","two", "three", "four", "five","six","seven", "eight", "nine","ten"]
    for w in words:
        count_letters_in_words(w)
        
if __name__ == "__main__":
    main()