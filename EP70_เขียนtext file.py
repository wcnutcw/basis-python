
try :
    fw = open("Score.txt","w",encoding = "utf-8")     # "w"  : สร้างไฟล์เปล่าและพร้อมกับเขียนข้อความภายในไฟล์   # "x" : สร้างไฟล์เปล่า
    fw.write("Hello World\n")                     # .write  : เขียนข้อความ =>> Hello world ขึ้นในไฟล์ Score.txt    # .write ใชแล้วต่อไปใช้ .writelines
    fw.writelines("สวัสดีชาวโลก")             #  .writelines : ข้อความยาวๆ เขียนทีละบรรทัด
    fw.close()                                      # .close : เมื่อดำเนินการกับตัวไฟล์เสร็จต้องปิดทุกครั้ง
except FileNotFoundError:    
    print("หาไฟล์ไม่เจอ")



try : 
    fr = open("Score.txt","r",encoding = "utf-8")
    line = fr.readlines()   # .readlines : อ่านทีละบรรทัด    # .readline : อ่านทีละบรรทัด ดึงมาทีละตัวอักษร   # **  แสดงเฉพาะภาษาอังกฤษ **
    for x in line:    # line => 0,1 มี 2 บรรทัด
        print("=>",x)

    fa = open("Score.txt","a",encoding = "utf-8")               # "a" (append)  : ต่อข้อความ คือ ข้อความใหม่ที่เพิ่มเข้ามา ไปต่อข้อมูลเก่า
    fa.writelines("\nสวัสดีวันปีใหม่\n")                             #  แต่ "w" จะไม่นำมาต่อ คือ ข้อความใหม่ไปแทนที่ข้อความเก่า
    for i in range(5):
        name = input("ป้อนข้อความ :")
        fa.writelines(name+"\n")   


    fr.close()
    
except :
    print("หาไฟล์ไม่เจอ")
    