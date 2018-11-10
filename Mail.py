class Mail:
    words = dict()
    subject_words = dict()
    body_words = dict()

    def __add_word(self, word: str):
        if(word in self.words):
            self.words[word] += 1
        else:
            self.words[word] = 1

    def add_subject_word(self, word: str):
        self.__add_word(word)

        if(word in self.words):
            self.subject_words[word] += 1
        else:
            self.subject_words[word] = 1

    def add_body_word(self, word: str):
        self.__add_word(word)

        if(word in self.words):
            self.body_words[word] += 1
        else:
            self.body_words[word] = 1
