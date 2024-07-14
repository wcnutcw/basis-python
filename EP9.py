#โปรแกรมคำนวณค่า BMI (ดัชนีมวลกาย)
# BMI = น้ำหนัก(kg) / ส่วนสูง * ส่วนสูง(m)


#input / convert to integer
weight = int(input("ป้อนน้ำหนักของคุณ(kg): "))
height = int(input("ป้อนส่วนสูงของคุณ(cm): "))

#process
height/=100 #height =  height/100           
bmi = weight/(height**2) #height*height

#output
print("BMI : ",bmi)