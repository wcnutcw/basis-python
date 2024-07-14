# รับค่าเข้ามาที่ fuction

def myData(a,b,c):   # a,b,c คือ Parameter
    print("ชื่อ =",a,"นามสกุล =",b,"อายุ =",c)


myData("Nut","Chs",21)
fname = "Kong"
lname = "Sawadde"
age = 21
myData(fname,lname,age)  # fname , lname , age คือ Argument

# Argument / Parameter

# Argument :  ค่าที่ส่งเข้าไปใน function  
# Parameter :  ค่าตัวแปรที่รับข้อมูลที่ส่งมาทำงาน โดยส่งมาจาก Argument 


def addition(a,b):
    print(a+b)

addition(5,9)
