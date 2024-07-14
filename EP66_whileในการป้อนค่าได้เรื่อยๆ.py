# ใช้ While เพื่อให้ป้อนคำสั่งได้เรื่อยๆ 

while True:
    try :
        number1 = float(input("ป้อนตัวเลข 1 :"))
        number2 = float(input("ป้อนตัวเลข 2 :"))
        if number1==0 and number2 == 0:
            break                    # กระโดดออกจากลูป while
        result = number1/number2
        print(result)

    except ValueError:         
            print("กรุณาป้อนตัวเลข")                               
    except ZeroDivisionError:         
            print("ห้ามหารด้วยเลขศูนย์")                               
    finally :                         
            print("ทำงานต่อไป...")


