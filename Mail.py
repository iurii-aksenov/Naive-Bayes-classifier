from typing import List


class Mail:
    words = dict()
    subject_words = dict()
    body_words = dict()

    def __init__(self, subject_words: List[int] = [], body_words: List[int] = []):
        self.add_subject_words(subject_words)
        self.add_body_words(body_words)

    def __add_word(self, word: int):
        if(word in self.words):
            self.words[word] += 1
        else:
            self.words[word] = 1

    def add_subject_words(self,  subject_words: List[int]):
        for item in subject_words:
            self.add_subject_word(item)

    def add_body_words(self,  body_words: List[int]):
        for item in body_words:
            self.add_body_word(item)

    def add_subject_word(self, word: int):
        self.__add_word(word)

        if(word in self.subject_words):
            self.subject_words[word] += 1
        else:
            self.subject_words[word] = 1

    def add_body_word(self, word: int):
        self.__add_word(word)

        if(word in self.body_words):
            self.body_words[word] += 1
        else:
            self.body_words[word] = 1

    def __str__(self):
        return "sebject: " + str(self.subject_words) + \
            "\n" + \
            "body: " + str(self.body_words)
