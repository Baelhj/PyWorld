import string

# file input
file = input("enter the file path: ")
print(f"\n --- Results --- \n")

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

        words_list = set(word_dict.items())
        sorted_list = sorted(words_list, key=lambda word: word[1], reverse=True)
        print(
            f"""\nTop 5 words:
1. {sorted_list[0][0]} → {sorted_list[0][1]}
2. {sorted_list[1][0]} → {sorted_list[1][1]}
3. {sorted_list[2][0]} → {sorted_list[2][1]}
4. {sorted_list[3][0]} → {sorted_list[3][1]}
5. {sorted_list[4][0]} → {sorted_list[4][1]}
              """
        )


except FileNotFoundError:
    print("File Not Found bro")
