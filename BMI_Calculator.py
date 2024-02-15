from tkinter import*
from tkinter import messagebox

class BMI_Calculator:

    def __init__(self, root):
        self.root=root
        self.root.title("BMI Calculator")
        self.root.geometry("320x120+0+0")

        frame1=Frame(self.root)
        frame1.grid()

        frame2=Frame(frame1, width=320, height=120, padx=20, relief=RIDGE)
        frame2.grid(row=0, column=0)

        frame3=Frame(frame1, width=320, height=120, padx=20, relief=RIDGE)
        frame3.grid(row=1, column=0)

        FirstNum=StringVar()
        SecondNum=StringVar()
        Result=StringVar()

        self.lblFirstNum=Label(frame2, text='Your Height (in meters)')
        self.lblFirstNum.grid(row=0, column=0)
        self.txtFirstNum=Entry(frame2, textvariable=FirstNum)
        self.txtFirstNum.grid(row=0, column=1)

        self.lblSecondNum=Label(frame2, text='Your Weight (in kgs)')
        self.lblSecondNum.grid(row=1, column=0)
        self.txtSecondNum=Entry(frame2, textvariable=SecondNum)
        self.txtSecondNum.grid(row=1, column=1)

        self.lblResult=Label(frame2, text='BMI')
        self.lblResult.grid(row=2, column=0)
        self.txtResult=Entry(frame2, textvariable=Result)
        self.txtResult.grid(row=2, column=1)

        def calc():
            f=float(FirstNum.get())
            s=float(SecondNum.get())
            r=(s/f**2)
            Result.set(r)
            
            if 18.5<=r<=24.9:
             messagebox.showinfo('BMI Calculator', 'You are at a healthy weight.')
            elif r<18.5:
             messagebox.showwarning('BMI Calculator', 'You are underweight.')
            elif 24.9<r<30:
             messagebox.showwarning('BMI Calculator', 'You are overweight.')
            elif r>=30:
             messagebox.showwarning('BMI Calculator', 'You are obese.')

        def reset():
            FirstNum.set("")
            SecondNum.set("")
            Result.set("")
            
        self.btnCalc=Button(frame3, text="Calculate", command=calc).grid(row=0, column=0)
        self.btnReset=Button(frame3, text="Reset", command=reset).grid(row=0, column=1)

if __name__ =='__main__':
    root=Tk()
    obj=BMI_Calculator(root)
    root.mainloop()
