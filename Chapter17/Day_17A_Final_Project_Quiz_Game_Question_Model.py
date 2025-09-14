# Write your code below this line 👇
class Question:
    def __init__(self, question, answer):
        self.__question = question;
        self.__answer = answer;

    def set_question(self, question):
        self.__question = question;

    def get_question(self):
        return self.__question;

    def set_answer(self, answer):
        self.__answer = answer;

    def get_answer(self):
        return self.__answer;