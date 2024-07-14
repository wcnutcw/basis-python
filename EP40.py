# Tuple คล้ายๆกับ List แต่ไม่สามารถเปลี่ยนแปลงข้อมูลได้

tup =(1,2,3,4,True,3.14,"Hello")  # tuple ใช้วงเล็บ ()  , list ใช้วงเล็บ[]
print(tup)

lis=[1,2,3,4,True,3.14,"Hello"]
print(lis)

print(type(tup))
print(type(lis))

# เขียนแบบ Constuctor : เรียกผ่านชื่อ class 
tup=tuple((1,2,3,4,True,3.14,"Hello"))
lis=list([1,2,3,4,True,3.14,"Hello"])

lis[0]="สวัสดีครับ"
print(lis)


# การเข้าถึงข้อมูล
print(tup[0:3])

# อยากจะแก้ไขข้อมูล แล้วให้กลับไปเป็น Tuple แบบเดิม
# แปลง Tuple เป็น list แล้วค่อยนำ List กลับเป็น Tuple

lis_new =list(tup)
lis_new[0]="สวัสดีครับ"
print(lis_new)
tup = tuple(lis_new)
print(tup)


# การแสดงผลโดยใช้ loop 

for item in tup:
    print("สมาชิก =",item)

if "ทุเรียน" in tup:
    print("เป็นสมาขิก")
else:
    print("ไม่เป็นสมาชิก")

print(len(tup))

for item_1 in range(len(tup)):   
    print(tup[item_1])   #tup[0] , tup[1] , ... ,tup[6]

" การสร้าง tuple"

x=()
x = tuple()
print(x)

x = ("Hello")
print(type(x))

x = ("Hello",)
print(type(x))


" การเพิ่มข้อมูล "

name = ("Hello","Jojo")
nick = ("nut",)
nick_2 =  "nack"
allGroup =()
name = name+nick + (nick_2,)
allGroup = name
print(allGroup)
print(name)


" ลบสมาชิกใน tuple  โดยให้ลบแบบlist"
tup =(1,2,3,4,True,3.14,"Hello")
lis = list(tup)
lis.pop()
print(lis)
lis.remove(2)
print(lis)
tup=tuple(lis)
print(tup)


" การค้นหาและนับจำนวนสมาชิก  แบบ count"
tup =(1,2,3,4,True,3.14,"Hello",4,5,4)
x = tup.count(4)  # มี 4 กี่ตัว
print(x)  # มี 3 ตัว

" การค้นหาและนับจำนวนสมาชิก  แบบ index"
tup =(1,2,3,4,True,3.14,"Hello",4,5,4)
x = tup.index(4)  # มีเลข 4  กี่ตำแหน่ง
print(x)  # มี 3 ตำแหน่ง

" การ sort ข้อมูล  : เรียงข้อมูลจากน้อยไปมาก "
tup_1 =(1,12,3,8,100,50,3,-1,0,1,5,46)
lis_1 = list(tup_1)
lis_1.sort()
tup_1 = tuple(lis_1)
print(tup_1)

# >>> (-1, 0, 1, 1, 3, 3, 5, 8, 12, 46, 50, 100)



