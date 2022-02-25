try:
    w = int (input("รับค่าน้ำหนัก "))
    h = int (input("รับค่าส่วนสูง "))
    bmi = (w/(h/100**2))
except:
    print("error")
    
else:
    print("คำตอบ",bmi)