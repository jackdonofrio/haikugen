import json, random
def get_word(words):
    return words[random.randint(0,len(words)-1)] + ' '
def line_generator(n_syllables=5):
    syllable_count = 0
    line = ''
    while syllable_count < n_syllables:
        n = random.randint(1, n_syllables - syllable_count)
        syllable_count += n
        line += get_word(json.load(open('words.json'))[str(n)])
    return line
print(line_generator())
print(line_generator(7))
print(line_generator())
# To-do:
# - make lower syllable words more common than the 7,6,5 ones
# - add more words