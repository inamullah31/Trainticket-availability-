'''#write a program to find greatest of four numbers
num1=(int(input("enter number 1: ")))
num2=(int(input("enter number 2: ")))
num3=(int(input("enter number 3: ")))
num4=(int(input("enter number 4: ")))

if(num1>num4):
    f1= num1
else:
    f1= num4

if(num2>num3):
    f2= num2
else:
    f2= num3

if(f1>f2):
    print(str(f1)+ " is greatest")
else:
    print(str(f2)+ " is greatest")

#write a program to find out whether a student is pass or fail, if it requires total 40% and at least 33% in eCH AUBJECT TO Paas.Assume 3 subject and take marks as an input from user.

sub1=int(input("enter first subject marks\n"))
sub2=int(input("enter first subject marks\n"))
sub3=int(input("enter first subject marks\n"))
if (sub1<33 or sub2<33 or sub3<33):
    print("you are fail")
if(sub1+sub2+sub3)/3 <40:
    print("you are fail beacause you have less than 40")
else:
    print("Congratulations ! you passed the exam")

#A spam comment is defined as a text containing following keywords:
text = input("enter the txt")

if("make a lot of money"):
    spam = True   
elif("buy now" in text):
    spam =True
elif("click this" in text):
    spam = True
elif("subscribe this" in text):
    spam =True
else:
    spam = False
if(spam):
    print("This text is spam")
else:
    print("This text is not a spam")
    
#Write a program to find whether a given username contains less than 10 characters or not.
names = ["harry","shubham","rohith","rohan","aditi","shipra"]
name = input("Enter the name to check\n")

if name in names:
    print("your name is present in the list")
else:
    print("your name is not in the list")
'''
#write a program to calculate the grade of a student from his marks from thefollowing scheme 
'''90-100 --> Ex
80-90  --> A
70-80  --> B
60 -70 --> c
50 -60 --> D
<50 -F

marks = int(input("Enter your Marks \n"))

if marks>90:
    grade ='ex'
elif marks>80:
    grade ="A"
elif marks>70:
    grade ="B"
elif marks>60:
    grade = "C"
elif marks>50:
    grade ="D"
else:
    grade="fail"
print("your grade is "+ grade)'''


