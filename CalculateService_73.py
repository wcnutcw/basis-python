
# ให้บริการค่าคงที่ / คำนวณเลข
pi = 3.14

def addition(*args):
    total=0
    for i in range(len(args)):
        total+=args[i]
    print("ผลบวก =",total)

def subtraction(*args):
    total=args[0]
    for i in range(1,len(args)):
        total-=args[i]
    print("ผลลบ =",total)   


def power(num1,m):
    print("ผลการยกกำลัง :",num1**m)
