#แปลง ค.ศ. เป็น พ.ศ.
#แปลง พ.ศ. เป็น ค.ศ.

year_1 = int(input("ป้อน ค.ศ :"))
year_2 = int(input("ป้อน พ.ศ :"))

#แปลง ค.ศ เป็น พ.ศ + 543
#แปลง พ.ศ เป็น ค.ศ - 543

year_1 = year_1 + 543
year_2 = year_2 - 543

print("เป็น พ.ศ =",year_1)
print("เป็น พ.ศ =",year_2)

