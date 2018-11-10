import os
import re
from typing import List, Dict

from Mail import *


class DataPart:
    hams: List[Mail] = []
    spams: List[Mail] = []

    def __str__(self):
        return "hams: " + str(self.hams) + \
            "spams: " + str(self.spams)


class Data:
    parts: Dict[str, DataPart] = dict()

    def read_mail(self, path: str):
        subject: str = ""
        body: str = ""
        with open(path, encoding="utf8") as file:
            subject = file.readline().replace("Subject: ", "")
            file.readline()
            body = file.readline()

        subject_words = subject.replace("\n", "").split(" ")
        body_words = body.replace("\n", "").split(" ")

        subject_words = map(int, subject_words) if (
            subject_words[0] != "") else [0]
        body_words = map(int, body_words) if (body_words[0] != "") else [0]

        return Mail(subject_words, body_words)

    def read_data(self, root_data_path: str):
        folders = os.listdir(root_data_path)
        for folder in folders:
            self.parts[folder] = DataPart()
            with os.scandir(root_data_path + "/" + folder) as files:
                for file in files:
                    file_path = root_data_path + "/" + folder + "/" + file.name
                    mail = self.read_mail(file_path)
                    if("legit" in file.name):
                        part: DataPart = self.parts[folder]
                        part.hams.append(mail)
                    else:
                        part: DataPart = self.parts[folder]
                        part.spams.append(mail)
