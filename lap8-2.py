def cal():
    r = int(tb1.get())
    circle = (22/7)*r*r
    messagebox.showinfo("พื้นที่วงกลม","ผลลัพธ์"+ str(circle))
    result.set(circle)
    
from tkinter import *
window = Tk()
window.geometry("800x500")
window.title("โดย ฟาอิซ มุคุระ")

result = StringVar()

lb = Label(window , text="ยินดีต้อนรับเข้าสู่ python", font=("FreesiaUPC",24))
lb.place(x=50, y=10)

lb2 = Label(window , text="รับค่ารัศมี", font=("FreesiaUPC",18))
lb2.place(x=50, y=100)

tb1 = Entry(window)
tb1.place(x=180, y=110, width=200, height=20)

lb3 = Label(window , text="ผลลัพธ์", font=("FreesiaUPC",18))
lb3.place(x=50, y=150)

tb2 = Entry(window, textvariable = result)
tb2.place(x=180, y=160, width=200, height=20)

btn = Button(window, text="คำนวณ", font=("FreesiaUPC",25), command=cal)
btn.place(x=400, y=110)

window.mainloop()




