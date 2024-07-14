#โครงสร้างควบคุม (Control Structure)
# 1. แบบลำดับ(+ - * / %)  2. แบบเลือก(if) 3. แบบทำซ้ำ(for)

'''
if boolean expression :
    statement
if จริง :
    ทำอะไร
elif จริง :
    ทำอะไร
else :
    ทำอะไร

'''

age =  int(input("ป้อนอายุของคุณ :")) # str convert to int
if age>=15 and age<20:   #and คือให้เชื่อมข้อมูลทั้งสองฝั่งโดย จริง และ(and) จริง เป็นจริง ก็จะทำให้มันเข้าเงื่อนไขใน if นั้นๆ
    print("วัยรุ่น") 
elif age>=20 and age<30:           #elif คือเจอเงื่อนที่เป็นจริงแล้วให้จบโปรแกรมเลย
    print("วัยผู้ใหญ่")
elif  age>=30 and age<=60:
    print("วัยทำงาน")
elif age>61:
    print("วัยชรา")
else :
    print("วัยเด็ก")
print("จบโปรแกรม")

#Ternary Operator คือการลดรูป if 
# "เงื่อนไขเป็นจริง" if expression "เงื่อนไขอื่นๆ 

number =  int(input("ป้อนเลขของคุณ : "))
print("ผิดแล้วจ้า") if number>=15  else print("ถูกแล้วจ้า")
print("จบโปรแกรม")
