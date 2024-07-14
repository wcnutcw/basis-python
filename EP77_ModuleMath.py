import math

z=abs(-50)
print(z)

p=pow(5,2)  # 5**2
print(p)


result = math.sqrt(64)
print(result)

result_1 = math.floor(80.4)   # .floor : ปัดเศษลง
print(result_1)

result_2 = math.ceil(80.4)   # .ceil: ปัดเศษขึ้น
print(result_2)

print(math.pi)

radian = math.radians(90)   # แปลง  degrees เป็น radians
print(math.sin(radian))

point1=[5,4]
point2=[5,13]

d=math.dist(point1,point2)      # คำนวณระยะทางจากจุด 1 ไป จุด 2
print(d)



# log

print(math.log10(1000))   # log ฐาน 10
print(math.log(math.exp(1)))     # log ฐาน e   # math.exp(1) คือ e ยกกำลัง 1

