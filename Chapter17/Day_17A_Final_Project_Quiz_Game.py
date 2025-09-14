# Write your code below this line 👇
from Day_17A_Final_Project_Quiz_Game_Question_Model import Question;
from Day_17A_Final_Project_QuizGame_Data import question_data;
from Day_17A_Final_Project_Quiz_Game_Quiz_Brain import QuizBrain;

question_bank = [];

# Creating an object on the Question().
# Getting its arguments from the question_data which is a list
# Adding it to the question_bank list
for question in question_data:
    question_bank.append(Question(question = question["question"], answer = question["answer"]));

quiz_brain = QuizBrain(list_of_questions = question_bank)

while (quiz_brain.still_has_questions()):
    quiz_brain.next_question();

print("You've completed the quiz");
print(f"Your final score was: {quiz_brain.get_score()}/{quiz_brain.get_question_number()}");