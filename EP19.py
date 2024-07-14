#โครงสร้างควบคุมแบบทำซ้ำ

# while ครบเงื่อนไข จะออกจากลูป (เมื่อเงื่อนไขเป็นเท็จจะออกจากลูปทันที)
'''
 while expression :
        statement
 '''

# i = 1 #ตัวนับจำนวนรอบ

# while i<=3:
#     print("รอบที่ :",i)
#     i=i+1 # ถ้า i=4 จะออกจากลูป
# print("จบโปรแกรม")


#หาผลรวมตัวเลข โดยใช้ While loop

i=1 #เริ่มต้นที่1
summation = 0 #เก็บผลการบวกเลขตามจำนวนรวม
average = 0 #ผลรวมหารด้วยจำนวนรอบ
count = int(input("ระบุจำนวนรอบ :"))

while i<=count:
    summation+=i #summation = summation + i คือเก็บผลรวมของi ในแต่ละรอบ
    print("รอบที่ i =",i,"ค่าsum =",summation)
    i+=1 # i = i+1 เพิ่มทีละ1
print("ผลรวมการบวกเลข =",summation) #summation ตัวสุดท้ายที่ได้ ก่อนออกจากลูป   

average = summation/count
print("ค่าเฉลี่ย = ",summation/10)

