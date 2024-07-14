# ฟังก์ชัน เรียก ฟังก์ชัน

def CompareMax(x,y):
    if x>y:
        return x
    else:
        return y

def eual(x,y,z):
    return CompareMax(CompareMax(x,y),z)
    # a=CompareMax(x,y)   #20
    # m=CompareMax(a,z)   #20,30
    # return m            # 30

Max = eual(10,20,30)
print("ค่ามากสุด =",Max)





