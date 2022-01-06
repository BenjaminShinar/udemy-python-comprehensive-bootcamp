#cSpell:ignore padx,pady

from tkinter import *


def makeLabel(frame, txt, r, c):
    return Label(frame, font="Helvetica 12 bold", bg="light green",
                 text=txt).grid(row=r, column=c, sticky=W)


def makeVarLabel(frame, obj, r, c):
    return Label(frame,
                 font="Helvetica 12 bold",
                 bg="light green",
                 textvariable=obj).grid(row=r, column=c, sticky=E)


class LoanCalculator(Frame):

    def __init__(self, master):
        super(LoanCalculator, self).__init__(master)
        master.grid()
        self.create_widgets(master)

    def create_widgets(self, tk):
        self.ls = []
        self.ls.append(makeLabel(tk, "Annual Intrest Rate", 1, 1))
        self.ls.append(makeLabel(tk, "Number of Years", 2, 1))
        self.ls.append(makeLabel(tk, "Loan Amount", 3, 1))
        self.ls.append(makeLabel(tk, "Monthly Payment", 4, 1))
        self.ls.append(makeLabel(tk, "Total Payment", 5, 1))

        self.annualIntrestRateVar = StringVar()
        self.ls.append(
            Entry(tk, textvariable=self.annualIntrestRateVar,
                  justify=RIGHT).grid(row=1, column=2))
        self.numberOfYears = StringVar()
        self.ls.append(
            Entry(tk, textvariable=self.numberOfYears,
                  justify=RIGHT).grid(row=2, column=2))
        self.loanAmount = StringVar()
        self.ls.append(
            Entry(tk, textvariable=self.loanAmount,
                  justify=RIGHT).grid(row=3, column=2))
        self.monthlyPaymentVar = StringVar()
        self.ls.append(makeVarLabel(tk, self.monthlyPaymentVar, 4, 2))
        self.totalPaymentVar = StringVar()
        self.ls.append(makeVarLabel(tk, self.totalPaymentVar, 5, 2))

        self.ls.append(
            Button(tk,
                   text="Compute Payment",
                   bg="red",
                   fg="white",
                   font="Helvetica 14 bold",
                   command=self.compute).grid(row=6, column=2, sticky=E))
        self.ls.append(
            Button(tk,
                   text="Clear",
                   bg="blue",
                   fg="white",
                   font="Helvetica 14 bold",
                   command=self.clear_all).grid(row=6,
                                                column=8,
                                                padx=20,
                                                pady=20,
                                                sticky=E))

    def clear_all(self):
        self.numberOfYears.set("")
        self.loanAmount.set("")
        self.annualIntrestRateVar.set("")
        self.monthlyPaymentVar.set("")
        self.totalPaymentVar.set("")

    def compute(self):
        amount = float(self.loanAmount.get())
        rate = float(self.annualIntrestRateVar.get()) / 1200
        years = int(self.numberOfYears.get())
        total, monthly = self.computeMonthly(amount, rate, years)
        self.monthlyPaymentVar.set(format(monthly, "10.2f"))
        self.totalPaymentVar.set(format(total, "10.2f"))

    def computeMonthly(self, amount, rate, years):
        totalMonths = years * 12
        monthly = amount * rate / (1 - (1 / (1 + rate)**totalMonths))
        total = monthly * totalMonths
        return total, monthly


if __name__ == "__main__":
    calc = Tk()
    calc.title("Loan Calculator")
    calc.configure(background="light green")
    app = LoanCalculator(calc)
    calc.mainloop()
    calc.resizable(width=False, height=False)