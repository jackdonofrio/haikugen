import json, random

class Haiku:
    def get_word(self,words):
        return words[random.randint(0,len(words)-1)] + ' '
    def line_generator(self, n_syllables=5):
        syllable_count = 0
        line = ''
        while syllable_count < n_syllables:
            n = random.randint(1, n_syllables - syllable_count)
            syllable_count += n
            line += self.get_word(json.load(open('words.json'))[str(n)])
        return line
    # for cli use
    def write_haiku(self):
        return f'''
        {self.line_generator()}
        {self.line_generator(7)}
        {self.line_generator()}
        '''

if __name__ == '__main__':
    print(Haiku().write_haiku())