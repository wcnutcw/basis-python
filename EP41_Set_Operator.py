# union

fruitA={"กล้วย","ผลไม้","มะนาว"}
fruitB={"สตอว์เบอรี่","กีวี","มะม่วง","ผลไม้","กล้วย"}

allFruit=fruitA.union(fruitB)
print(allFruit)
# {'กล้วย', 'มะนาว', 'กีวี', 'มะม่วง', 'สตอว์เบอรี่', 'ผลไม้' }

# หรือใช้คำสั่ง update ในการต่อสมาชิก
fruitA.update(fruitB)
print(fruitA)
#{'สตอว์เบอรี่', 'มะม่วง', 'กล้วย', 'มะนาว', 'กีวี', 'ผลไม้'}

# copy สมาชิก
fruitC=fruitA.copy()
print(fruitC)

# difference 

fruitD=fruitA.difference(fruitB)   # A - B คือ อยู่ใน A ไม่อยู่ใน B
print(fruitD) # {'มะนาว'}

# intersection : สมาชิกซ้ำกัน
fruitA={"กล้วย","ผลไม้","มะนาว"}
fruitB={"สตอว์เบอรี่","กีวี","มะม่วง","ผลไม้","กล้วย"}
fruitE = fruitA.intersection(fruitB)
print(fruitE) # {'กล้วย', 'ผลไม้'}

# ไม่ต้องสร้างตัวแปรเพิ่ม โดยใส่ _update
fruitA={"กล้วย","ผลไม้","มะนาว"}
fruitB={"สตอว์เบอรี่","กีวี","มะม่วง","ผลไม้","กล้วย"}
fruitA.difference_update(fruitB)
print(fruitA)  # {'มะนาว'}


# subset : ใช้คำสั่ง .issubset()

fish ={"ปลาดุก","ปลาหมอ","ปลาวาฬ","ปลาโลมา"}
x = {"ปลาหมอ","ปลาดุก"}

print(x.issubset(fish)) # True

# superset คือ set หลัก 
#  .issuperset() คือเช็คว่า set ใหญ่ มีสมาชิกทั้งหมด ของ set ย่อยมั้ย
print(fish.issuperset(x)) # True 


# min , max ใน set
number ={1,2,5,9,-1,41,400,100,9,-10,500}
print(min(number)) # -10
print(max(number)) # 500




