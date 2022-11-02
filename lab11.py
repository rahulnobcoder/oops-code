from tkinter import *
def bmicalc():
    wei = float(weight_tf.get())
    hei = float(height_tf.get())
    if hei == 0:
        return

    bmi_val = wei/(hei*hei)
    bmi = Label(frame, text='YOUR BMI', bg="light yellow")
    bmi.grid(row=3, column=1)

    bmivalLabel = Label(frame, text=bmi_val,font="Calibri 9 bold", bg="white")
    bmivalLabel.grid(row=3, column=2)


root = Tk()
root.title("BMI CALCULATOR")
root.geometry("500x200")
root.configure(background='light blue')

frame = Frame(root, bg="light yellow", borderwidth=6)
frame.pack(expand=True)

height = Label(frame, text='HEIGHT(IN METER)',font="Calibri 9 bold" ,padx=11, bg="light yellow")
height.grid(row=1, column=1)

height_tf = Entry(frame)
height_tf.grid(row=1, column=2, pady=10)

weight = Label(frame, text='WEIGHT(IN KG)',font="Calibri 9 bold", bg="light yellow")
weight.grid(row=2, column=1)

weight_tf = Entry(frame)
weight_tf.grid(row=2, column=2, pady=10)

frame3 = Frame(frame)
frame3.grid(row=5, columnspan=3, pady=10)

cal_btn = Button(frame3, text='Calculate',font="Calibri 9 bold",command=bmicalc,bg="light green")
cal_btn.pack()


root.mainloop()
