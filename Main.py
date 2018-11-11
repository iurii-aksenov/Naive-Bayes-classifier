from typing import List, Dict

from Mail import *
from NaiveBayesClassifier import *
from Data import *
from WordsStatistic import *
from MailComplexAnalizator import *


def main():
    data = Data()
    data.read_data("./Dataset")

    folds = list(data.parts.keys())

    test_fold_name = folds[0]
    train_fold_name = folds[1]

    test_mails: DataPart = data.parts[test_fold_name]
    spam_mails: List[Mail] = test_mails.spams
    spam_mail: Mail = spam_mails[0]

    analizator  = MailComplexAnalizator();
    analizator.add_to_word_statistics(data.parts[train_fold_name])

    print("is spam: " + str(analizator.is_spam(spam_mail, is_check_incomings=True)))


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


# def calculateParameters(real, predicted):
#     small_number = 0.000000000000000001
#     true_positive = 0
#     false_positive = 0
#     true_negative = 0
#     false_negative = 0

#     for i in range(len(predictions)):
#         if (testData[i].label == 0) and (predictions[i] == 0):
#             trueNegative += 1
#         if (testData[i].label == 0) and (predictions[i] == 1):
#             falsePositive += 1
#         if (testData[i].label == 1) and (predictions[i] == 1):
#             truePositive += 1
#         if (testData[i].label == 1) and (predictions[i] == 0):
#             falseNegative += 1

#     positive = smallNumber if (
#         truePositive + falseNegative) == 0 else truePositive + falseNegative
#     negative = smallNumber if (
#         trueNegative + falsePositive) == 0 else trueNegative + falsePositive
#     precision = truePositive / \
#         (smallNumber if (truePositive + falsePositive)
#          == 0 else truePositive + falsePositive)
#     accuracy = (truePositive + trueNegative) / (positive + negative)
#     fscore = 2*(precision*recall) / \
#         (smallNumber if (precision+recall) == 0 else precision+recall)

#     return (recall, specificity, precision, accuracy, fscore)
