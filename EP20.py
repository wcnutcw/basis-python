# for loop คือทำซ้ำไปเรื่อยๆ ใช้เมื่อรู้จำนวนรอนที่ขัดเจน

"""
    for in range(start , stop , step) #กำหนด   #โดย stop จะสิ้นสุดที่ เลขก่อนถึง stop #step คือ ระบุว่าจะให้เพิ่มทีละเท่าไร

"""

for i in range(1,5,2):            #ค่าเริ่มต้นของการใช้ range เริ่มต้นที่ 1  ถึง 4 คือ สิ้นสุดที่ 5-1 โดยเพิ่มขึ้นทีละ 2 : 1  , 3 
    print("รอบที่ =",i,"Hello World")


summation = 0
for i in range(1,11):
    summation+=i
    print("รอบที่ =",i,"sum =",summation)
print("ผลรวม =",summation)
print("ค่าเฉลี่ย =",summation/i)