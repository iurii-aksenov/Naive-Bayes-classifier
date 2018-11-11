from typing import List, Dict

from Mail import *
from NaiveBayesClassifier import *
from Data import *
from WordsStatistic import *
from MailComplexAnalizator import *


def f_score(test_data, predicted_data):
    small_number = 0.000000000000000001
    true_positive = small_number
    false_positive = small_number
    true_negative = small_number
    false_negative = small_number

    for i in range(len(predicted_data)):
        if (test_data[i] == 0) and (predicted_data[i] == 0):
            true_negative += 1
        if (test_data[i] == 0) and (predicted_data[i] == 1):
            false_positive += 1
        if (test_data[i] == 1) and (predicted_data[i] == 1):
            true_positive += 1
        if (test_data[i] == 1) and (predicted_data[i] == 0):
            false_negative += 1

    precision = true_positive / (true_positive + false_positive)
    recall = true_positive / (true_positive + false_negative)
    fscore = 2*(precision*recall) / (precision+recall)

    return fscore


def main():
    data = Data()
    data.read_data("./Dataset")

    folds = list(data.parts.keys())
    f_scores = []

    for test_fold in folds:
        test_data = []
        predicted_data = []

        print("test_fold: "+ test_fold + "-------------------------------------------------------------------")
        analizator = MailComplexAnalizator()
        for train_fold in folds:
            if train_fold != test_fold:
                analizator.add_to_word_statistics(data.parts[train_fold])
        test_mails: DataPart = data.parts[train_fold]

        print("test_fold: "+ test_fold + " calculate fscore ---------------------------------------------------")

        for spam_mail in test_mails.spams:
            test_data.append(1)
            predicted_data.append(int(analizator.is_spam(spam_mail, is_check_incomings=True)))

        for ham_mail in test_mails.hams:
            test_data.append(0)
            predicted_data.append(int(analizator.is_spam(ham_mail, is_check_incomings=True)))

        fscore  = f_score(test_data, predicted_data)
        print("test_fold: "+ test_fold + " calculated fscore: " + str(fscore) + "---------------------------------------------------")
        f_scores.append(fscore)



    # test_fold_name = folds[0]
    # train_fold_name = folds[1]

    

    # analizator = MailComplexAnalizator()
    # analizator.add_to_word_statistics(data.parts[train_fold_name])

    # test_data = []
    # predicted_data = []

    # test_mails: DataPart = data.parts[test_fold_name]
    # for spam_mail in test_mails.spams:
    #     test_data.append(1)
    #     predicted_data.append(int(analizator.is_spam(spam_mail, is_check_incomings=True)))

    # for ham_mail in test_mails.hams:
    #     test_data.append(1)
    #     predicted_data.append(int(analizator.is_spam(ham_mail, is_check_incomings=True)))

    print(" ".join(map(str,f_scores)))
    f_score_average  = float(sum(f_scores)) / float(len(f_scores))

    print("fscore:" + str(f_score_average))

    # for test_fold in folds:
    #     add_to_word_statistics(
    #         data.parts[test_fold], test__words, test_subject_words, test_body_words)
    #     for train_fold in folds:
    #         if train_fold != test_fold:
    #             add_to_word_statistics(
    #                 data.parts[train_fold], train__words, train_subject_words, train_body_words)

   # def from_data_part_to_wrods_statistic
    # print(str(fold_statistics_words))
# print(str(fold_statistics_subject))
# print(str(fold_statistics_body))


main()


print("Hello world")


# Упростить всё. Сразу читать по фодам и сразу записывать в глобальный диктионари. Можно вывети статистику общую по словам в файл





