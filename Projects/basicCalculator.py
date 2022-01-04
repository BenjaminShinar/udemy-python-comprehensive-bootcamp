#cSpell:ignore  Verdana insertwidth columnspan textvariable padx pady

from tkinter import *


def makeNumberButton(calculator, value, rowNumber, colNumber):
    btn = Button(calculator,
                 bg="#98DBC6",
                 bd=12,
                 text=str(value),
                 padx=33,
                 pady=25,
                 font=("Helvetica", 20, "bold"),
                 command=lambda: calculator.buttonClick(value))
    btn.grid(row=rowNumber, column=colNumber, sticky=W)
    return btn


class CalculatorApplication(Frame):

    def __init__(self, master):
        super(CalculatorApplication, self).__init__(master)
        self.task = ""
        self.UserIn = StringVar()
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        self.user_input = Entry(self,
                                bg="#5BC8AC",
                                bd=29,
                                insertwidth=4,
                                width=24,
                                font=("Verdana", 20, "bold"),
                                textvariable=self.UserIn,
                                justify=RIGHT)
        self.user_input.grid(columnspan=4)

        self.user_input.insert(0, "0")  #default value

        #this needs to be a god damn function

        self.button1 = makeNumberButton(self, 7, 2, 0)
        self.button2 = makeNumberButton(self, 8, 2, 1)
        self.button3 = makeNumberButton(self, 9, 2, 2)
        self.button4 = makeNumberButton(self, 4, 3, 0)
        self.button5 = makeNumberButton(self, 5, 3, 1)
        self.button6 = makeNumberButton(self, 6, 3, 2)
        self.button7 = makeNumberButton(self, 1, 4, 0)
        self.button8 = makeNumberButton(self, 2, 4, 1)
        self.button9 = makeNumberButton(self, 3, 4, 2)
        self.button10 = makeNumberButton(self, 0, 5, 0)

        self.buttonPlus = makeNumberButton(self, "+", 2, 3)
        self.buttonMinus = makeNumberButton(self, "-", 3, 3)
        self.buttonMultiply = makeNumberButton(self, "*", 4, 3)
        self.buttonDiv = makeNumberButton(self, "/", 5, 3)
        self.clearButton = Button(self,
                                  bg="#98DBC6",
                                  bd=12,
                                  text="AC",
                                  padx=7,
                                  pady=25,
                                  font=("Helvetica", 20, "bold"),
                                  width=28,
                                  command=lambda: self.clearDisplay())
        self.clearButton.grid(row=1, columnspan=4, sticky=W)

        self.buttonEval = Button(self,
                                 bg="#98DBC6",
                                 bd=12,
                                 text="=",
                                 padx=100,
                                 pady=25,
                                 font=("Helvetica", 20, "bold"),
                                 command=lambda: self.calculateTask())
        self.buttonEval.grid(row=5, column=1, sticky=W, columnspan=2)

    def buttonClick(self, number):
        self.task = str(self.task) + str(number)
        self.UserIn.set(self.task)

    def calculateTask(self):
        self.data = self.user_input.get()
        try:
            self.answer = eval(self.data)
            self.displayText(self.answer)
            self.task = self.answer
        except SyntaxError as e:
            self.displayText("Invalid input")
            self.task = ""

    def displayText(self, value):
        self.user_input.delete(0, END)
        self.user_input.insert(0, value)

    def clearDisplay(self):
        self.task = ""
        self.displayText("0")


if __name__ == "__main__":
    calculator = Tk()
    calculator.title("Calculator")
    app = CalculatorApplication(calculator)
    calculator.resizable(width=False, height=False)
    calculator.mainloop()
