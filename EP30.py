# เกมทายลูกเต๋า
# 1 to 6 ( ทายถูกหรือผิด )

#โดยใช้คำสั่ง random

import random
#สุ่มเลขลูกเต๋า
myrandom = random.randrange(1,7)  # 1-6
print(myrandom)
correct = False
print("คุณมีโอกาสตอบ 3 ครั้ง \n")
k = 0
while k<3:              #มีโอกาสตอบ 3ครั้ง นับ 0 ถึง 2
    number = int(input("ป้อนคำตอบของคุณ ="))
    correct = (number==myrandom) # True / false
    if not correct:
        if(number>myrandom):
            print("ค่าน้อยกว่านี้นะ")
        if(number<myrandom):
           print("ค่ามากกว่านี้นะ") 
    if correct :
        print("ถูกต้อง")
        break
    k+=1

if not correct:             # correct เป็น False   
        print("เสียใจด้วยคุณตอบผิด")
        print("เฉลย =",myrandom)