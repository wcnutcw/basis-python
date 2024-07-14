# lambda function ( Anonymouse function ) : ฟังก์ชันที่สร้างขึ้นมาโดยไม่อยากระบุชื่อ

"""
lambda arguments : expression     # arguments คือค่าที่ส่งเข้ามาให้ parameter ทำงาน ในฟังก์ชัน

"""
 
x = lambda name:name   #  return name กลับมาให้ตัวแปร x

print(x("nut"))   # nut ส่งให้เข้าไปทำงาน ที่ arguments แล้ว return expression  ออกมาให้ตัวแปร x เก็บค่า 

summ = lambda x,y : x+y

print(summ(2,3))


def myPower(x):
    return lambda a: x**a

z = myPower(2)  # z มีคุณสมบัติแบบ lambda function  : z = lambda a: 2**a
result = z(4)  # z = lambda 4: 2**4    ,  result = 2**4

print(result)

