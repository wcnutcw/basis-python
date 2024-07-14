# Module : โปรแกรมย่อย ( Sub program ) คือรวบรวมกลุ่มคำสั่งมาเขียนอีกไฟล์  

# แล้วโปรแกรมอื่นๆ สามารถเรียกใช้งานตามชื่อไฟล์ได้เลย ( สะดวกต่อการเรียกใช้งาน )


"""โปรแกรมหลัก : มีหน้าที่เรียกใช้ module"""  

import CalculateService_73 as cal,Weather_73  # CalculateService_73 คือ Module    # Weather_73  คือ Module


# สามาถเปลี่ยนชื่อเรียกใช้งานได้  : ชื่อไฟล์ as ชื่อที่ต้องการ เช่น CalculateService_73 as cal  ( เรียกใช้งานชื่อไฟล์โดยใช้ชื่อ cal )
# เรียกใช้   : ชื่อไฟล์.ชื่อฟังก์ชัน()

cal.addition(10,2,3)       
cal.subtraction(10,2,3)
print(cal.pi)

result = Weather_73.city["ชลบุรี"]
print(result)

Weather_73.getWeather()

cal.power(5,2)











