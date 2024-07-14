# Primitive  : จับคู่แบบ 1:1 คือ ตัวแปร 1 ตัว เก็บได้แค่ตัวเดียว
"""
Booleans >>> True , False
String
Number >>> Integer , Float , Complex
Bytes

"""



# Non Primitive(ประหยัดพื้นที่ความจำ!) โดยนมีการนำ Primitive ไปใช้ด้วย    : จับคู่ได้หลายตัวแปร  เป็นกลุ่ม คือ ตัวแปร 1 ตัว เก็บได้หลายค่า
"""
List
Tuple
Dict
Set >>> Frozen

"""


# List : นำข้อมูลมาเรียงต่อกัน ข้อมูลภายใน list เรียกว่า สมาขิก ( แบบ เรื่องset )




##เขียนแบบ non primitive : list
number =[] # list ว่าง
number_1 = [1,2,3,4,5,6] # list มีสมาชิก 1 to 6
name_1 = ["A","B","C"] # list name มีสมาชิก A B C
all = [10 , "A",True , 3.14 , 10 ] # list เก็บแบบผสมได้ ทั้ง String Boolean integer

name = list(["A","B","C"]) # เขียนแบบ construtor

#แสดงผล
print(name)
print(all)
print(number_1)

# การเข้าถึง ข้อมูล list    
# เริ่มต้นทาง ซ้ายไปขวา โดย เริ่มลำดับที่  0 ,1  , 2 ,...
# เริ่มต้นทาง ขวาไปซ้าย โดย เริ่มลำดับที่ -1,-2,-3,...


print(name[0]) # จะได้ A
print(name[1]) # จะได้ B
print(name[-1]) #จะได้ C
print(all[-3]) # จะได้ True
print(all[2]) # จะได้ True

print(all[1:3]) # จะได้ A , True  โดยตัวเลข 3 คือหมายถึง <3 (ก่อนตัวที่3) : ก่อนจะถึงตัวสุดท้าย
print(all[-3:-1]) # จะได้ True , 3.14  โดยตัวเลข -1 คือหมายถึง >-1 (ก่อนตัวที่ -1) : ก่อนจะถึงตัวสุดท้าย 

print(all[0:]) # ตั้งแต่ลำดับ ที่ 0 ถึงตัวสุดท้าย ได้ 10 , A,True , 3.14 , 10 

# การแก้ไขข้อมูล 
"""
 ชื่อตัวแปร[index] = "ข้อมูลที่แก้ไข"

"""

Num = [1,2,3,4,5,6] # list มีสมาชิก 1-6

# print("ก่อนแก้ไข :",Num)
# Num[0]=-1
# Num[2]=9
# Num[-1]=20
# Num[-2]="นายA"
# print("หลังแก้ไข :",Num)


summ= 0
for x in Num:   # สมาชิก x อยู่ใน Num (เก็บสมาขิกNum ในตัวแปร x)
    summ+=x    # summ = summ +x
print(summ)

fruit = ["มะม่วง","มะนาว","มะยม"]

if 20 in Num:
    print("เป็น")
else:
    print("ไม่เป็น")

if "มะยม" in fruit:
    print("เป็น")
else:
    print("ไม่เป็น")

print(len(Num))


for i in range(len(fruit)):
    print(fruit[i])

for item in fruit:
    print(item)



print("ก่อนเพิ่ม :",fruit)
#เพิ้มข้อมูล
fruit.append("มะปราง") # append คือนำสมาชิกใหม่ มาต่อท้าย
print("หลังเพิ่ม :",fruit) # หลังเพิ่ม : ['มะม่วง', 'มะนาว', 'มะยม', 'มะปราง']

#insert แทรกข้อมูลระหว่างสมาชิก
fruit.insert(1,"แตงโม") # แตงโม เป็น สมาขิกตัวที่ 1
print("หลังเพิ่ม แทรก:",fruit) # หลังเพิ่ม แทรก: ['มะม่วง', 'แตงโม', 'มะนาว', 'มะยม', 'มะปราง']


# ลบข้อมูล >>> remove , pop , del ,clear
fruit.remove("มะยม") # ลบสมาชิก "มะยม" ออกไป
print("Remove :",fruit)
# Remove : ['มะม่วง', 'แตงโม', 'มะนาว', 'มะปราง']


fruit.pop() #เอาสมาชิกตัวล่าสุดหรือตัวที่อยู่ด้านขวามือสุดออกไป
print("Pop :",fruit)
#Pop : ['มะม่วง', 'แตงโม', 'มะนาว']

# del คือลบ index (คือระบุตำแหน่งข้อมูล)
del fruit[1] # ลบ แตงโมออก เพราะอยู่ตำแหน่งที่ 1
print("Del :",fruit)
#Del : ['มะม่วง', 'มะนาว']

fruit.clear() # ลบ สมาชิกข้างในfruit ออกหมด  ยังเหลือตัวแปร fruit
print("Clear :",fruit) 
#Clear : []

# del fruit # ลบออกทั้งหมด ทั้งตัวแปร และสมาชิก 
# print(fruit)


number_2 = [1,2,3,4,5,6,7]
fruit_1 =["มะม่วง","มะนาว","ทุเรียน","มะละกอ"]

#การคัดลอกข้อมูล
x=[]
print("ก่อนcopy :",x)
#ก่อนcopy : []
x = fruit_1.copy() # x copy ข้อมูล  fruit_1
print("หลังcopy :",x)
#หลังcopy : ['มะม่วง', 'มะนาว', 'ทุเรียน', 'มะละกอ']

# การรวบข้อมูล
allgroup = number_2 + fruit_1   # + คือการรวบข้อมูลสมาชิกในกลุ่มเดียวกัน
print(allgroup)
# [1, 2, 3, 4, 5, 6, 7, 'มะม่วง', 'มะนาว', 'ทุเรียน', 'มะละกอ']


number_3 = [1,2,4,5,5,5,6,6,6,6,6,7,7,8,9,10]
x_1 = number_3.count(5) #ดูว่ามีเลข 5กี่ตัว
print("มีเลขอยู่\t",x_1,"ตัว")

number_2 = [1,2,3,4,5,6,7]
fruit_1 =["มะม่วง","มะนาว","ทุเรียน","มะละกอ"]
 
# extend เพิ่มสมาชิก โดยนำตัวแปรอีกตัวมาใส่ในตัวแปรหลัก
number_2.extend(fruit_1) # นำข้อมูลสมาชิก fruit_1 มาใส่ใน number_2
print(number_2)
# [1, 2, 3, 4, 5, 6, 7, 'มะม่วง', 'มะนาว', 'ทุเรียน', 'มะละกอ']