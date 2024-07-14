# โปรแกรมบัญชีธนาคาร 

#data
account={"นายA":5000,"นายB":0}

def getBalance():
    print("ยอดเงินคงเหลือในบัญชี :",account)


def deposit(money):
    if not type(money) is int and not type(money) is float:
        raise Exception("ป้อนตัวเลขเท่านั้น")
    if money<=0 :
        raise Exception("ค่าตัวเลขต้องเป็นบวกเท่านั้น")
    if money>account["นายA"]:
        raise Exception("ยอดเงินไม่พอ")

    print("ฝากเงินเข้าบัญชี A :",money)
    account["นายA"]+=money

def withdraw(money):
    if not type(money) is int and not type(money) is float:
        raise Exception("ป้อนตัวเลขเท่านั้น")
    if money<=0 :
        raise Exception("ค่าตัวเลขต้องเป็นบวกเท่านั้น")
    if money>account["นายA"]:
        raise Exception("ยอดเงินไม่พอ")
    print("ถอนเงินจากบัญชี A :",money)
    account["นายA"]-=money

def transfer(money):
    if not type(money) is int and not type(money) is float:
        raise Exception("ป้อนตัวเลขเท่านั้น")
    if money<=0 :
        raise Exception("ค่าตัวเลขต้องเป็นบวกเท่านั้น")
    if money>account["นายA"]:
        raise Exception("ยอดเงินไม่พอ")
    print("ทำการโอนเงินไปที่บัญชี B :",money)
    account["นายB"]+=money
    account["นายA"]-=money

try :
    getBalance()
    deposit(5000)
    getBalance()
    transfer(50.2)
    getBalance()
except Exception as e:
    print(e)

