from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

for dictionary in question_data:
    question_text = dictionary["text"]
    question_answer = dictionary["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)  # Define quiz object from QuizBrain class

while quiz.still_has_questions():  # While there is another question run code
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.question_number}.")
