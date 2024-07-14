#สร้างภาพวาด 4 เหลี่ยมจตุรัส

"""
2x2
xx
xx

3x3
xxx
xxx
xxx

"""

number=int(input("ป้อนขนาด ="))  

for row  in range(number):              # ถ้าป้อนเลข5 =>> 0,1,2,3,4  ทำ5รอบ
    for column in range(number):
        print("X",end='')           #end คือ เรียงตัวxเป็นแถว 5 ตัว
    print("")               #ขึ้นบรรทัดใหม่