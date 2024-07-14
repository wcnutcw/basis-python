weight =int(input("ป้อนน้ำหนัก(kg) :"))
height =int(input("ป้อนส่วนสูง(cm) : "))/100
bmi =weight/(height**2)
# print("BMI = ",weight/(height**2))

''' 
ิิBMI
<18.5 ผอม
18.5 - 22.9 = สมส่วน
23.0 - 24.9 = น้ำหนักเกิน
25.0 - 29.9 = โรคอ้วน ระดับที่ 1 
>30 = โรคอ้วนระดับอันตราย
'''

if bmi<18.5 and bmi>=0 and height>0:   
    result = "ผอม"             #เก็บข้อความไว้ในตัวแปร result 
elif bmi>=18.5 and bmi<=22.9  and height>0:
     result = "สมส่วน"
elif bmi>=23.0 and bmi<=24.9 and height>0 :
     result = "น้ำหนักเกิน"
elif bmi>=25.0 and bmi<=29.9 and height>0 :
     result = "โรคอ้วน ระดับที่ 1 "
elif bmi>30 and height>0 :
     result = "โรคอ้วนระดับอันตราย"
else:
    result = "ไม่ทราบค่าที่ชัดเจนโปรดป้อนข้อมูลอีกครั้ง" 

print("BMI =",bmi ,"\n""ผลการประเมิณ = ",result)

