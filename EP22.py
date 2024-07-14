# แม่สูตรคูณ

start = int(input("ป้อนแม่สูตรคูณตัวเริ่มต้น ="))
stop =  int(input("ป้อนแม่สูตรคูณตัวสุดท้าย ="))

for x in range(start,stop+1):
    print("แม่สูตรคูณ :",x)
    for y in range(1,13):
        print(x,"x",y,"=",x*y)