
""" Module ที่มากับ python """
# Module Date/Time

import datetime

result=datetime.datetime.now()   # ดึงวันและเวลาปัจจุบัน มาใช้งาน
print(result)       # ปี-เดือน-วัน-เวลา 
print(result.year)    # .year : เอาแค่ปี
print(result.month)    # .month : เอาแค่เดือน
print(result.day)      # .day : เอาแค่วัน


newdate = datetime.datetime(2020,6,20,15)      # กำหนด ปี-เดือน-วัน-เวลา เอง
print(newdate)    # 2020-06-20 15:00:00


# รูปแบบการแสดงผล : จัดรูปแบบเอง
# คำสั่ง : ชื่อตัวแปร.strftime()   ในการจัดรูปแบบเอง

# note : รูปแบบเต็มจะเป็นตัวอักษรใหญ่ , รูปแบบสั้นจะเป็นตัวอักษรเล็ก

print("เริ่มต้น :",result)   
print(result.strftime("%x"))    # %x : แสดงในรูปแบบสั้น คือ วัน/เดือน/ปี =>> 04/29/24
print(result.strftime("%X"))    # %X : แสดงเวลา => 23:02:54
print(result.strftime("%c"))    # %c : แสดงในรูปแบบยาว คือ ชื่อวัน ชื่อเดือน วันที่ เวลา  ปี => Mon Apr 29 23:03:34 2024

print(result.strftime("%H"))    # %H : แสดงเวลาที่เป็นชั่วโมงอย่างเดียว => 23
print(result.strftime("%M"))    # %M : แสดงเวลาที่เป็นนาทีอย่างเดียว => 06
print(result.strftime("%S"))    # %S : แสดงเวลาที่เป็นวินาทีอย่างเดียว => 36
print(result.strftime("%p"))    # %p : แสดง PM หรือ AM      => PM

print(result.strftime("%H : %M : %S : %p"))   # นำชั่วโมง นาที วินาทีและช่วงเวลามาต่อกัน  =>> 23 : 09 : 47 : PM



# %j : แสดงวันที่เราอยู่ว่าอยู่ในลำดับใดใน 1 ปี 
print(result.strftime("%j"))  # 120  ( ลำดับที่ 120 หรือ จากวันที่1 มกรา เราผ่านมาแล้ว 120วัน )

# %a : บอกชื่อวัน ในรูปแบบสั้น
print(result.strftime("%a"))   # Mon

#  %a : บอกชื่อวัน ในรูปแบบเต็ม
print(result.strftime("%A"))  # Monday

# เช็คว่าวันที่ 20/6/2020 เป็นวันอะไร จากคำสั่ง newdate = datetime.datetime(2020,6,20,15)     
# ชื่อตัวแปร.strftime(%a)
print(newdate.strftime("%a"))   # Sat


print(result.strftime("%w"))    # %w : เช็คว่าจาก sunday=0 ถึง saturday=6  ในวันที่เราอยู่กำลังอยู่ในลำดับไหนของ1week => 1


print(result.strftime("%d"))    # %d : แสดงวันที่ => 29
print(result.strftime("%b"))    # %b : แสดงเดือน แบบสั้น => Apr
print(result.strftime("%B"))    # %B : แสดงเดือน แบบเต็ม => April
print(result.strftime("%y"))    # %y : แสดงปี แบบสั้น => 24
print(result.strftime("%Y"))    # %Y : แสดงปี แบบเต็ม => 2024

print(result.strftime("%m"))    # %m : แสดงลำดับเลขเดือน  => 04

print(result.strftime("Day %d on %A month  %B year %Y"))   # Day 29 on Monday month  April year 2024  ( ไม่รองรับภาษาไทย )


# ว/ด/ป
print(result.strftime("%d/%m/%Y"))   # 29/04/2024