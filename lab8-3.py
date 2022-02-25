def triangle():
    b = (base.get())
    h = (high.get())
    a = (1/2*b*h)
    messagebox.showinfo("พื้นที่สามเหลี่ยม","คำตอบ %.2f" % a)
    area.set(a)
    
from tkinter import *
main = Tk()
main.geometry("800x600")
main.title("โปรแกรมหาพื้นที่สี่เหลี่ยม โดย ธนวัตน์ แสงม่วง")
base = StringVar()
high = StringVar()
area = StringVar()

lb1 = Label(main, text="รับค่าฐาน:", font=("Tohoma",20) )
lb1.place(x=20, y=20)
tb1 = Entry(main, textvariable=base)
tb1.place(x=200, y=20, width=300, height=40)

lb2 = Label(main, text="รับค่าสูง:", font=("Tohoma",20) )
lb2.place(x=20, y=80)
tb2 = Entry(main, textvariable=high)
tb2.place(x=200, y=80, width=300, height=40)

btn = Button(main, text="คำนวณ", font=("Tohoma",20), command= triangle)
btn.place(x=200, y=150)

lb3 = Label(main, text="คำตอบ:", font=("Tohoma",20) )
lb3.place(x=20, y=250)

lb4 = Label(main, bg="#556699" , fg="#FFFFFF", font=("Tohoma",20), textvariable=area )
lb4.place(x=20, y=250)

main.mainloop()