from typing import List, Dict

from Mail import Mail
from NaiveBayesClassifier import BayesClassifier
from Data import Data, DataPart
from WordsStatistic import WordsStatistic
from MailComplexAnalizator import MailComplexAnalizator
from Utils import Metrics


def main():
    data = Data()
    data.read_data("./Dataset")

    folds = list(data.parts.keys())
    f_scores = []

    global_test_data = []
    global_predicted_data = []

    for test_fold in folds:
        test_data = []
        predicted_data = []

        print("test_fold: " + test_fold +
              "-------------------------------------------------------------------")
        analizator = MailComplexAnalizator()
        for train_fold in folds:
            if train_fold != test_fold:
                analizator.add_to_word_statistics(data.parts[train_fold])
        test_mails: DataPart = data.parts[test_fold]

        print("test_fold: " + test_fold +
              " calculate fscore ---------------------------------------------------")

        for spam_mail in test_mails.spams:
            test_data.append(1)
            global_test_data.append(1)
            is_spam = int(analizator.is_spam(spam_mail, is_check_incomings=True,
                                             accounting_ratio_subject=1, accounting_ratio_body=1, accounting_ratio_words=1))
            predicted_data.append(is_spam)
            global_predicted_data.append(is_spam)

        for ham_mail in test_mails.hams:
            test_data.append(0)
            global_test_data.append(0)
            is_spam = int(analizator.is_spam(ham_mail, is_check_incomings=True,
                                             accounting_ratio_subject=1, accounting_ratio_body=1, accounting_ratio_words=1))
            predicted_data.append(is_spam)
            global_predicted_data.append(is_spam)

        fscore = Metrics.f_score(test_data, predicted_data)
        print("test_fold: " + test_fold + " calculated fscore: " +
              str(fscore) + "---------------------------------------------------")
        f_scores.append(fscore)

    #print(" ".join(map(str, f_scores)))
    f_score_average = float(sum(f_scores)) / float(len(f_scores))

    print("fscore:" + str(f_score_average))

    print("------- confusion matrix ------")
    Metrics.plot_confusion_matrix(global_test_data, global_predicted_data)


if __name__ == "__main__":
    main()


# можно использовать ещё окно контекста для понимания отношения слов word2vec

print("Hello world")
