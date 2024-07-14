# โปรแกรม crack password : ไม่รู้รหัสผ่านเลยต้องการสุ่มหารหัสผ่าน ไปเรื่อยๆ จนเจอรหัสจริงๆ

import random

ATM_PASSWORD = "132"
result="" #เก็บผลลัพธ์



while result!=ATM_PASSWORD:
        result=""           # clear ค่า ถ้าเกิดมีการเริ่มต้น loop รอบใหม่
        for letter in range(len(ATM_PASSWORD)):
            list_number=random.choice("0123456789")
            result="".join(list_number)+str(result)     # .join : นำค่ามาต่อข้อความกัน ไปเก็บใน str result
            print("SEARCH :",result)

print("CRACK PASSWORD IS ",result)

