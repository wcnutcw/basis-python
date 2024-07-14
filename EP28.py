#ตารางหมากฮอต

"""
xxx
xxx
xxx

x = สีน้ำตาล  
o = สีขาว    

"""



number = int(input("ป้อนขนาด :"))
for row in range(1,number+1):
    for column in range(1,number+1):
        print("x",end="") if (row+column)%2==0   else print("o",end="")   #เขียนแบบternary ลดรูป if else
        # if (row+column)%2==0
        #     print("x",end='')
        # else:
        #     print("o",end='')
    print("")
    



