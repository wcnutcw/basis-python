#ป้อนตัวเลขหาผลรวมตัวเลข

summation= 0

# while summation<100:       #ถ้า summation <100 ยังสามารถป้อนเลขได้ ถ้ามากกว่า100 จะออกจากลูป
#     number=int(input("ป้อนตัวเลขของคุณ :"))
#     summation+=number
#     print("ผลรวม =",summation)

while True:           #True หมายถึง เป็นจริงตลอด ไม่จำกัดว่าถึงตัวไหน
     number_1=int(input("ป้อนตัวเลขของคุณ :"))
     summation+=number_1
     if summation>=100:         #ผลรวมมากกว่า= 100 ให้ออกจาก loop เลย
        break
print("ผลรวม =",summation)