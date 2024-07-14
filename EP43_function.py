# function : โปรแกรมย่อย ที่อยู่ใน โปรแกรมหลัก   ( การทำงาน :  โปรแกรมหลัก >>> โปรแกรมย่อย  )
# function : รวมคำสั่งให้อยู่กลุ่มเดียวกัน เพื่อให้ใช้งานได้ง่าย และ ช่วยประหยัดพื้นที่ในหน่วยความจำ

# การสร้าง function / เรียก function
"""
    def ชื่อฟังก์ชัน():       ***ชื่อฟังก์ชันห้ามซ้ำกัน***
        statement


"""

# โปรแกรมย่อย

def sayHi():
    print("Hello World")

def sayThailand():
    print("สวัสดี")

def sayEngland():
    print("Hello")

def add():
    x=3+1
    print(x)
    
# โปรแกรมหลัก

sayHi()
sayThailand()
sayEngland()
add()