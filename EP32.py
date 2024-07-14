# รับและเรียงลำดับข้อมูลตัวเลข
number=[]
while True:
    x= int(input("ป้อนตัวเลข :"))
    if x<0:
        break
    number.append(x)                  # นำตัวเลขมาต่อท้าย

print("ก่อนเรียงตัวเลข :",number)
number.sort()               # sort คือ เรียงตัวเลขจาก น้อย ไป มาก
print("น้อยไปมาก :",number)
number.reverse()
print("มากไปน้อย :",number)  # reverse คือ เรียงตัวเลขจาก มาก ไป น้อย ( ให้ใช้คำสั่ง sort ก่อน !)
print("จบโปรแกรม")

print(number)
# หาผลรวม ค่ามาก ค่าน้อย โดยใช้ฟังก์ชัน
print("ค่าที่น้อยที่สุด :",min(number)) # ค่าน้อยที่สุด
print("ค่าที่มากที่สุด :",max(number)) # ค่ามากที่สุด
print("ผลรวมตัวเลข :",sum(number)) # หาผลรวม