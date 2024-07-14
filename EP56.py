# Fibonacci Number

"""

0,1,1,2,3,5,8,13,...
# เริ่ม จาก 2 ลำดับแรก

"""

x = int(input("ป้อนเลขว่าต้องการกี่ลำดับ :"))

def Fibonacci(number):
    if number<=1:
        return number
    else :
        return Fibonacci(number-2)+Fibonacci(number-1)



Fibonacci_Num=[]
for i in range(x):
    Fibonacci_Num.append(Fibonacci(i))


Fibonacci_Num=tuple(Fibonacci_Num)
print(Fibonacci_Num)
