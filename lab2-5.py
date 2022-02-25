midterm = int(input("กลางเทอม:"))
fanal = int(input("เทอมสุดท้าย:"))
hw = int(input("การบ้าน:"))
x = (midterm*40/100) + (fanal*50/100) + (hw*10/100) 
print("คะแนนรวม", x)
if x >=90 and x <= 100 :
    print("เกรดA")
elif x >=85 and x <=90 :
    print("เกรดB+")
elif x >=80 and x <=85 :
    print("เกรดB")
elif x >=70 and x <=80 :
    print("เกรดC+")
elif x >=60 and x <=70 :
    print("เกรดC")
elif x >=55 and x <=60 :
    print("เกรดD+")
elif x >=50 and x <=55 :
    print("เกรดD")
elif x >=0 and x <=49 :
    print("เกรดF")