def print_b_words(file_name):
    with open(file_name, 'r') as file:
        for line in file:
            words = line.split(" ")
            for word in words:
                if word.startswith('b'):
                    print(word)
                    punctuation = ",.!?\n"
                    with open(file_name, 'r') as file:
                        for line in file:
                            for p in punctuation:
                                line = line.replace(p, "")
                                words = line.split(" ")
                                for word in words:
                                    if (word.startswith('b') or word.startswith('B')) and len(word) == 3:
                            print(word)

print_b_words('bet.txt')
