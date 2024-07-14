"""

 Set : สมาขิกซ้ำกันไม่ได้ และ ไม่สามารถแก้ไขข้อมูลสมาชิกได้ถ้าสร้าง set แล้ว แต่เพิ่มได้  ( List[] , Tuple() : สมาชิกซ้ำกันได้ )
 Set เขียนในูป { }
 Set การเรียงลำดับไม่แน่นอน(ถ้าใส่ซ้ำจะนับแค่1ตัว)  ( List , Tuple : เรียงลำดับจากซ้ายไปขวา) ** ไม่สามารถแสดง index(ตำแหน่ง) ข้อมูลได้ **

"""

# แบบปกติ
fruit ={"มะขาม","มะม่วง","มะยม",50,True}
print(fruit)

# เขียนแบบ constructor
lis = ["ปลาดุก","ปลาหมอ"]
fish=set(lis)
print(fish)

เพิ่มข้อมูลสมาชิก โดยคำสั่ง add
fruit.add("ทุเรียน")
fruit.add(3.14)
print(fruit)

# เพิ่มข้อมูลสมาชิกหลายๆตัว พร้อมกัน
lis=["ตะไคร้","โหระพา","ชะอม"]
fruit.update(lis)          # update : เพิ่มและอัพเดตข้อมูลในคราวเดียวกันพร้อมกัน  
# fruit.update(["ตะไคร้","โหระพา","ชะอม"]) 
print(fruit)

#Loop
for item in fruit:
    print("ข้อมูล :",item)

"แสดงจำนวนสมาขิกใน set"

print(len(fruit))   # {True, 3.14, 'มะขาม', 'มะยม', 'โหระพา', 'ทุเรียน', 50, 'ชะอม', 'ตะไคร้', 'มะม่วง'}
# 10 ตัว

# check สมาชิก
if "มะเฟือง" in fruit:
    print("มี")
else:
    print("ไม่มี")


print("มะม่วง" in fruit)

"ลบสมาชิกใน set ใช้ remove , discard"
fruit.remove("ทุเรียน")
print(fruit)   # {True, 3.14, 'มะม่วง', 'ชะอม', 'ตะไคร้', 50, 'มะขาม', 'มะยม', 'โหระพา'}

fruit.discard("มะปราง")  # discard คือ จะลบเมื่อมีสมาชิกใน set จริงๆ ( ถ้าไม่มีโปรแกรมก็จะไม่ขึ้น error ยังรันได้ต่อ แนะนำให้ใช้!!!)
print(fruit)  # {True, 3.14, 'ชะอม', 'ตะไคร้', 'มะม่วง', 'โหระพา', 'มะขาม', 50, 'มะยม'}

# del : ลบสมาชิก ลบตัวแปร (เคลียmemory)
del fruit
print(fruit)

" Opearator "
1)union

fruitA={"กล้วย","ผลไม้","มะนาว"}
fruitB={"สตอว์เบอรี่","กีวี","มะม่วง"}

allFruit=fruitA.union(fruitB)
print(allFruit) 
#{'กล้วย', 'มะนาว', 'กีวี', 'มะม่วง', 'สตอว์เบอรี่', 'ผลไม้'}

# หรือใช้คำสั่ง update ในการต่อสมาชิก
fruitA.update(fruitB)
print(fruitA)
#{'สตอว์เบอรี่', 'มะม่วง', 'กล้วย', 'มะนาว', 'กีวี', 'ผลไม้'}

# copy สมาชิก
fruitC=fruitA.copy()
print(fruitC)
# {'สตอว์เบอรี่', 'กีวี', 'ผลไม้', 'มะม่วง', 'กล้วย', 'มะนาว'}

2) difference  : A - B คือ อยู่ใน A ไม่อยู่ใน B 

fruitD=fruitA.difference(fruitB)   # A - B คือ อยู่ใน A ไม่อยู่ใน B
print(fruitD) # {'มะนาว'}

3) intersection : สมาชิกซ้ำกัน
fruitA={"กล้วย","ผลไม้","มะนาว"}
fruitB={"สตอว์เบอรี่","กีวี","มะม่วง","ผลไม้","กล้วย"}
fruitE = fruitA.intersection(fruitB)
print(fruitE) # {'กล้วย', 'ผลไม้'}



# ไม่ต้องสร้างตัวแปรเพิ่ม โดยใส่ _update
fruitA={"กล้วย","ผลไม้","มะนาว"}
fruitB={"สตอว์เบอรี่","กีวี","มะม่วง","ผลไม้","กล้วย"}
fruitA.difference_update(fruitB)
print(fruitA)  # {'มะนาว'}


4) subset : A subse B คือ สมาชิก A อยู่ในสมาชิก B ทั้งหมด
# subset : ใช้คำสั่ง .issubset()

fish ={"ปลาดุก","ปลาหมอ","ปลาวาฬ","ปลาโลมา"}
x = {"ปลาหมอ","ปลาดุก"}

print(x.issubset(fish)) # True

# superset คือ set หลัก 
#  .issuperset() คือเช็คว่า set ใหญ่ มีสมาชิกทั้งหมด ของ set ย่อยมั้ย
print(fish.issuperset(x)) # True


# min , max ใน set
number ={1,2,5,9,-1,41,400,100,9,-10,500}
print(min(number)) # -10
print(max(number)) # 500


" Frozen set " 
# Frozen set : ไม่สามารถ ลบ เพิ่มข้อมูล แก้ไข ได้เลย (แตกต่างจาก set ที่สามารถใช้คำสั่งเพิ่มได้)
# Froen set เหมาะสำหรับข้อมูลที่อยากให้คงที่เสมอ!!!

fruit=frozenset(["มะม่วง","มะยม","มะนาว","มะปราง"])
print(fruit) # ถ้าใช้คำสั่ง เพิ่ม ลบ หรือ แก้ไขข้อมูล โปรแกรมจะ error ไม่รันโค้ดต่อ

#สามารถแสดงข้อมูลเป็น loop ได้
for item in fruit:
    print("ข้อมูล =",item)
#ข้อมูล = มะปราง
#ข้อมูล = มะยม
#ข้อมูล = มะม่วง
#ข้อมูล = มะนาว
