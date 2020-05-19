

def main():

    file_name = "98-0.txt"
    stop_words_file_name = "stopwords"

    file1 = open(stop_words_file_name, encoding="utf8")
    stop_words = file1.readlines()
    clean_stop_words = []
    for stop_word in stop_words:
        clean_stop_words.append(stop_word.strip())
    print(clean_stop_words)

    word_counts = {}
    line_count = 0
    word_count = 0

    file2 = open(file_name, encoding="utf8")

    while True:

        line = file2.readline()
        if line == "":
            break

        line_count += 1

        words = line.lower().split(" ")
        for word in words:
            word_count += 1
            clean_word = word.strip()
            clean_word = clean_word.replace(".","")
            clean_word = clean_word.replace('\"', "")
            clean_word = clean_word.replace("'", "")
            clean_word = clean_word.replace(",", "")
            clean_word = clean_word.replace("?", "")
            clean_word = clean_word.replace("!", "")

            if clean_word != "" and clean_word not in clean_stop_words:
                if clean_word not in word_counts:
                    word_counts[clean_word] = 0
                word_counts[clean_word] += 1

    print(f'{line_count} lines and {word_count} words processed...')

    wcs = (list(word_counts.items()))
    wcs.sort(key=lambda x:x[1], reverse=True)
    print(wcs[0:10])

    file1.close()
    file2.close()

    exit(0)


if __name__ == "__main__":
    main()