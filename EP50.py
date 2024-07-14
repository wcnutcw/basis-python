""" List parameter """

def displayfruitList(item):  
    for i in range(len(item)):
        print("ผลไม้ชิ้นที่ :",i+1,"=",item[i])


def displayvetTup(item):  
    for i in range(len(item)):
        print("ผลไม้ชิ้นที่ :",i+1,"=",item[i])


fruit=["มะม่วง","ทุเรียน"] # สร้างตัวแปร fruit ให้อยู่ในรูป list [ ]
displayfruitList(fruit)


""" Tuple parameter """

def displayfruitTup(item):  
    for i in range(len(item)):
        print("ผลไม้ชิ้นที่ :",i+1,"=",item[i])


Vet = ("ชะอม","ผักกาด","คะน้า") # สร้างตัวแปร vet ให้อยู่ในรูป tuple ( )
displayvetTup(Vet)