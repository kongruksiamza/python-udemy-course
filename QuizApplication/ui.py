from tkinter import *
from controller import Controller
THEME_APP = '#375362'

class UserInterface:
    def __init__(self,controller:Controller):

        self.controller = controller
        #หน้าต่างโปรแกรม
        self.window=Tk()
        self.window.title("โปรแกรมทำข้อสอบ")
        self.window.config(padx=20,pady=20,bg=THEME_APP)
        #พื้นที่แสดงคะแนนสอบ
        self.scoreLabel=Label(text="คะแนน : 0",fg="white",bg=THEME_APP)
        self.scoreLabel.grid(row=0,column=2)
        #พื้นที่แสดงโจทย์ปัญหา
        self.canvas=Canvas(width=300,height=250,bg="white")
        self.question_text=self.canvas.create_text(
            150,
            125,
            width=280,
            text="1 + 1 = 2",
            font=('Arial',18,'bold'),
            fill=THEME_APP
        )
        self.canvas.grid(row=1,column=1,columnspan=2,pady=50)
        #ปุ่มตัวเลือกให้เลือกตอบคำถาม
        true_image = PhotoImage(file="images/check.png")
        self.true_button=Button(image=true_image,command=self.true_pressed)
        self.true_button.grid(row=2,column=1)

        false_image = PhotoImage(file="images/remove.png")
        self.false_button=Button(image=false_image,command=self.false_pressed)
        self.false_button.grid(row=2,column=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        if self.controller.hasQuestion():
            q_text=self.controller.nextQuestion()
            self.scoreLabel.config(text=f"คะแนน : {self.controller.score}")
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text='สิ้นสุดการทำข้อสอบ')
            self.scoreLabel.config(text=f"คะแนน : {self.controller.score}")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    
    def true_pressed(self):
        self.controller.checkAnswer("true")
        self.waitNextQuestion()
    
    def false_pressed(self):
        self.controller.checkAnswer("false")
        self.waitNextQuestion()

    def waitNextQuestion(self):
        self.window.after(1000,self.get_next_question)