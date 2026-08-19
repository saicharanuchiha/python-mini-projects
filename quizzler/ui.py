from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score = Label(text="Score: 0", font=("Arial", 12, "italic"), background=THEME_COLOR, foreground="white")
        self.score.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150, 125, width= 280,
            text= "text",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic")
        )
        self.canvas.grid(column=0,row=1, columnspan=2, padx=20, pady=20)

        self.correct = PhotoImage(file="images/true.png")
        self.right_button = Button(image=self.correct, highlightthickness=0, command=self.right)
        self.right_button.grid(column=0, row=2)

        self.incorrect = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=self.incorrect, highlightthickness=0,command=self.wrong)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.right_button.config(state="normal")
            self.wrong_button.config(state="normal")
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def give_feedback(self, is_right):
        self.right_button.config(state="disabled")
        self.wrong_button.config(state="disabled")

        if is_right:
            self.canvas.config(background="green")
        else:
            self.canvas.config(background="red")
        self.window.after(1000, self.get_next_question)

    def right(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def wrong(self):
        self.give_feedback(self.quiz.check_answer("False"))