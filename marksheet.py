Name=input("Please enter your name: ")
#Subject variable specify the marks in that subject
#Lets assume there are 4 subjects
Subject1=int(input("Enter marks out of 100: "))
Subject2=int(input("Enter marks out of 100: "))
Subject3=int(input("Enter marks out of 100: "))
Subject4=int(input("Enter marks out of 100: "))

Total_marks=400
marks_obtained=Subject1+Subject2+Subject3+Subject4
Percentage=(marks_obtained/Total_marks)*100
if Percentage>=90:
    print(f"{Name} passed with A+ Grade")
elif Percentage<80 and Percentage>=70:
    print(f"{Name} passed with B Grade")
elif Percentage<70 and Percentage>=60:
    print(f"{Name} passed with C Grade")
elif Percentage<60 and Percentage>=50:
    print(f"{Name} passed with D Grade")
elif Percentage<50:
    print(f"{Name} failed with F Grade")
