; การเข้าถึงตัวอักษรใน String
len function : บอกความยาว รวมช่องว่างด้วย

strip function : ลบช่องว่างซ้ายขวา
เช่น name = name.strip()
ลบช่องว่างด้านซ้าย  l: name=name.lstrip()
ลบช่องว่างด้ายขวา  r: name=name.rstrip()

ตัวพิมพ์ใหญ่
name.upper()
ตัวพิมเล็กทั้งหมด
name.lower()
ตัวขึ้นต้นประโยคให้เป็นตัวพิมพ์ใหญ่ตัวเดียว
name.capitalize()

replace  คือแทนที่ตัวอักษร
name.replace("ตัวที่ต้องการแทนที่","แทนที่คำด้วย")

name_2 ="HELLO 4 IN 4 WHY 4"

#มี4ซ้ำต้องการเปลี่ยนเลข 4 ตามตำแหน่ง

print(name_2.replace("4","3.5",1))
print(name_2.replace("4","3.5",2))
print(name_2.replace("4","3.5",3))

#1 คือ 4 ตัวแรก

#2 คือ 4ตัวที่1 และ 2

#3 คือ 4ตัวที่ 1 และ 2 และ 3


การเช็คข้อความ => true of false
a ="สวัสดีครับ"
x = "สวัสดี" in name
print(x)   # =>> true
z = "สวัสดี" not in a #จาก true เป็น false
print(z)
y = "วอท" in a
print(y)  # =>> false

การต่อ String (Concatinate)  โดย +
fname = "nut"
lname = "chs"
age ="21"
Fullname = fname + lname +age
print(Fullname)
# =>> nutchs21
print("ชื่อต้น :"+fname+"\tนามสกุล :"+lname+"\tอายุ :"+age)
#=>> ชื่อต้น :nut    นามสกุล :chs    อายุ :21

format คือคำสั่ง ระบุบล็อคที่ได้กำหนดไว้คือ{}
#ต้องใส่ให้ครบที่กำหนด{}ไว้ 
text = "ชื่อต้น :{}\tนามสกุล :{}\tอายุ :{}"
print(text.format(fname,lname,age))
#โดยเริ่มตำแหน่งที่ 0 ถึง 2  
#คือ fname คือตำแหน่งที่ 0่
#จบที่ age คือตำแหน่งที่2

#ถ้ามีการระบุตำแหน่งให้ใช้ format
text = "ชื่อต้น :{1}\tนามสกุล :{3}\tอายุ :{0}\tอาชีพ :{2}"
print(text.format(fname,lname,age,"โปรแกรมเมอร์"))
#=>> ชื่อต้น :chs    นามสกุล :โปรแกรมเมอร์   อายุ :nut       อาชีพ :21

value = 1204.1645486
text = "ชื่อต้น :{}\tนามสกุล :{}\tอายุ :{}\tอาชีพ :{}\tเงินเดือน :{:.2f}" #.2f คือ ทศนิยม2ตำแหน่ง

print(text.format(fname,lname,age,"โปรแกรมเมอร์",value))
#=>> ชื่อต้น :nut    นามสกุล :chs    อายุ :21        อาชีพ :โปรแกรมเมอร์     เงินเดือน :1204.16

นับจำนวนคำในประโยค(count)
fruit = "ทุเรียน มังคุด แตงโม ส้มโอ ทุเรียน"
print(fruit.count("ทุเรียน"))
#=>> 2

เช็คคำขึ้นต้น : startswith
 และ 
 คำลงท้าย   : endswith
 =>> true or false
Cha = "นายดีมีสุข"
print(Cha.startswith("นาย"))
# True
Cha = "นายดีมีสุข"
print(Cha.startswith("นาย"))
print(Cha.endswith("สุข"))
# True



# .zfill(len) เติม 0 ข้างหน้า str

a="90"
print(a.zfill(4))   # 0090   ( len=4 คือ ความยาว str ไม่เท่ากับ4 จะเติม 0 ไว้ข้างหน้า)


