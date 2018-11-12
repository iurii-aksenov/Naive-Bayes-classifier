class Logging:
    @staticmethod
    def log(text:str):
        with open("./Logs/log.txt", "w") as file:
            file.write(text)
