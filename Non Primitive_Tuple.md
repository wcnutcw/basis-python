# List สามารถเปลี่ยนแปลงข้อมูลได้
# Tuple คล้ายๆกับ List แต่ไม่สามารถเปลี่ยนแปลงข้อมูลได้
Tuple สามารถนำไปประยุกต์ใช้กับ ID รหัสบัตรประชาชน

"เปรียบเทียบ tuple และ list"
tup =(1,2,3,4)  # tuple ใช้วงเล็บ ()  , list ใช้วงเล็บ[]
print(tup)
#>>>(1, 2, 3, 4, True, 3.14, 'Hello')


lis=[1,2,3,4]
print(lis)
#>>>[1, 2, 3, 4, True, 3.14, 'Hello']

print(type(tup)) #>>> <class 'tuple'>
print(type(lis)) #>>> <class 'list'>


# เขียนแบบ Constuctor : เรียกผ่านชื่อ class 
tup=tuple((1,2,3,4,True,3.14,"Hello"))
lis=list([1,2,3,4,True,3.14,"Hello"])

# เปลี่ยนสมาขิก
lis[0]="สวัสดีครับ"
print(lis)
#>>> ['สวัสดีครับ', 2, 3, 4, True, 3.14, 'Hello']
 
tup[0] = "สวัสดีครับ" # ไม่สามารถเปลี่ยนสมาชิกได้ มันจะขึ้น error



"การเข้าถึงข้อมูล"
print(tup[0:3])   # [ start : < end ]
#>>> (1, 2, 3)

# อยากจะแก้ไขข้อมูล แล้วให้กลับไปเป็น Tuple แบบเดิม
# แปลง Tuple เป็น list แล้วค่อยนำ List กลับเป็น Tuple

lis_new =list(tup)
lis_new[0]="สวัสดีครับ"
print(lis_new)   #>>> ['สวัสดีครับ', 2, 3, 4, True, 3.14, 'Hello']
tup = tuple(lis_new)
print(tup) #>>> ('สวัสดีครับ', 2, 3, 4, True, 3.14, 'Hello')


"การแสดงผลโดยใช้ loop"

for item in tup:
    print("สมาชิก =",item)

# สมาชิก = สวัสดีครับ
# สมาชิก = 2
# สมาชิก = 3
# สมาชิก = 4
# สมาชิก = True
# สมาชิก = 3.14
# สมาชิก = Hello


" ตรวจสอบข้อมูล "

if "ทุเรียน" in tup:
    print("เป็นสมาขิก")
else:
    print("ไม่เป็นสมาชิก")
# ไม่เป็นสมาชิก

" การนับจำนวนสมาชิก (len) "

tup = ('สวัสดีครับ', 2, 3, 4, True, 3.14, 'Hello')
print(len(tup))
# 7


" len and loop for"
for item_1 in range(len(tup)):   
    print(tup[item_1])   #tup[0] , tup[1] , ... ,tup[6]
# สวัสดีครับ
# 2
# 3
# 4
# True
# 3.14
# Hello

" การสร้าง tuple"
x=() 
x = tuple()  # เขียนแบบ constructor
print(x)
ิ่
# เพิ่มข้อมูลใน tuple

x = ("Hello")
print(type(x)) #<class 'str'>

x = ("Hello",)
print(type(x)) #<class 'tuple'>


" การเพิ่มข้อมูล หรือ รวมข้อมูล "

name = ("Hello","Jojo")
nick = ("nut",)
nick_2 =  "nack"
allGroup =()
name = name+nick + (nick_2,)
allGroup = name
print(allGroup) #>>> ('Hello', 'Jojo', 'nut', 'nack')
print(name) #>>> ('Hello', 'Jojo', 'nut', 'nack')


"การลบข้อมูล del : คือ ลบทั้งตัวแปรและสมาชิก"
del tup 
print(tup) 

" ลบสมาชิกใน tuple  โดยให้ลบแบบlist"
tup =(1,2,3,4,True,3.14,"Hello")
lis = list(tup)  # แปลงเป็น list
lis.pop()   # pop คือ ลบตัวสุดท้ายออก 
print(lis)   #[1, 2, 3, 4, True, 3.14]
lis.remove(2)    # ลบ 2 ออก 
print(lis) # [1, 3, 4, True, 3.14]
tup=tuple(lis)   # แปลงคืนเป็น Tuple
print(tup)  # (1, 3, 4, True, 3.14)


" การค้นหาและนับจำนวนสมาชิก  แบบ count"
tup =(1,2,3,4,True,3.14,"Hello",4,5,4)
x = tup.count(4)  # มี 4 กี่ตัว
print(x)  # มี 3 ตัว

" การค้นหาและนับจำนวนสมาชิก  แบบ index"
tup =(1,2,3,4,True,3.14,"Hello",4,5,4)
x = tup.index(4)  # มีเลข 4  กี่ตำแหน่ง
print(x)  # มี 3 ตำแหน่ง



" การ sort ข้อมูล  : เรียงข้อมูลจากน้อยไปมาก "
 Tuple ไม่มีฟังก์ชัน sort ให้ใช้งาน
 แต่ถ้าจะให้เรียงต้องแปลง เป็น list ก่อน

tup_1 =(1,12,3,8,100,50,3,-1,0,1,5,46)
lis_1 = list(tup_1)
lis_1.sort()
tup_1 = tuple(lis_1)
print(tup_1)

# >>> (-1, 0, 1, 1, 3, 3, 5, 8, 12, 46, 50, 100)