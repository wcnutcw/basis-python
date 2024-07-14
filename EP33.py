# เลขคู่ , เลข

number=[] 
odd =[] #เลขคี่
even =[] #เลขคู่
while True:
    x= int(input("ป้อนตัวเลข :"))
    if x<0:
        break
    if x%2==0:
        even.append(x)
    else :
        odd.append(x)
    number.append(x) 

print("ตัวเลขทั้งหมด :",number)  
print("เลขคึ่ :",odd)  
print("เลขคู่ :",even)  