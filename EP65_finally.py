# finally : ถึงแม้โปรแกรมจะมี ปัญหา ก็ยังคงทำงานเมื่อเดิม ( นำไปประยุกต์ใช้ได้หลายอย่างเพื่อให้โปรแกรมยังคงทำงานต่อไปได้ )

# else : จะไม่แสดงในส่วน else เมื่อมีข้อผิดพลาดเกิดขึ้น


try :
    number1 = float(input("ป้อนตัวเลข 1 :"))
    number2 = float(input("ป้อนตัวเลข 2 :"))
    result = number1/number2
    print(result)

except Exception as e:         
    print(e)                   
finally :                         
        print("ทำงานต่อไป")         

