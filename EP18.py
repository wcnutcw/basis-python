#แปลงอุณหภูมิ

temp = input("ป้อนอุณหภมิ (องศา) :") #ตย.45C
 
degree = float((temp[:-1].strip())) #ตย.ไม่ให้เลือกตัวสุดท้าย ได้ 45
unit = str(temp[-1].upper().strip()) #ตย.ได้ C

unit_1 = input("หน่วยที่คุณต้องการแปลง (C,F,R,K):")
unit_1 = unit_1.upper().strip()
if unit=="C":
    if unit_1=="F":
        result =(9*degree)/5 +32
        unit_result = "F"
        text = "{:.3f}\t{}"
        print(text.format(result,unit_result))
    elif unit_1=="R":
        result = 5*degree/4
        unit_result = "R"
        text = "{:.3f}\t{}"
        print(text.format(result,unit_result))
    elif unit_1=="K":
        result = degree +273
        unit_result = "K"
        text = "{:.3f}\t{}"
        print(text.format(result,unit_result))
    elif unit_1=="C":
        print(degree,unit)
elif unit=="F":
    if unit_1=="C":
        result = (degree-32)*5/9
        unit_result = "C"
        text = "{:.2f}\t{}"
        print(text.format(result,unit_result))
    elif unit_1=="R":
        result = (degree-32)*4/9
        unit_result = "R"
        text = "{:.2f}\t{}"
        print(text.format(result,unit_result))
    elif unit_1=="K":
        result = (degree-32)*5/9 + 273
        unit_result = "K"
        text = "{:.2f}\t{}"
        print(text.format(result,unit_result))
    elif unit_1=="F":
        print(degree,unit)
elif unit=="R":
    if unit_1=="C":
        result = degree*5/4
        unit_result = "C"
        text = "{:.2f}\t{}"
        print(text.format(result,unit_result))
    elif unit_1=="F":
        result = degree*9/4 +32
        unit_result = "F"
        text = "{:.2f}\t{}"
        print(text.format(result,unit_result))
    elif unit_1=="K":
        result = degree*5/4 +273
        unit_result = "K"
        text = "{:.2f}\t{}"
        print(text.format(result,unit_result))
    elif unit_1=="R":
        print(degree,unit)
elif unit=="K":
    if unit_1=="C":
        result = degree-273
        unit_result = "C"
        text = "{:.2f}\t{}"
        print(text.format(result,unit_result))
    elif unit_1=="F":
        result = (degree-273)*9/5 +32
        unit_result = "F"
        text = "{:.2f}\t{}"
        print(text.format(result,unit_result))
    elif unit_1=="R":
        result = (degree-273)*4/5
        unit_result = "R"
        text = "{:.2f}\t{}"
        print(text.format(result,unit_result))
    elif unit_1=="K":
        print(degree,unit)
elif unit:
    print("กรุณาใส่หน่วยองศาด้วย")
elif unit_1:
    print("กรุณาใส่หน่วยองศาให้ถูกต้อง(C,F,R,K)")
else: 
    print("ไม่ทราบค่าที่แน่ชัดโปรดป้อนข้อมูลใหม่ให้ถูกต้อง")

