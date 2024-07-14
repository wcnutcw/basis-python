 # ฟังก์ชัน เลขคู่ เลขคี่



def searchNumber(number):       # number of function is Parameter
    if number%2==0:
        print("เลขคู่")
    else:
        print("เลขคี่")

number=int(input("ป้อนเลขของคุณ :"))
searchNumber(number)    # number is Argument


