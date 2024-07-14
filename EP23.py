# break / continue

i=1 
while i<=10:
    print("รอบที่ =",i)
    if(i==5):                       #เมื่อ i = 5 ให้ออกจากลูปได้เลยโดยคำสั่ง break
        break
    i+=1
else :
    print("จบโปรแกรม")

x = 0

while x<=10:
    x+=1   
    if(x%2 !=0):                       #ถ้า x==5 คือ กระโดดข้ามเลข 5 จาก 4 ไป 6 เลย โดยคำสั่ง continue                                       
        continue                        #x%2 !=0 หมายถึง ถ้า xหารด้วย2 ไม่ลงตัว ก็คือเลขคี่   (!= คือ ไม่เท่ากับ )
    print("รอบที่ =",x)
else :
    print("จบโปรแกรม")


for i in range(1,12):   
    if(i==11):
        break
    if(i%2 ==0):
        continue
    print(i)
print("จบโปรแกรม")
   
