import string

# file input
file = input("enter the file path: ")

# open file
try:
    with open(file, encoding="utf-8") as f:
        poem = f.read()

        # count words in file
        poem_words = poem.lower()
        ex = str.maketrans("", "", string.punctuation)
        res = poem_words.translate(ex)
        words = res.split()

        word_count = len(words)
        print(words)
        print("Total words is: ", word_count)

        # count unique words in file by removing dublicates
        unique_words_count = len(set(words))
        print("Total unique words is: ", unique_words_count)

        # Frequency word counter
        word_dict = {}
        for w in words:
            if w in word_dict:
                word_dict[w] += 1
            else:
                word_dict[w] = 1

        print(word_dict)
except FileNotFoundError:
    print("File Not Found bro")
