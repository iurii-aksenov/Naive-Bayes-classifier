from typing import Dict

class WordsStatistic:
    hams: Dict[int, int] = dict()
    spams: Dict[int, int] = dict()

    def get_hams_count(self):
        result: int = 0
        for key in self.hams:
            result += self.hams[key]
        return result

    def get_spams_count(self):
        result: int = 0
        for key in self.spams:
            result += self.spams[key]
        return result

    def add_ham_words(self, words: Dict[int, int]):
        for word in words:
            self.add_ham_word(word, words[word])

    def add_spam_words(self, words: Dict[int, int]):
        for word in words:
            self.add_spam_word(word, words[word])

    def add_ham_word(self, word: int, count: int = 1):
        if(word in self.hams):
            self.hams[word] += count
        else:
            self.hams[word] = count

    def add_spam_word(self, word: int, count: int = 1):
        if(word in self.spams):
            self.spams[word] += count
        else:
            self.spams[word] = count

    def get_unique_words_count(self):
        ham_keys = self.hams.keys()
        spam_keys = self.spams.keys()
        unique_words = list(set(ham_keys).union(spam_keys))
        return len(unique_words)

    def __str__(self):
        return "hams: " + str(self.hams) + \
            "\n" + \
            "spams: " + str(self.spams)