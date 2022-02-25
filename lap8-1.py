from tkinter import *
main = Tk()
main.geometry("500x400")
main.title("โดย ฟาอิซ มุคุระ") 
messagebox.showinfo("Hello","สวัสดีครับ")
messagebox.showwarning("เตือน","ตั้งใจเรียนด้วย")
messagebox.showerror("ผิดพลาด","โปรแกรม error")
messagebox.askquestion("confirm","คุณต้องการลบหรือไม่")
messagebox.askokcancel("confirm","คุณต้องการลบหรือไม่")
messagebox.askyesno("confirm","คุณต้องการลบหรือไม่")
messagebox.askretrycancel("confirm","คุณต้องการลบหรือไม่")

main.mainloop()