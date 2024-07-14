# Global Variable / Local Variable  : ชื่อเหมือนกัน หรือ ต่างกันก็ได้ ในการเก็บค่าในตัวแปร แต่การใช้งานแตกต่างกัน

# global : ตัวแปรที่โปรแกรมหลัก ทำงานไปทั่ว ( x ข้างนอก function )
# local :  ตัวแปรที่โปรแกรมย่อย ทำงานในfunction ( x ข้างใน function )

# โปรแกรมย่อย
def displayNumber():
    x=10
    print("Hello = ",x,"ใน")


# โปรแกรมหลัก
x=20
displayNumber()
print("Hello = ",x,"นอก")
print(x) # 20
