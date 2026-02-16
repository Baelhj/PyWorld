import string


def my_file():
    # file input
    file = input("enter the file path: ")
    return file


def file_check():
    file = my_file()
    try:
        with open(file, encoding="utf-8") as f:
            poem = f.read()
            return poem

    except FileNotFoundError:
        print("File Not Found bro!")

file_check()

def clean_text(poem: str):
    poem = file_check()
    poem_words = poem.lower()
    ex = str.maketrans("", "", string.punctuation)
    res = poem_words.translate(ex)
    words = res.split()
    return words

clean_text(poem)

def word_counter(words):
    words = res.split()
    word_count = len(words)
    print(f"\n --- Results --- \n")
    print("Total words: ", word_count)
    unique_words = len(set(words))
    print("Unique words: ", unique_words)


# open file
try:
    file = my_file()
    print(f"\n --- Results --- \n")
    with open(file, encoding="utf-8") as f:
        poem = f.read()

        # count words in file
        poem_words = poem.lower()
        ex = str.maketrans("", "", string.punctuation)
        res = poem_words.translate(ex)
        words = res.split()

        word_count = len(words)
        print("Total words: ", word_count)

        # count unique words in file by removing dublicates
        unique_words_count = len(set(words))
        print("Unique words: ", unique_words_count)

        # Frequency word counter
        word_dict = {}
        for w in words:
            if w in word_dict:
                word_dict[w] += 1
            else:
                word_dict[w] = 1

        words_list = word_dict.items()
        sorted_list = sorted(words_list, key=lambda word: word[1], reverse=True)

        print(f"\nTop 5 words:")

        top = 0

        for i in sorted_list:
            if top < 5:
                top += 1
                print(f"{top}. {i[0]} → {i[1]}")
            else:
                break

except FileNotFoundError:
    print("File Not Found bro")
