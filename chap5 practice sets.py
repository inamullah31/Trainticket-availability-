#Write a program to create a dictionary of hindi words with values as their engllish translation provide user with an option look it up!
myDict ={
    "pankha":"fan",
    "Dabba":"Box",
    "Vastu":"Item"
}
print("options are",myDict.keys())
a=input("enter the hindi word\n")
print("the meaning of your word is",)
#the below line does not throw an error
print("the meaning of your word is",myDict.get(a))
#displays none while value is not present

#print("Your options are here",myDict)


#3rd problem
#Can we have a set with 18 (int) and "18"(str) as a value in it? 
num1=int(input("enter number  1\n"))
num2=int(input("enter number  2\n"))
num3=int(input("enter number  3\n"))
num4=int(input("enter number  4\n"))
num5=int(input("enter number  5\n"))
num6=int(input("enter number  6\n"))
num7=int(input("enter number  7\n"))
num8=int(input("enter number  8\n"))
s={num1,num2,num3,num4,num5,num6,num7,num8}
print(s)
s={18,"18", 18.1}
print(s) 

#4th problem 
#What will be the length of following set s:
s=set()
s.add(20)
s.add(20.5)
s.add("20")
print(len(s))
s={20,20.0,"20"}
print(len(s))
# prints len 2 

#5th problem
s={}
print(type(s))

#6th problem
#Create an empth dictionary.Allow 4 friends to enter their favrouite language as values and use their nemes.Assume that  the names are unique.
favlang={}
a = input("enter your favourite language shubham\n")
b = input("enter your favourite language aniket\n")
c = input("enter your favourite language shaheena\n")
d = input("enter your favourite language harshith\n")
favlang['shubham']=a
favlang['aniket']=b
favlang['shaheena']=c
favlang['harshitha']=d

print(favlang)

#6th problem
#if names of 2 friends are same:What will is output the program

favlang={}
a = input("enter your favourite language shubham\n")
b = input("enter your favourite language aniket\n")
c = input("enter your favourite language shaheena\n")
d = input("enter your favourite language harshith\n")
favlang['shubham']=a
favlang['aniket']=b
favlang['shubham']=c
favlang['harshitha']=d

print(favlang)
#canyou change the values inside a list which is contained in set s
s={8,7,12,"harry",[1,2]}
print(s)


