# สร้างขอบตาราง 
# ให้ x เป็นขอบตาราง


number = int(input("ป้อนขนาด :"))
for row in range(number):
    for column in range(number):
        if row==0 or row ==number-1 or column==0 or column==number-1:    # number - 1 คือ ตัวสุดท้าย ใน range
            print("x",end="")
        else:
            print(" ",end="")
    print(" ")