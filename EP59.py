# ฟังก์ชันหาผลรวม / ค่าเฉลี่ยตัวเลข

Round = int(input("ป้อนจำนวนลำดับที่ต้องการบวกเลข :"))
aray_number=[]

def array(Round):
    k=0
    while k<Round:
        number = float(input("ป้อนเลข :"))
        aray_number.append(number)
        k+=1
    print("ตัวเลขทั้งหมด :",aray_number)
    return aray_number

a = array(Round)

def summation(num):
    total=0
    for i in num:
        total+=i    
    avg = total/len(num)
    return total,avg

summ,avgg= summation(a)
print("ผลรวมตัวเลข :",summ)
print("ค่าเฉลี่ย :",avgg)




