from typing import List, Dict

from Mail import *
from NaiveBayesClassifier import *
from Data import *
from WordsStatistic import *


def main():
    data = Data()
    data.read_data("./Dataset")

    folds = list(data.parts.keys())

    train_all_words = WordsStatistic()
    train_subject_words = WordsStatistic()
    train_body_words = WordsStatistic()

    test__words = WordsStatistic()
    test_subject_words = WordsStatistic()
    test_body_words = WordsStatistic()

    test_fold_name = folds[0]

    train_fold_name = folds[1]
    add_to_word_statistics(
        data.parts[train_fold_name], train_all_words, train_subject_words, train_body_words)

    test_mails: DataPart = data.parts[test_fold_name]
    spam_mails: List[Mail] = test_mails.spams
    spam_mail: Mail = spam_mails[0]

    print("-------------------      ---------------------------")

    classifier = BayesClassifier()
    classifier.train(train_subject_words)
    probabilities: [float, float] = classifier.predict(spam_mail.subject_words)
    print("ham: " + str(probabilities[0]) + " spam: " + str(probabilities[1]))

    classifier = BayesClassifier()
    classifier.train(train_body_words)
    probabilities: [float, float] = classifier.predict(spam_mail.body_words)
    print("ham: " + str(probabilities[0]) + " spam: " + str(probabilities[1]))

    classifier = BayesClassifier()
    classifier.train(train_all_words)
    probabilities: [float, float] = classifier.predict(spam_mail.words)
    print("ham: " + str(probabilities[0]) + " spam: " + str(probabilities[1]))

    print("-------------------   income   ---------------------------")

    classifier = BayesClassifier()
    classifier.train(train_subject_words)
    probabilities: [float, float] = classifier.predict(
        spam_mail.subject_words, True)
    print("ham: " + str(probabilities[0]) + " spam: " + str(probabilities[1]))

    classifier = BayesClassifier()
    classifier.train(train_body_words)
    probabilities: [float, float] = classifier.predict(
        spam_mail.body_words, True)
    print("ham: " + str(probabilities[0]) + " spam: " + str(probabilities[1]))

    classifier = BayesClassifier()
    classifier.train(train_all_words)
    probabilities: [float, float] = classifier.predict(spam_mail.words, True)
    print("ham: " + str(probabilities[0]) + " spam: " + str(probabilities[1]))

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
# print(str(fold_statistics_subject))
# print(str(fold_statistics_body))


main()


print("Hello world")


# Упростить всё. Сразу читать по фодам и сразу записывать в глобальный диктионари. Можно вывети статистику общую по словам в файл
