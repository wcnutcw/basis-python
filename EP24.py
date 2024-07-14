#ป้อนตัวเลขหาผลรวมตัวเลข

start , stop =1,5
summation,avg = 0,0

while(start<=stop):       #ทำงาน 5 รอบ start = 1 จนถึง stop = 5
    number=int(input("ป้อนตัวเลขของคุณ :"))
    summation+=number
    start+=1

avg = summation/stop
print("ผลรวม =",summation)
print("ค่าเฉลี่ย =",avg)