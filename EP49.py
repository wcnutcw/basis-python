# Default Parameter  : กำหนดค่าเริ่มต้นให้ใน partameter

def displayData(fname,lname,city="กรุงเทพ"):  # # Default Parameter  : city="กรุงเทพ"
    print("ชื่อ =",fname)
    print("นามสกุล =",lname)
    print("จังหวัด =",city)

displayData("nut","chs","bangkok")
displayData(fname="อาโลล",lname="สวัสดี")  # ไม่ได้ป้อนข้อมูลในส่วน city ก็จะให้ ไปอยู่ที่ค่าเริ่มต้น คือ  city="กรุงเทพ"

