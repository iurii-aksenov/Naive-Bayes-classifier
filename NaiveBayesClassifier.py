from typing import List, Dict

from Mail import *
from Data import *


class WordsStatistic:
    hams: Dict[int, int] = dict()
    spams: Dict[int, int] = dict()

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


class BayesClassifier:

    words: WordsStatistic = WordsStatistic()
    subject: WordsStatistic = WordsStatistic()
    body: WordsStatistic = WordsStatistic()

    def train(self):
        a = ""

    def predict(self):
        b = ""


def main():
    data = Data()
    data.read_data("./Dataset")

    folds = list(data.parts.keys())

    fold_1 = folds[0]

    fold_statistics_words = WordsStatistic()
    fold_statistics_subject = WordsStatistic()
    fold_statistics_body = WordsStatistic()

    data_part: DataPart = data.parts[fold_1]
    hams: List[Mail] = data_part.hams
    spams: List[Mail] = data_part.spams
    for item in spams:
        fold_statistics_body.add_spam_words(item.body_words)
        fold_statistics_subject.add_spam_words(item.subject_words)
        fold_statistics_words.add_spam_words(item.words)

    for item in hams:
        fold_statistics_body.add_ham_words(item.body_words)
        fold_statistics_subject.add_ham_words(item.subject_words)
        fold_statistics_words.add_ham_words(item.words)


   # def from_data_part_to_wrods_statistic

    #print(str(fold_statistics_words))
    print(str(fold_statistics_subject))
   # print(str(fold_statistics_body))


main()


print("Hello world")
