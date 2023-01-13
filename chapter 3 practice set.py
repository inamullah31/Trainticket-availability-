name = input("enter your name")
print("Good Afternoon "+ name)
"""letter = '''Dear <|NAME|>,
You are selected!'''

Date: <|DATE|>"""

name= input ("enter you name\n")
date =input("enter your date\n")
letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)
print(letter)
#replace
letter='''Dear <|NAME|>,
you are selected !
<|DATE|>'''
name=input("enter your name\n")
date=input("enter your date\n")
letter= letter.replace("<|NAME|>",name)
letter= letter.replace("<|DATE|>",date)
print(letter)
#double space

St="this is the string with double  spaces"
doubleSpaces = St.find("  ")
print(doubleSpaces)
St=St.replace("  "," ")
print(St)
#escape sequence character
letter1="Dear Harry,\n\t This Python course is nice.\nThanks!"
print(letter1)

