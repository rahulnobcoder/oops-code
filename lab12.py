from tkinter import *
def gpa():
    if name_tf.get()=='' or roll_tf.get()=='' or reg_no_tf.get()=='':
        return
    cs1grade=credit(grade1_tf.get())
    cs2grade=credit(grade2_tf.get())
    ma1grade=credit(grade3_tf.get())
    ec1grade=credit(grade4_tf.get())
    gpa=(cs1grade*4+cs2grade*4+ma1grade*3+ec1grade*4)/15


    gpa=Label(root,text=gpa,bg="white")
    credit1=Label(root,text=cs1grade*4,bg="white")
    credit2=Label(root,text=cs2grade*4,bg="white")
    credit3=Label(root,text=ma1grade*3,bg="white")
    credit4=Label(root,text=ec1grade*4,bg="white")
    totalc=Label(root,text=(cs1grade*4+cs2grade*4+ma1grade*3+ec1grade*4),bg="white")


    gpa.grid(row=9,column=5)
    credit1.grid(row=4,column=5)
    credit2.grid(row=5,column=5)
    credit3.grid(row=6,column=5)
    credit4.grid(row=7,column=5)
    totalc.grid(row=8,column=5)

def credit(s):
    if s=="s"or s=="S":
        return 10
    elif s=="a" or s=="A":   
        return 9
    elif s=="b" or s=="B":   
        return 8  
    elif s=="c" or s=="C":   
        return 7
    elif s=="d" or s=="D":   
        return 6  
    elif s=="e" or s=="E":   
        return 5      
    else:
        return 0                         


root=Tk()
root.title("MARKSHEET")
root.geometry("700x400")
root.configure(background='light grey')

#labels
name = Label(root, text='Name' ,bg="light grey")
roll = Label(root, text='Roll.No' ,bg="light grey")
srl = Label(root, text='Srl.No' ,bg="light grey")
subj= Label(root, text='Subject' ,bg="light grey")
grade = Label(root, text='    Grade   ' ,bg="light grey")
sub_cred= Label(root, text='Sub Credit' ,bg="light grey")
creditobtained = Label(root, text='Credit Obtained' ,bg="light grey")
reg_no=Label(root,text="Reg.No",bg="light grey")
srl1=Label(root,text="1",bg="light grey")
srl2=Label(root,text="2",bg="light grey")
srl3=Label(root,text="3",bg="light grey")
srl4=Label(root,text="4",bg="light grey")
sub1=Label(root,text="CS 201",bg="light grey")
sub2=Label(root,text="CS 202",bg="light grey")
sub3=Label(root,text="MA 201",bg="light grey")
sub4=Label(root,text="EC 201",bg="light grey")
subc1=Label(root,text="4",bg="light grey")
subc2=Label(root,text="4",bg="light grey")
subc3=Label(root,text="3",bg="light grey")
subc4=Label(root,text="4",bg="light grey")
total_credit=Label(root,text="Total credit",bg="light grey")
sgpa=Label(root,text="SGPA",bg="light grey")

#buttons
submit = Button(root, text='submit',font="Calibri 9 bold",bg="green",command=gpa)

#entries
name_tf = Entry(root)
roll_tf = Entry(root)
grade1_tf=Entry(root)
grade2_tf=Entry(root)
grade3_tf=Entry(root)
grade4_tf=Entry(root)
reg_no_tf=Entry(root)



roll.grid(row=2, column=1,pady=0.5)
name.grid(row=1, column=1,pady=0.5)
srl.grid(row=3, column=1,pady=0.5)
subj.grid(row=3, column=2,pady=0.5)
grade.grid(row=3, column=3,pady=0.5)
sub_cred.grid(row=3, column=4,pady=0.5)
creditobtained.grid(row=3, column=5,pady=0.5)
reg_no.grid(row=1,column=4,pady=0.5)
srl1.grid(row=4,column=1,pady=0.5)
srl2.grid(row=5,column=1,pady=0.5)
srl3.grid(row=6,column=1,pady=0.5)
srl4.grid(row=7,column=1,pady=0.5)
sub1.grid(row=4,column=2,pady=0.5)
sub2.grid(row=5,column=2,pady=0.5)
sub3.grid(row=6,column=2,pady=0.5)
sub4.grid(row=7,column=2,pady=0.5)
subc1.grid(row=4,column=4,pady=0.5)
subc2.grid(row=5,column=4,pady=0.5)
subc3.grid(row=6,column=4,pady=0.5)
subc4.grid(row=7,column=4,pady=0.5)
total_credit.grid(row=8,column=4,pady=0.5)
sgpa.grid(row=9,column=4,pady=0.5)


submit.grid(row=9,column=2,pady=0.5)


name_tf.grid(row=1, column=2,pady=1)
roll_tf.grid(row=2, column=2,pady=1)
reg_no_tf.grid(row=1, column=5,pady=1)
grade1_tf.grid(row=4,column=3,pady=1)
grade2_tf.grid(row=5,column=3,pady=1)
grade3_tf.grid(row=6,column=3,pady=1)
grade4_tf.grid(row=7,column=3,pady=1)




root.mainloop()
