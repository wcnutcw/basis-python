# **kwargs  : ตั้งชื่อ parameter ได้ไม่จำกัด ( เก็บข้อมูลแบบ Dict{} )
# *args : ใส่ argument ได้ไม่จำกัด   ( เก็บข้อมูลแบบ tuple() )


def displayData(**kwargs):   # kwargs เปลี่ยนเป็ชื่ออื่นได้
    print(kwargs)


displayData(singlename="Nut")
displayData(fname="Nut",lname="Chs")
displayData(fname="Nut",lname="Chs",age="21")
displayData(fname="Nut",lname="Chs",age="21",city="กรุงเทพ")
displayData(fname="Nut",lname="Chs",age="21",country="กรุงเทพ")

