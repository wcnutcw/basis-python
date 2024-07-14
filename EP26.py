# ตัวเลขขั้นบันได

"""
input = 6
1
12
1213
123456
"""

#มีจำนวนรอบทีชัดเจนควรใช้ for 

last = int(input("ป้อนตัวเลข :"))

for row in range(1,last+1):
    for column in range(1,row+1):
        print(column,end='')      #end คือคำสั่งแสดงแบบแถว
    print("")    #ขึนบรรทัดใหม่เมื่อจบ loop ข้างใน column

"""
input = 3

row = 1,3

row = 1
column = 1,2
1

row = 2
column = 1,3
12

row = 3
column = 1,4
123

"""




