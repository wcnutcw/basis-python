x = 10
y = 3.99
z = "10"
result1 = x + y #บวกเลขกันโดยต้องมีชนิดข้อมูล(tyle)แบบเดียวกัน
print(result1) # 10 + 3.99 = 13.99

#แปลง string เป็น int โดยใช้ int()
result2 = x + int(z)
print(result2) #10 + 10 = 20

#แปลง int เป็น string โดยใช้ str()
result3 = str(x) +  z #ไม่ได้มีการคำนวณทางคณิตศาสตร์ แต่ เป็นการเรียงข้อความ
print(result3) # จะได้ 1010

# แปลง string เป็น float(ทศนิยม) โดยใช้ float()
result4 = x + float(z)
print(result4) # 10 + 10.0 = 20.0

#แปลง float เป็น string โดยใช้ str()
result5 = str(y) + z #เป็นการเรียงข้อความ
print(result5) #จะได้ 3.9910

#แปลง int เป็น float โดยใช้ float()
result6 = float(x) #มีทศนิยมต่อท้าย
print(result6) #จะได้ 10.0

#แปลง float เป็น int โดยใช้ int()
result7 = int(y) #ตัดทศนิยมออก
print(result7)  #จะได้ 3

#เปลี่ยนชนิดข้อมูล แปลงเป็นถาวรโดย ตัวแปร = คำสั่งเปลี่ยน(ตัวแปร)
#ตย. จาก y =3.99 ที่เป็น float เป็น string 
y = str(y)
print(type(y))