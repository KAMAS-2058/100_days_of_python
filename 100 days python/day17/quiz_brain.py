
class QuizBrain:
    
    def __init__(self,q_list) -> None:
        self.question_num = 0
        self.question_list = q_list
        self.score = 0

    def stillHaveQuestions(self):
        if len(self.question_list) < len(self.question_list):
            return True
        else: 
            return False

    def nextQuestion(self):
        current_question = self.question_list, self.question_num
        self.question_num += 1
        user_answer = input(f"Q.{self.question_num}: {current_question.text} (True/False):")
        self.check_answer(user_answer,current_question.answer)


    def checkAnswer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("correct")
            self.score += 1
        else:
            print("incorrect")
        print(f"the correct answer is {correct_answer}")
        print(f"Your score is: {self.score} / {self.question_num} ")

    