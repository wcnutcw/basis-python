#หาเลขคู่ หรือ คี่

number = int(input("ป้อนตัวเลข : "))

if number%2 ==0: #ใช้modulus (%) คือ numberหาร2แล้วได้เศษ0    คือ หารเอาเศษ
    print("เป็นเลขคู๋")
else :
    print("เป็นเลขคี่")
    