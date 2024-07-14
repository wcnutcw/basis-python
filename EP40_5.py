# นำค่าใน tuple ไปใส่ในตัวแปร

tup=(10,20,30)
a,b,c=tup
print(a)
print(b)
print(c)
d=a+c
print(d)

# การสลับ tuple

x=(50,60)
y=(70,80)

x,y = y,x  # ดูจาก ขวาไปซ้าย แต่ละคู่  : y >> x , x >> y
print(x) # >> (70, 80)
print(y) # >> (50, 60)

# tuple >> string

charactor = ('k','o','n','g')
name = "".join(charactor)   # join คือ รวมตัวอักษร เข้าด้วยกัน   ( "". คือบอกว่าเป็น string)
print(name) # kong


# reverse tuple : หลังไปหน้า
z = (10,20,30,40,50,60,70,80)
w = tuple(reversed(z))   # reversed : เรียงจากหลังไปหน้า
print(w) # แสดงเป็น tuple
# >>> (80, 70, 60, 50, 40, 30, 20, 10)


# string  >>> tuple แบบ reverse
e = "HelloMyfriend"
e_1 = tuple(reversed(e)) 
print(e_1)
# >>> ('d', 'n', 'e', 'i', 'r', 'f', 'y', 'M', 'o', 'l', 'l', 'e', 'H')