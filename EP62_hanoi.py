# Tower of hanoi

"""
n = จำนวนจาน
เสา =>> A,B,C

มีจานจำนวน 3 จาน
n=1   (n-1)
n=2   (n-1)
n=3   (จานใหญ่สุด)



"""

"""

A => 3 => C => ใหญ่ => จาน (เรียงจานจากใหญ่ไปเล็ก : ล่างขึ้นบน)
 
เสา B เป็นจุดพักจาน   ** จานเล็กอยู่บนจานใหญ้ได้ แต่ จานใหญ่อยู่บนจานเล็กไม่ได้

A => ล ก ญ  ( บน ลง ล่าง )
A (ล ก) => B ( ล ก)

A ญ => C ญ


=> C => ล ก ญ


"""
# มองเป็นก้อนใหญ่ ในการเขียนโปรแกรม ส่วนก้อนเล็กๆปล่อยให้โปรแกรมจัดเรียงการทำงานเอง


def hanoi(n,a,b,c):
    if(n==0):
        return
    hanoi(n-1,a,c,b) # ย้าย a(ล,ก) -> b  | c เป็นจุดพัก (จานใหญ่ที่สุด)  (ย้ายa ,พักc ,ไปb)
    print("จานที่ =",n,"จาก =",a,"ไป =",c)
    hanoi(n-1,b,a,c)


try :
    n= int(input("ป้อนจำนวนจาน :"))
    hanoi(n,"A","B","C")
except Exception as e:
        print(e)
