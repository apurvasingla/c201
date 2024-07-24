from tkinter import *
window=Tk()



window.title('BMI Calculator')
window.geometry("380x400")
window.configure(bg='lightcyan')

def calculate_interst():
    p=float(principle.get())
    r=float(rate_of_interst.get())
    t=float(time.get())
    i=(p*r*t)/100
    interest = round(i,2)

    show_label.destroy()
    message=Label(result_frame,text=" interest on it "+str(p)+"at rate of interest"+str(r)+"N"+str(t)+"years is"+str(interest),
                   bg = "lightcyan", font=("Calibri", 12), width=42) 
    message.place(x=20,y=40) 
    message.pack()



app_label = Label(window, text="SIMPLE INTERST GUI", fg = "black", bg = "lightcyan", font=("Calibri", 20),bd=5)
app_label.place(x=50, y=20)

principle = Label(window, text="Your Name", fg = "black", bg = "lightcyan", font=("Calibri", 12),bd=1)
principle.place(x=20, y=90)

principle = Entry(window, text="", bd=2, width=22)
principle.place(x=150, y=92)

rate_of_interst = Label(window , text="rate of interst" , fg = "black",bg = "lightcyan",font= ("Calibri",12),bd =1)
rate_of_interst.place(x=20,y=140)
rate_of_interst = Entry(window,text="",bd=2,width=22)
rate_of_interst.place(x=150 ,y=142)

time = Label(window , text="time" , fg = "black",bg = "lightcyan",font= ("Calibri",12),bd =1)
time.place(x=20,y=185)
time= Entry(window,text="",bd=2,width=22)
time.place(x=150 ,y=187)

calculate_button=Button(window,text="CALCULATE",fg = "black", bg = "cyan",bd=4,command=calculate_interst)
calculate_button.place(x=20,y=250)

result_frame = LabelFrame(window,text="Result", bg = "lightcyan", font=("Calibri", 12)) 
result_frame.pack(padx=20, pady=20) 
result_frame.place(x=20,y=300) 

show_label=Label(result_frame,text=" ", bg = "lightcyan", font=("Calibri", 12), width=33) 
show_label.place(x=20,y=20) 
show_label.pack()
window.mainloop()

