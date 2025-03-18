from tkinter import *
def mtokm():
    m=float(mil.get())
    km=m*1.609
    mk.config(text=f"{km}")


w=Tk()
w.title("miles to km converter")
w.config(padx=20,pady=20)

mil=Entry(width=7,)
mil.grid(column=1 ,row=0)

ml=Label(text="Miles")
ml.grid(column=2 ,row=0 )

e=Label(text="is equal to")
e.grid(column=0 ,row=1 )

mk=Label(text="0")
mk.grid(column= 1,row=1 )

mmk=Label(text="KM")
mmk.grid(column=2 ,row=1 )

cal=Button(text="calculate",command=mtokm)
cal.grid(column=1 ,row=2)

w.mainloop()