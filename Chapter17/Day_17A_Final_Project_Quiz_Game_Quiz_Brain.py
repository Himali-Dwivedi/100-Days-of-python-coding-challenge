class QuizBrain:
    def __init__(self, list_of_questions):
        self.__question_number = 0;
        self.__list_of_questions = list_of_questions;
        self.__score = 0;

    def set_question_number(self, question_number):
        self.__question_number = question_number;

    def get_question_number(self):
        return self.__question_number;

    def set_list_of_questions(self, list_of_questions):
        self.__list_of_questions = list_of_questions;

    def get_list_of_questions(self):
        return self.__list_of_questions;

    def set_score(self, score):
        self.__score = score;
    
    def get_score(self):
        return self.__score;

    def still_has_questions(self):
        if(self.__question_number < len(self.__list_of_questions)):
            return True;
        else:
            return False;

    def next_question(self):
        current_question = self.__list_of_questions[self.__question_number];
        self.__question_number += 1;
        user_answer = input(f"Q.{self.get_question_number()}: {current_question.get_question()} (True/False): ");
        while(user_answer.lower() not in ["true", "false"]):
            user_answer = input(f"Invalid input!\nQ.{self.get_question_number()}: {current_question.get_question()} (True/False): ");
        self.check_answer(user_answer, current_question.get_answer())

    def check_answer(self, user_answer, correct_answer):
        if(user_answer.lower() == correct_answer.lower()):
            print("You got it right!")
            self.__score += 1;
        else:
            print("You got it wrong");
            print(f"The correct answer was: {correct_answer}.");
        print(f"Your current score is: {self.__score}/{self.__question_number}");
        print("\n");