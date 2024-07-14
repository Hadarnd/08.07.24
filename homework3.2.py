#start
grade: int= int(input("what is your grade?"))

if grade < 0 or grade > 100 :
    print("illegal grade")

elif grade >= 0 and grade <= 40 :
    print("try harder next time...")

elif grade >= 41 and grade <= 60 :
    print("You're getting there, need some more work.")

elif grade >= 61 and grade <= 80 :
    print("pretty good")

elif grade >= 81 and grade <= 95 :
    print("Awsome!")

elif grade >= 96 and grade <= 100 :
    print("Excelent!! you're a star!!!")
#end