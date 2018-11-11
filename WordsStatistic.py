from typing import Dict


class WordsStatistic:
    hams: Dict[int, int]
    hams_count: int

    spams: Dict[int, int]
    spams_count: int

    def __init__(self):
        self.hams = dict()
        self.hams_count = 0
        self.spams = dict()
        self.spams_count = 0

    def add_ham_words(self, words: Dict[int, int]):
        for word in words:
            self.__add_ham_word(word, words[word])

    def add_spam_words(self, words: Dict[int, int]):
        for word in words:
            self.__add_spam_word(word, words[word])

    def __add_ham_word(self, word: int, count: int = 1):
        self.hams_count += count
        if(word in self.hams):
            self.hams[word] += count
        else:
            self.hams[word] = count

    def __add_spam_word(self, word: int, count: int = 1):
        self.spams_count += count
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
