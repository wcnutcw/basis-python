# Raise Exception  : สร้าง exception ขึ้นมาเอง ( กำหนดเงื่อนไขเอง )


while True:
    try :
        name = str(input("ป้อนชื่อผู้ใช้โปรแกรม :"))
        if name == "nut":
            raise Exception("มีชื่อในระบบนี้แล้ว")                  # ส่งไปทำงานที่ except 
            
        number1 = float(input("ป้อนตัวเลข 1 :"))
        number2 = float(input("ป้อนตัวเลข 2 :"))
        if number1==0 and number2 == 0:
            break      
        if number1<0 or number2<0:
            raise Exception("ไม่สามารถป้อนค่าติดลบได้")           # ส่งไปทำงานที่ except

        result = number1/number2
        print(result)

    except Exception as e:         
            print(e)           
    finally :                         
            print("ทำงานต่อไป...")

print("จบการทำงานจ้า")