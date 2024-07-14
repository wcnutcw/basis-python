# ค้นหาและนับจำนวนตัวอักษรในสมาชิก

message =["aa","aab","cba","bba","aba","cca","aaaaaaacba"] 
result=[]

for item in message:
    result.append(item.count("a"))   # count ทำหน้าที่นับจำนวน
print(result)
