# ฟังก์ชันการบวกเลข

def add(x,y):   
    print(x+y)


add(20,30)


# *args  : ใช้ Argument หลายๆตัว ไม่จำกัด (สามารถเปลี่ยนชื่อได้)

def sum(*args):  # (*ชื่อตัวแปร) : ใช้ Argument หลายๆตัว ไม่จำกัด
    summa=0
    for i in range(len(args)):
        summa+=args[i]
    print(summa)        # ค่าที่อยู่ใน args เป็นแบบ tuple

sum(10,20)
sum(10,20,30)
