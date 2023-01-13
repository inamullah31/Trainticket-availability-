i=0
avlb=10
gavlb=20
while True:
    print("\n***Menu***")
    print("option\n 1=tb \n exit=0")
    op=int(input("enter your option"))
    if op==0:
        print("bahar nikloo")
        break
    elif op==1:
        print("****tb Menu***\n 1--rt\n 2--gt")
        op=int(input("enter your options"))
        if op==1:
            print("avlb tickets are",avlb)
            i=int(input("enter how many tk"))
            if i<=avlb:
                print("booked",i)
            avlb=avlb-i
            i=0
        else:("train ke nichay aakay marjaoo")
    elif op==2:
        print("gavlb are",gavlb)
        i=int(input("enter your tk"))
        gavlb=gavlb-i
        i=0
    else:("train ke nichay aakay marjaoo")



