# ฟังก์ชันการสุ่ม

import random



for i in range(3):
    x=random.random()   # .random() : สุ่มในช่วง 0.0 - 1.0
    print(x)



for i in range(3):
    x=random.uniform(5,10)   # .uniform()  : กำหนดช่วงตัวเลขที่ต้องการสุ่ม   =>  5<=x<10
    print(x)

for i in range(3):
    x=random.randrange(1,10,1)   # .randomrange(start , stop , step)  : กำหนดช่วงและสามารถกำหนดได้ว่าจะเพิ่มทีละเท่าไร แบบจำนวนเต็มเท่านั้น
    print(x)                     # range  : แสดงความเป็นจำนวนเต็มเสมอ

for i in range(3):
    x=random.randint(1,10)   # .randint : สุ่มแบบเลขจำนวนเต็ม โดยนับตัวสุดท้ายด้วย
    print(x)             



item=[1,2,3,4,5,"A","B","C"]
for i in range(3):
    x=random.choice(item)     # .choice : สุ่มหยิบใน list ที่สร้างขึ้นมา
    print(x)          


item=[1,2,3,4,5,"A","B","C"]
for i in range(3):
    random.shuffle(item)    # .shuffle : สุ่มหยิบใน list ที่สร้างขึ้นมา และ สลับตำแหน่งสมาชิกในlist ( ทำงานที่ตัวแปรเก็บข้อมูล )
    print(item)       


# ลดรูป choice
for i in range(3):
    x=random.choice([1,2,3,4,5,"A","B","C"])     
    print(x)          
    

for i in range(3):
    x=random.choice("123ABCD")      # สุุ่มหยิบ string ทีละตำแหน่งของข้อความ
    print(x)          

