#แลกเงินและหาจำนวนแบงค์

money = int(input("ป้อนเงิน :"))

if money>=1000:
    print("1000บาท =",money//1000,"ใบ")  #// คือหารปัดเศษ
    money = money % 1000  #ตย.เช่น 1500 % 1000 =500 (ได้เศษ500)
if money>=500 :
    print("500บาท=",money//500,"ใบ")
    money = money % 500
if money>=100:
    print("100บาท=",money//100,"ใบ")
    money = money % 100
if money>=50:
     print("100บาท=",money//50,"ใบ")
     money = money % 50
if money>=20:
     print("100บาท=",money//20,"ใบ")
     money = money % 20
if money>=10:
     print("100บาท=",money//10,"ใบ")
     money = money % 10
if money>=1:
     print("100บาท=",money,"ใบ")
