# From Module : เอาคำสั่งเฉพาะบางส่วนใน module นำมาใช้งานได้เลย

from CalculateService_73 import addition  , pi  # from ชื่อไฟล์ import ชื่อฟังก์ชัน

addition(10,2,20)    # เรียกใช้ได้เลย ไม่ต้องมีชื่อไฟล์นำหน้า
print(pi)

from Weather_73 import *      # * คือนำคำสั่งทั้งหมดมาใช้งาน

print(city)
getWeather()
