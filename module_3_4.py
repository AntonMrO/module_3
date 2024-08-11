def single_root_words(root_word, *other_words):
    same_words = []
    for words in other_words:
        if root_word.lower() in words.lower() or words.lower() in root_word.lower():
            same_words.append(words)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
result3 = single_root_words('Management', 'MAN', 'Just', 'Age', 'Manager', 'ANGEL', 'gem')
print(result3)
result4 = single_root_words('Age', 'Ag','Management', 'Just', 'Age', 'MAN', 'ANGEL', 'gem', 'Manager')
print(result4)