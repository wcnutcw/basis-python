#STRING

name = " HeLLO " #index คือ โดยค่าเริ่มต้นคือ0  =ตัวH (คัวแรก)
name_1 = "HELLO : 40"

print(name[0:5])   
# 0:5 หมยถึง 0ถึง5 ตั้งแต่ตัวที่ H ถึง L หรือ :5 ความหมายเดียวกัน หรือ 0: ความหมายเดียวกัน  (ไม่นับตัวสุดท้าย มองเป็นเครื่องหมาย <5)
print(name[:5])
print(name[0:])

print("อายุเท่าไร :",name_1[-2:])  #-2คือตัวสุดท้ายคือ 4 


#lenคือบอกความยาว โดยถ้ามีช่องว่างก็จะนับด้วย
# strip function : ลบช่องว่างซ้ายขวา
# เช่น name = name.strip()
# ลบช่องว่างด้านซ้าย  l: name=name.lstrip()
# ลบช่องว่างด้ายขวา  r: name=name.rstrip()

# ตัวพิมพ์ใหญ่
# name.upper()
# ตัวพิมเล็กทั้งหมด
# name.lower()
# ตัวขึ้นต้นประโยคให้เป็นตัวพิมพ์ใหญ่ตัวเดียว
# name.capitalize()

# replace  คือแทนที่ตัวอักษร
# name.replace("ตัวที่ต้องการแทนที่","แทนที่คำด้วย")

print(len(name)) 

name = name.strip()
print(len(name))

print(name.upper())
print(name.lower())
print(name.capitalize())

print(name.replace("He","40"))

name_2 ="HELLO 4 IN 4 WHY 4"

#มี4ซ้ำต้องการเปลี่ยนเลข 4 ตามตำแหน่ง

print(name_2.replace("4","3.5",1))
print(name_2.replace("4","3.5",2))
print(name_2.replace("4","3.5",3))

#1 คือ 4 ตัวแรก

#2 คือ 4ตัวที่1 และ 2

#3 คือ 4ตัวที่ 1 และ 2 และ 3

a ="สวัสดีครับ"
x = "สวัสดี" in a
print(x) 
z = "สวัสดี" not in a #จาก true เป็น false
print(z)
y = "วอท" in a
print(y)

if x:
    a = a.replace("สวัสดี","วอท")
print(a)

fname = "nut"
lname = "chs"
age ="21"
Fullname = fname + lname +age
print(Fullname)
print("ชื่อต้น :"+fname+"\tนามสกุล :"+lname+"\tอายุ :"+age)

text = "ชื่อต้น :{}\tนามสกุล :{}\tอายุ :{}"
print(text.format(fname,lname,age))

text = "ชื่อต้น :{1}\tนามสกุล :{3}\tอายุ :{0}\tอาชีพ :{2}"
print(text.format(fname,lname,age,"โปรแกรมเมอร์"))

value = 1204.1645486
text = "ชื่อต้น :{}\tนามสกุล :{}\tอายุ :{}\tอาชีพ :{}\tเงินเดือน :{:.2f}" #.2f คือ ทศนิยม2ตำแหน่ง

print(text.format(fname,lname,age,"โปรแกรมเมอร์",value))

fruit = "ทุเรียน มังคุด แตงโม ส้มโอ ทุเรียน"
print(fruit.count("ทุเรียน"))

Cha = "นายดีมีสุข"
print(Cha.startswith("นาย"))
print(Cha.endswith("สุข"))

count = "925031"
if count.endswith("1"):
    print("ถูก")
else:
    print("ไม่รู้สิ")