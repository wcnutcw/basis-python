# Recurive Function : เรียกฟังก์ชันตัวเอง

def a():
    print("A")
    a()        # Recurive Function  : คล้ายๆกับทำ loop ในฟังก์ชัน ไม่มีที่สิ้นสุด ต้องเขียนคำสั่งให้หาจุดออกจากลูป

def b():
    print("B")



"""
หาจุดวนซ้ำ
หาจุดออกจาก function ( return )
ต้องมี parameter

"""

def c():
    i=1
    print(i)
    i+=1   # เปลี่ยนเป็นเลช 2
    c()    # reset กลายเป็น เลข 1 เหมือนเดิม


def addNumber(number):
    if number==5:
        return      # number = 5 ออกจากฟังก์ชัน
    print(number)   # 0
    number+=1        # 1
    addNumber(number)    # number = 1 วนไปข้างบนต่อแล้วลงล่างเรื่อยๆ



addNumber(0)


def summation(number):
    if number==1:
        return number
    else:
        return number+summation(number-1) 


x=summation(5)
print(x)


"""
5
5 + summation(4)
5 + 4 + summation(3)
5 + 4 + 3 + summation(2)
5 + 4 + 3 + 2 + summation(1)
5 + 4 + 3 + 2 + 1
= 15


"""
