# จับคู่สินค้า และ ราคา

fruit =["มะม่วง","แตงโม","กีวี่"]
price =["10","20","30"]

for x,y in zip(fruit,price[::-1]) : # zip คือการให้สมาชิกทำงานพร้อมกันเลย
    print("สิ้นค้า =",x,"ราคา =",y)