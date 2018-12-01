from typing import List, Dict, Tuple
import math

from WordsStatistic import *


class BayesClassifier:

    smoothing_ratio: float = 1.0
    all_words: float = 0.00000000000000001
    all_spams: int
    all_hams: int

    word_statistic: WordsStatistic

    def train(self, train_word_statistic: WordsStatistic):
        self.word_statistic = train_word_statistic
        self.all_words = train_word_statistic.get_unique_words_count()
        self.all_spams = train_word_statistic.spams_count
        self.all_hams = train_word_statistic.hams_count

    def predict(self, words: Dict[int, int], is_check_incomings=True):
        if(is_check_incomings):
            return self.__get_text_probability_with_income_count(words)
        else:
            return self.__get_text_probability(words)

    def __get_text_probability(self, words: Dict[int, int]):
        ham_probability_log: float = 0
        spam_probability_log: float = 0
        for word in words:
            ham_probability_log += math.log(self.__get_ham_probability(word))
            spam_probability_log += math.log(
                self.__get_spam_probability(word))

        return (ham_probability_log, spam_probability_log)

    def __get_text_probability_with_income_count(self, words: Dict[int, int]):
        ham_probability_log: float = 0
        spam_probability_log: float = 0
        for word in words:
            ham_probability_log += math.log(
                self.__get_ham_probability(word) * words[word])
            spam_probability_log += math.log(
                self.__get_spam_probability(word) * words[word])

        return (ham_probability_log, spam_probability_log)

    def __get_ham_probability(self, word: int):
        word_in_ham_count: int = 0
        if(word in self.word_statistic.hams):
            word_in_ham_count = self.word_statistic.hams[word]

        return 1.7*self.__calculate_probability(word_in_ham_count, self.all_hams)

    def __get_spam_probability(self, word: int):
        word_in_spam_count: int = 0
        if(word in self.word_statistic.spams):
            word_in_spam_count = self.word_statistic.spams[word]

        return self.__calculate_probability(word_in_spam_count, self.all_spams)

    def __calculate_probability(self, word_in_class: float, words_in_class: int):
        return (self.smoothing_ratio + word_in_class) / \
            (self.smoothing_ratio * self.all_words + words_in_class)
