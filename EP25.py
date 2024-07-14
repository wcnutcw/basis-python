# ค้นหาตัวเลขมากสุด / น้อยสุด

maximum , minimum = 0,9999

while True:
    number = int(input("ป้อนตัวเลขของคุณ :"))
    if number<0:       #กระโดดออกจากloop
        break
    if number>maximum:     #เก็บค่ามากสุด
        maximum=number
    if number<minimum:     #เก็บค่าน้อยสุด
        minimum=number

print("ค่าสูงสุด :",maximum)
print("ค่าต่ำสุด :",minimum)

