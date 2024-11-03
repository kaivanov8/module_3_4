# Произвольное число параметров module_3_4
# проверка на содержание
def test_word(key,word_):
    contains= False
    for m in range(0, len(word_)+1):
        for n in range(0, len(word_)+1):
            if word_[m:n].upper() == key.upper() and not(contains):
                contains = True
    return contains

def single_root_words(root_word, *other_words):
    same_words = []
    for part_list in other_words:
        if test_word(root_word, part_list) or test_word(part_list, root_word):
            same_words.append(part_list)
    return same_words

print (single_root_words('rich',
                         'richiest','orichalcum','cheers','richies'))
print (single_root_words('disablement',
                         'Able','Mable','Disable','bagel'))