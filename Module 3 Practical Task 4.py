def single_root_words(root_word, *other_words):
    same_words = []

    for word in other_words:
        root_word_1 = root_word.lower()
        word_1 = word.lower()

        if root_word_1 in word_1 or word_1 in root_word_1:
            same_words.append(word)

    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)

