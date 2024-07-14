import os                # os ใช้ในการจัดการเกี่ยวกับ ตัวไฟล์   จึงต้องเรียก os มาใช้งาน โดยการ import

try :
    if os.path.exists("Score.txt"):     # os.path.exists("ชื่อไฟล์")  : ค้นหาไฟล์
        os.remove("Score.txt")     # os.remove("ชื่อไฟล์")   : ลบไฟล์ทิ้ง
        print("ลบแล้ว")
    else:
        print("ไม่พบไฟล์")

except Exception as e  : 
    print(e)


