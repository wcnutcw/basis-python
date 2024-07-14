# function return ค่า

"""
1. ไม่มีการรับค่าและส่งค่า
def name():

2. มีการรับค่าเข้าไปทำงาน
def name(a,b):

3. มีการรับค่าเข้าไปทำงาน และส่งออกมา : ใช้ return ( โยนค่าออกมาจาก function นำมาใช้ต่อ )
def name(a,b):
    return    

4. ไม่มีการรับค่า แต่ส่งค่าออกไป   : ใช้ return ( โยนค่าออกมาจาก function นำมาใช้ต่อ )

def name():
    return

"""


def add(a,b):
    return a+b


x=add(10,20)
print(x)


def showNumber():
    return 500

y =showNumber()
print(y)    


def randomNumber(x):
    if x=="100":
        print("ถูกหวย")
        return 1000
    else :
        print("ไม่ถูกหวย") 
        return 0

money =  randomNumber("100")   # return ออกมา เก็บในตัวแปร money
z =300
result = money -z
print("เงินรางวัล =",money,"เงินคงเหลือ",result)



# ให้ Return ทำงานแบบ break คือ โดดออกจาก function

def exam(x):
    if len(x)<3:  # น้อยกว่า3หลัก
        return
    if x=="100":
        print("ถูกหวย")
        return 1000 
    else :
        print("ไม่ถูกหวย") 
        return 0


a=exam("50")  # เลข 2 หลัก
print(a)    # None




    

