import string

file = input("enter the file path: ")


def file_check():
    try:
        with open(file, encoding="utf-8") as f:
            poem = f.read()
            return poem

    except FileNotFoundError:
        print("File Not Found bro!")


poem = file_check()


def clean_text(poem: str):
    poem_words = poem.lower()
    ex = str.maketrans("", "", string.punctuation)
    res = poem_words.translate(ex)
    words = res.split()
    return words


words = clean_text(poem)


def word_counter(words):
    word_count = len(words)
    unique_words = len(set(words))
    word_dict = {}
    for w in words:
        if w in word_dict:
            word_dict[w] += 1
        else:
            word_dict[w] = 1

    words_list = word_dict.items()
    sorted_list = sorted(words_list, key=lambda word: word[1], reverse=True)

    return word_count, unique_words, sorted_list


word_count, unique_words, sorted_list = word_counter(words)


print(f"\n --- Results --- \n")
print("Total words: ", word_count)
print("Unique words: ", unique_words)
print(f"\nTop 5 words:")
top = 0

for i in sorted_list:
    if top < 5:
        top += 1
        print(f"{top}. {i[0]} → {i[1]}")
    else:
        break
