from tkinter import *
show=Tk()

show.title("BMI by MrMeje")
show.geometry("600x400")
show.configure(background="Aqua")

#BMI=kg/(mxm)

def solutoin():
    kg = float(txtweight.get())
    m = float(txthieght.get())/100 #m=cm/100[convert to meater]
    f = kg/(m * m)
    if f<18:
        txtbmistatus.configure(text="Underweight")
    elif f>=18 and f<25:
         txtbmistatus.configure(text="Normal weight")
    elif f>=25 and f<30:
         txtbmistatus.configure(text="Overweight")
    elif f>=30:
         txtbmistatus.configure(text="Obese")
    else:
         txtbmistatus.configure(text="Unclassified")
    txtbmi.configure(text=round(f, 2))

lblweight= Label(show, text= "Enter weight:", bg="skyblue")
lblweight.grid (row=0 , column=0)
txtweight= Entry(show , width= 30)
txtweight.grid(row=0, column=1)

lblkg= Label(show, text= "Kg" ,bg="red")
lblkg.grid(row=0, column= 2)

lblhieght= Label(show, text="Enter hiegt:", bg="skyblue")
lblhieght.grid(row=1 , column=0)
txthieght=Entry(show , width=30)
txthieght.grid(row=1 , column=1)

lblcm= Label(show, text="cm", bg="red")
lblcm.grid(row=1, column=2)

lblgender= Label(show, text="Enter Gender:", bg="skyblue")
lblgender.grid(row=2 , column=0)
txtgender=Entry(show , width=30)
txtgender.grid(row=2 , column=1)

lblage= Label(show, text="Age:", bg="skyblue")
lblage.grid(row=3, column=0)
txtage= Entry(show, width=30)
txtage.grid(row=3, column=1)

button_BMI=Button(show, text="Total BMI", bg="green" , width=10 , command=solutoin)
button_BMI.grid(row=4, column=1)

#function for the clear button
def clear():
    txtweight.delete(0,END)
    txthieght.delete(0,END)
    txtbmi.delete(0,END)


button_clear=Button(show, text="Clear", bg="Orange" , width=10 , command=clear)
button_clear.grid(row=4, column=2)


button_Exit=Button(show, text="Exit", bg="crimson" , width=10, command=show.destroy)
button_Exit.grid(row=4, column=3)


lblbmi= Label(show, text="your BMI:", bg="skyblue")
lblbmi.grid(row=5 , column=0)
txtbmi=Label(show , width=30)
txtbmi.grid(row=5 , column=1)

#BMI STATUS
lblbmistatus= Label(show, text="your BMI status:", bg="skyblue")
lblbmistatus.grid(row=6 , column=0)
txtbmistatus=Label(show , width=30)
txtbmistatus.grid(row=6 , column=1)



show.mainloop()

