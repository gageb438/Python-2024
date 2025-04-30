class Question():
    def __init__(self, question:str, options:list, answer:str):
        # set the proper things
        self.__question = question
        self.__answer = answer
        self.__options = options

    def answer(self):
        ans = input(":> ")
        if ans.lower() in self.__options:
            print(f"Correct!")
            return True
        else:
            print(f"Incorrect! {self.__answer} was the answer.")
            return False
    def question(self):
        print("---Science Question---")
        print("Options:")
        for item in self.__options:
            print(item)

    def get_question(self):
        return self.__question
    def get_answer(self):
        return self.__answer
    def get_options(self):
        return self.__options