import string

# file input
file = input("enter the file path: ")
print("--- Results ---")

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

        tw = ""
        wc = ""
        print(
            f"""Top 5 words: \n
              1. {tw} → {wc} \n
              2. {tw} → {wc} \n
              3. {tw} → {wc} \n
              4. {tw} → {wc} \n
              5. {tw} → {wc}
              """
        )


except FileNotFoundError:
    print("File Not Found bro")