# % format
firstname = 'Rukpong'
beverage = 'coffee'
drink_time = 2
money = 45
print('My name is %s. I like a %s and drink it %s time(s) a day.' % (firstname, beverage, drink_time))
# >>> My name is Rukpong. I like a coffee and drink it 2 time(s) a day.


# str.format
firstname = 'Rukpong'
beverage = 'coffee'
drink_time = 2
money = 45
result_message = 'My name is {}. I like a {} and drink it {} time(s) a day.'.format(firstname, beverage, drink_time)
print(result_message)
# >>> My name is Rukpong. I like a coffee and drink it 2 time(s) a day.

 # f. string
firstname = 'Rukpong'
beverage = 'coffee'
drink_time = 2
money = 45
print(f'My name is {firstname}. I like a {beverage} and drink it {drink_time} time(s) a day. The {beverage} is {money} Baht. I\'m spend {money * 2} Baht per a day.')
 # My name is Rukpong. I like a coffee and drink it 2 time(s) a day. The coffee is 45 Baht. I'm spend 90 Baht per a day.


 # เพิ่มความยาวของข้อความ
 print(f"=={'HEADER':10}==")   # :10 ถ้าข้อความยังไม่ครบ10ลำดับ จะเพิ่มช่องว่างจนครบ
print(f"=={123:10}==")
print(f"=={'OutputFilePython':10}==")
# ==HEADER    ==
# ==       123==
# ==OutputFilePython==

# end =""  : เรียงต่อข้อความ
for i in range(3):
    x=0
    print(x,end="")   # 000

# จัด alignment ของข้อความ
^ หมายถึง กึ่งกลาง

< หมายถึง ชิดซ้าย

> หมายถึง ชิดขวา

print(f"=={'HEADER':^10}==")   # : สัญลักษณ์และอักษรมีกี่ลำดับ
print(f"=={123:<10}==")


**สามารถใส่ character อื่น ๆ ใน space ที่ว่างจากการระบุจำนวน character ได้
print(f"=={'HEADER':=^10}==")
print(f"=={123:$>10}==")
# >>> ====HEADER====
# >>> ==$$$$$$$123==

**สามารถเพิ่มตัวเลข 0 ให้กับค่าตัวเลขได้ (ใช้ร่วมกับค่าตัวเลขเท่านั้น ไม่สามารถใช้กับ string ได้)
print(f'{7:05}')    # ถ้าตัวเลขไม่ครบ5ตัว จะเพิ่ม0ให้ครบ 5 ตัว  # >> 00005
print(f'{9:010}')
print(f'{9:<010}')
print(f'{9:^010}')


**สามารถเพิ่มเครื่องหมาย + ให้กับค่าตัวเลข
print(f'{7:+}')
print(f'{-7:-}')
print(f'{-7: }')
print(f'{7: }')
print(f'{7:+05}')


** สามารถระบุจำนวนทศนิยมได้
print(f'{3:f}')            # 3.000000
print(f'{3.1415926535:.2f}')    # 3.14
print(f'{3.1415926535:08.2f}')   # 00003.14


**สามารถแทรกเครื่องหมาย , หรือ _ ระหว่างตัวเลขได้ (ระหว่างตัวเลข 3 หลัก)
print(f'{1234567890:,}')    # 1,234,567,890
print(f'{12345.67890:,.2f}')  # 12,345.68
print(f'{7000000000:_}')     # 7_000_000_000


# สามารถใช้กับ datetime ได้ โดยระบุ datetime format ลงไปใน f-Strings
from datetime import datetime
now = datetime.now()
print(f'{now:%d %b %Y} - {now:%H:%M:%S}')    # 07 May 2024 - 10:52:32


# .isdigit() : เช็คว่ามีตัวเลขในข้อความมั้ย


# .title() : แปลงเป็นตัวพิมพ์ใหญ่เฉพาะตัวหน้าของคำเท่านั้น (ตัวแรกของทุกๆคำในประโยค)
def demo_title():
 s = "the land of smiles"
 print(s.title())
demo_title()
#==============================================================
The Land Of Smiles    # เฉพาะตัวแรกของคำเท่านั้นที่เป็นตัวพิมพ์ใหญ่ 
[Finished in 0.1s]




