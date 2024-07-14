# ลดรูป exception
# จำรายชื่อ exception ไม่ได้ ใช้ Exception

try :
    number1 = float(input("ป้อนตัวเลข 1 :"))
    number2 = float(input("ป้อนตัวเลข 2 :"))
    result = number1/number2
    print(result)

except Exception as e:         # Exception : ข้อมูลชื่อที่ error ทั้งหมด พร้อมบอกวิธีการแก้ไข
    print(e)                   # Exception as e คือ เปลี่ยนชื่อ เป็น e
else :                         # ถ้าไม่มีข้อผิดพลาด ก็ทำงานต่อที่ else 
    print("จบโปรแกรม")         # else จะไม่ทำงานเมื่อมีข้อผิดพลาดเกิดขึ้น 
