# หาค่าเลขยกกำลัง

number = [1,2,3,4,5,6,7]

# normal
for i in range(len(number)):
    number[i]=number[i]**2
print(number)

# ลดรูป
number_1 = [1,2,3,4,5,6,7]
number_1=[i*i for i in number]
print(number)