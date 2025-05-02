class Question():
    def __init__(self, question:str, options:list, answer:str):
        # set the proper things
        self.__question = question
        self.__answer = answer.lower()
        # lower the whole list
        new_options = []

        for item in options:
            new_options.append(item)
        
        self.__options = new_options

    def answer(self):
        ans = input(":> ")
        if ans.lower() == self.__answer:
            print(f"Correct!")
            return True
        else:
            print(f"Incorrect! {self.__answer} was the answer.")
            return False

    def question(self):
        print("---Question---")
        print(self.__question)
        print("Options:")
        for item in self.__options:
            print(item)

    def get_question(self):
        return self.__question
    def get_answer(self):
        return self.__answer
    def get_options(self):
        return self.__options