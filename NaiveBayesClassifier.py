from typing import List, Dict, Tuple
import math

from Mail import *
from Data import *
from WordsStatistic import *


class BayesClassifier:

    smoothing_ration: float = 1.0
    all_words = 0.00000000000000001

    word_statistic: WordsStatistic = WordsStatistic()

    def train(self, train_word_statistic: WordsStatistic):
        self.word_statistic = train_word_statistic
        self.all_words = train_word_statistic.get_unique_words_count()

    def get_text_probability(self, words: Dict[int, int]):
        ham_probability_log: float = 0
        spam_probability_log: float = 0
        for word in words:
            ham_probability_log += math.log(self.___get_ham_probability(word))
            spam_probability_log += math.log(
                self.___get_spam_probability(word))

        return (ham_probability_log, spam_probability_log)

    def get_text_probability_with_income_count(self, words: Dict[int, int]):
        ham_probability_log: float = 0
        spam_probability_log: float = 0
        for word in words:
            ham_probability_log += math.log(
                self.___get_ham_probability(word) * words[word])
            spam_probability_log += math.log(
                self.___get_spam_probability(word) * words[word])

        return (ham_probability_log, spam_probability_log)

    def ___get_ham_probability(self, word: int):
        word_in_ham_count: int = 0
        if(word in self.word_statistic.hams):
            word_in_ham_count = self.word_statistic.hams[word]
        all_hams = self.word_statistic.get_hams_count()

        return self.__calculate_probability(word_in_ham_count, all_hams)

    def ___get_spam_probability(self, word: int):
        word_in_spam_count: int = 0
        if(word in self.word_statistic.spams):
            word_in_spam_count = self.word_statistic.spams[word]
        all_spams = self.word_statistic.get_spams_count()

        return self.__calculate_probability(word_in_spam_count, all_spams)

    def __calculate_probability(self, word_in_class: float, words_in_class: int):
        return (self.smoothing_ration + word_in_class) / \
            (self.smoothing_ration*self.all_words + words_in_class)


def main():
    data = Data()
    data.read_data("./Dataset")

    folds = list(data.parts.keys())

    train__words = WordsStatistic()
    train_subject_words = WordsStatistic()
    train_body_words = WordsStatistic()

    test__words = WordsStatistic()
    test_subject_words = WordsStatistic()
    test_body_words = WordsStatistic()

    test_fold = folds[0]
    #add_to_word_statistics(data.parts[test_fold], test__words, test_subject_words, test_body_words)
    for train_fold in folds:
        if train_fold != test_fold:
            add_to_word_statistics(
            data.parts[train_fold], train__words, train_subject_words, train_body_words)
    classifier = BayesClassifier();
    classifier.train(train_subject_words);

    test_mails:DataPart = data.parts[test_fold]
    spam_mails: List[Mail] = test_mails.spams;
    spam_mail: Dict[int,int] = spam_mails[0];

    probabilities: [float, float] = classifier.get_text_probability(spam_mail)

    print(probabilities)

    # for test_fold in folds:
    #     add_to_word_statistics(
    #         data.parts[test_fold], test__words, test_subject_words, test_body_words)
    #     for train_fold in folds:
    #         if train_fold != test_fold:
    #             add_to_word_statistics(
    #                 data.parts[train_fold], train__words, train_subject_words, train_body_words)


def add_to_word_statistics(data_part: DataPart, words_statistic: WordsStatistic, subject_statistic: WordsStatistic, body_statistic: WordsStatistic):
    hams: List[Mail] = data_part.hams
    spams: List[Mail] = data_part.spams
    for item in spams:
        words_statistic.add_spam_words(item.words)
        subject_statistic.add_spam_words(item.subject_words)
        body_statistic.add_spam_words(item.body_words)

    for item in hams:
        words_statistic.add_ham_words(item.words)
        subject_statistic.add_ham_words(item.subject_words)
        body_statistic.add_ham_words(item.body_words)

   # def from_data_part_to_wrods_statistic
    # print(str(fold_statistics_words))
#print(str(fold_statistics_subject))
# print(str(fold_statistics_body))


main()


print("Hello world")


# Упростить всё. Сразу читать по фодам и сразу записывать в глобальный диктионари. Можно вывети статистику общую по словам в файл

