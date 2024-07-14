# โปรแกรมคำนวณเกรดนักเรียน

try:
    # fw=open("Score.txt","a",encoding="utf-8")
    # while True:
    #      studentID=input("ป้อนรหัสนักเรียน :")
    #      if studentID=="exit":
    #                  break
    #      Score=input("ป้อนคะแนนสอบนักเรียน :")
    #      fw.writelines(studentID+"\t"+Score+"\n")
    # fw.close()
    fr=open("Score.txt","r",encoding="utf-8")
    fw=open("Grade.txt","w",encoding="utf-8")
    grade=None
    for line in fr.readlines():   # .readlins() : อ่านทีละบรรทัด
        score=line[-4:].strip()
        studentid=line[:3].strip()
        # print("รหัสนักเรียน :",studentid,"คะแนน :",score)
        score=int(score)
        if score>=80:
            grade="A"
        elif score>=70 and score<80:
            grade="B"
        elif score>=50 and score<=69:
            grade="C"
        else:
            grade="F"
        fw.writelines(studentid+"\t"+str(score)+"\t"+grade+"\n")
    fw.close()
    fr.close()
        

except Exception as e:
             print(e)
