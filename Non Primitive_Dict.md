Dictionary : Tuple + Set 


# list , tuple

lis = ["สีแดง","สีเหลือง","สีเขียว"]
tup = ("สีแดง","สีเหลือง","สีเขียว")

# dictionary => key (การเข้าถึงข้อมูล) , value  (ค่าข้อมูล)
# list , tuple => index , value  ( ต้องหา index ถึงจะได้ ข้อมูล)
 
# การสร้าง dict 
# แบบปกติ
# ชื่อตัวแปร = {key:value,key:value,...key,value}
colors = {"red":"สีแดง","yellow":"สีเหลือง","green":"สีเขียว"}
# ระบุ key จะได้ value ( key:value )
print(colors["red"])  # สีแดง 


#  เขียนแบบ constructor
animal =dict(cat="แมว",dog="หมา",duck="เป็ด")
colors = dict({"red":"สีแดง","yellow":"สีเหลือง","green":"สีเขียว",10:"ดี"})

print(animal["dog"])  #หมา



# การเข้าถึงข้อมูล
print(colors[10])
print(colors.get(10)) # .get


# เปลี่ยนข้อมูล
colors[10]="บ้านแสนสุข"
print(colors) 
# {'red': 'สีแดง', 'yellow': 'สีเหลือง', 'green': 'สีเขียว', 10: 'บ้านแสนสุข'}

#การเพิ่มข้อมูล หรือแก้ไขข้อมูล  .update
colors.update({"blue":"สีน้ำเงิน"})
print(colors)
#{'red': 'สีแดง', 'yellow': 'สีเหลือง', 'green': 'สีเขียว', 10: 'บ้านแสนสุข', 'blue': 'สีน้ำเงิน'}

# ถ้าเจอ key ซ้ำ ให้แก้ไขข้อมูล
colors.update({10:"บ้านดี"})
print(colors)
# {'red': 'สีแดง', 'yellow': 'สีเหลือง', 'green': 'สีเขียว', 10: 'บ้านดี', 'blue': 'สีน้ำเงิน'}

# loop
for k,v in colors.items():    
     print("key =",k,"value =",v)

 # . items ให้แสดงทั้ง key และ value
 #  # .keys แสดงแค่ key
  # values แสดงแค่ value


# ลบข้อมูล ระบุ key : .pop
colors.pop("red")
print(colors)
# {'yellow': 'สีเหลือง', 'green': 'สีเขียว', 10: 'บ้านดี', 'blue': 'สีน้ำเงิน'}

# ลบข้อมูลล่าสุดที่เพิ่มเข้ามา หรือ อยู่หลังสุด ออกไป : .popitem
colors.popitem()
print(colors)
# {'yellow': 'สีเหลือง', 'green': 'สีเขียว', 10: 'บ้านดี'}

# clear : เคลียสมาชิกทั้งหมด เหลือแต่ตัวแปร
colors.clear()
print(colors)  # {}


# del : ลบสมาชิก และตัวแปร ออกไป (เคีลย memory)
del colors
print(colors)


# copy  : copy ข้อมูลสมาชิก
colors = {"red":"สีแดง","yellow":"สีเหลือง","green":"สีเขียว",10:"ดี"}
x =colors.copy()
print(x) 
# {'red': 'สีแดง', 'yellow': 'สีเหลือง', 'green': 'สีเขียว', 10: 'ดี'}


" Dict ซ้อน Dict "

market ={
    "ร้านป้าพร":{
        "name":"ป้าพร",
        "menu":["กระเพราไก่","ก๋วยเตี๋ยว"],
        "zone":"A"


    },
    "ร้านลุงป้อม":{
        "name":"น้าจ๊อบ",
        "menu":["มะม่วง","ทุเรียน"],
        "zone":"B"

    },
    "ร้านน้าใจ":{
        "name":"น้าใจ",
        "menu":["โค้ก","น้ำผลไม้"],
        "zone":"C"
    }
}

print(market["ร้านป้าพร"]["name"]) # [key หลัก][keyย่อย]
# ['กระเพราไก่', 'ก๋วยเตี๋ยว']


# Check ว่ามีข้อมูลมั้ย
print("ก๋วยเตี๋ยว" in market["ร้านป้าพร"]["menu"])
# True

if "มะม่วง" in market["ร้านป้าพร"]["menu"]:
    print("มี")
else :
    print("ไม่มี")
# ไม่มี

