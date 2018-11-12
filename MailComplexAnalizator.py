from typing import List

from WordsStatistic import WordsStatistic
from NaiveBayesClassifier import BayesClassifier
from Mail import Mail
from Data import DataPart
from Logging import Logging


class MailComplexAnalizator:
    words_statistic: WordsStatistic
    subject_statistic: WordsStatistic
    body_statistic: WordsStatistic

    def __init__(self):
        self.words_statistic = WordsStatistic()
        self.subject_statistic = WordsStatistic()
        self.body_statistic = WordsStatistic()

    def is_spam(self, mail: Mail, is_check_incomings=True, accounting_ratio_body=1.0, accounting_ratio_subject=1.0, accounting_ratio_words=1.0):

        classifier = BayesClassifier()
        classifier.train(self.words_statistic)
        words_predict = classifier.predict(mail.words, is_check_incomings)

        classifier = BayesClassifier()
        classifier.train(self.subject_statistic)
        subject_predict = classifier.predict(mail.subject_words, is_check_incomings)

        classifier = BayesClassifier()
        classifier.train(self.body_statistic)
        body_predict = classifier.predict(mail.body_words, is_check_incomings)

        ham: float = words_predict[0] * accounting_ratio_words + subject_predict[0] * \
            accounting_ratio_subject + body_predict[0] * accounting_ratio_body
        spam: float = words_predict[1] * accounting_ratio_words + subject_predict[1] * \
            accounting_ratio_subject + body_predict[1] * accounting_ratio_body

        Logging.log("mail: " + mail.file_name + "; " +
                    "words_predict: (ham: " + str(words_predict[0])+", " + "spam: " + str(words_predict[1]) + "); " +
                    "subject_predict: (ham: " + str(subject_predict[0])+", " + "spam: " + str(subject_predict[1]) + "); " +
                    "body_predict: (ham: " + str(body_predict[0]) +
                    ", " + "spam: " + str(body_predict[1]) + "); " +
                    "mail_ham: " + str(ham) + " mail_spam: " + str(spam) + ";"
                    )

        return spam > ham

    def add_to_word_statistics(self, data_part: DataPart):
        hams: List[Mail] = data_part.hams
        spams: List[Mail] = data_part.spams
        for item in spams:
            self.words_statistic.add_spam_words(item.words)
            self.subject_statistic.add_spam_words(item.subject_words)
            self.body_statistic.add_spam_words(item.body_words)

        for item in hams:
            self.words_statistic.add_ham_words(item.words)
            self.subject_statistic.add_ham_words(item.subject_words)
            self.body_statistic.add_ham_words(item.body_words)
