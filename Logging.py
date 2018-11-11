class Logging:
    @staticmethod
    def log(text:str):
        with open("./Logs/log.txt", "a") as file:
            file.write(text)
