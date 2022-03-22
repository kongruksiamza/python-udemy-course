class Controller:
    def __init__(self,data):
        self.question_list = data
        self.question_number = 0
        self.score = 0
        self.current=None

    #ไปยังคำถามข้อถัดไป
    def nextQuestion(self):
        self.current=self.question_list[self.question_number]
        self.question_number+=1
        #print(self.question_number,")",current.text,"? (True/False)")
        #user_answer=input("ป้อนคำตอบ :")
        #self.checkAnswer(user_answer,current.answer)
        return f"{self.question_number}) {self.current.text}"
    
    def hasQuestion(self):
        return self.question_number<len(self.question_list)

    def checkAnswer(self,userInput):
        correct_answer=self.current.answer
        if(userInput.lower() == correct_answer.lower()):
            #ได้รับคะแนน
            self.score+=1
            return True
        else :
            return False