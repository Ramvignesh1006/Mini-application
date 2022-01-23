users=[["ram",7411,75000],["vignesh",1234,89000],["vicky",7890,120000],["ramu",2345,256000]]
l=None
amount=[100,200,500,2000]
number=[0,0,0,0]
def admin(bal):
    while True:
        print("1. Load")
        print("2. Show")
        print("3. Exit")
        a1=int(input("Enter your choice: "))
        if(a1==1):
            ind=0
            for i in amount:
                num=int(input("Enter No. of"+str(i)+"Notes: "))
                number[ind]+=num
                ind+=1
                bal+=(i*num)
            print("Your current balance amount: ",bal)
            print("Your money added successfully")
        elif(a1==2):
            for j in range(0,len(amount)):
                print(str(amount[j])+"-"+str(number[j]))
            print("Your current balance amount:",bal)
        elif(a1==3):
            print("Thank you")
            break
        else:
            print("Invalid move")
def user(bal,pin):
    while True:
        print("1. Withdraw")
        print("2. Balance Enquiry")
        print("3. Pin change")
        print("4. Exit")
        u1=int(input("Enter your choice: "))
        if(u1==1):
            w=int(input("Enter your withdrawal amount: "))
            if(w<bal and w%100==0):
                if(w>=2000):
                    a2=w//2000
                    w1=(w%2000)
                    if(w1>=500):
                        a3=w1//500
                        w1=(w1%500)
                        if(w1>=200):
                            a4=w1//200
                            w1=(w1%200)
                            if(w1>=100):
                                a5=w1//100
                                w1=(w1%100)
                                if(w1==0):
                                    bal-=w
                                    print("Your current balance is: ",bal)
                                    print("Your withdrawal amount: ")
                                    print(a2,a3,a4,a5)
                            elif(w1==0):
                                a5=0
                                bal-=w
                                print("Your current balance is:",bal)
                                print("Your withdrawal amount: ")
                                print(a2,a3,a4,a5)
                            else:
                                print("Invalid amount")
                        elif(w1>=100):
                            a4=0
                            a5=w1//100
                            w1=(w1%100)
                            if(w1==0):
                                bal-=w
                                print("Your current balance is: ",bal)
                                print("Your withdrawal amount: ")
                                print(a2,a3,a4,a5)
                        elif(w1==0):
                            a4=0
                            a5=0
                            bal-=w
                            print("Your current balance is:",bal)
                            print("Your withdrawal amount: ")
                            print(a2,a3,a4,a5)
                        else:
                            print("Invalid amount")
                    elif(w1>=200):
                        a3=0
                        a4=w1//200
                        w1=(w1%200)
                        if(w1>=100):
                            a5=w1//100
                            w1=(w1%100)
                            if(w1==0):
                                bal-=w
                                print("Your current balance is: ",bal)
                                print("Your withdrawal amount: ")
                                print(a2,a3,a4,a5)
                        elif(w1==0):
                            a5=0
                            bal-=w
                            print("Your current balance is:",bal)
                            print("Your withdrawal amount: ")
                            print(a2,a3,a4,a5)
                        else:
                            print("Invalid amount")
                    elif(w1>=100):
                        a3=0
                        a4=0
                        a5=w1//100
                        w1=(w1%100)
                        if(w1==0):
                            bal-=w
                            print("Your current balance is: ",bal)
                            print("Your withdrawal amount: ")
                            print(a2,a3,a4,a5)
                    elif(w1==0):
                        a3=0
                        a4=0
                        a5=0
                        bal-=w
                        print("Your current balance is:",bal)
                        print("Your withdrawal amount: ")
                        print(a2,a3,a4,a5)
                    else:
                        print("Invalid amount")
                elif(w>=500):
                    a2=0
                    a3=w//500
                    w1=(w%500)
                    if(w1>=200):
                        a4=w1//200
                        w1=(w1%200)
                        if(w1>=100):
                            a5=w1//100
                            w1=(w1%100)
                            if(w1==0):
                                bal-=w
                                print("Your current balance is: ",bal)
                                print("Your withdrawal amount: ")
                                print(a2,a3,a4,a5)
                        elif(w1==0):
                            a5=0
                            bal-=w
                            print("Your current balance is:",bal)
                            print("Your withdrawal amount: ")
                            print(a2,a3,a4,a5)
                        else:
                            print("Invalid amount")
                    elif(w1>=100):
                        a4=0
                        a5=w1//100
                        w1=(w1%100)
                        if(w1==0):
                            bal-=w
                            print("Your current balance is: ",bal)
                            print("Your withdrawal amount: ")
                            print(a2,a3,a4,a5)
                    elif(w1==0):
                        a4=0
                        a5=0
                        bal-=w
                        print("Your current balance is:",bal)
                        print("Your withdrawal amount: ")
                        print(a2,a3,a4,a5)
                    else:
                        print("Invalid amount")
                elif(w>=200):
                    a2=0
                    a3=0
                    a4=w//200
                    w1=(w%200)
                    if(w1>=100):
                        a5=w1//100
                        w1=(w1%100)
                        if(w1==0):
                            bal-=w
                            print("Your current balance is: ",bal)
                            print("Your withdrawal amount: ")
                            print(a2,a3,a4,a5)
                    elif(w1==0):
                        a5=0
                        bal-=w
                        print("Your current balance is:",bal)
                        print("Your withdrawal amount: ")
                        print(a2,a3,a4,a5)
                    else:
                        print("Invalid amount")
                elif(w==100):
                    a2=0
                    a3=0
                    a4=0
                    a5=w//100
                    w1=w%100
                    if(w1==0):
                        bal-=w
                        print("Your current balance is: ",bal)
                        print("Your withdrawal amount: ")
                        print(a2,a3,a4,a5)
                else:
                    print("Invalid amount")
            else:
                print("Invalid amount")
            print("Thank you")
        elif(u1==2):
            print("Your current balance amount:",bal)
        elif(u1==3):
            p=int(input("Enter your current pin number:"))
            if(p==pin):
                p1=int(input("Enter your New password:"))
                p2=int(input("Confirm your New password:"))
                if(p1==p2):
                    pin=p1
                    print("Your New password is updated")
                else:
                    print("Enter correct password")
            else:
                print("Incorrect password")
                print("Please try again")
        elif(u1==4):
            print("Thank you")
            break
        else:
            print("Invalid move")
print("                ATM")
print("Welcome")
print("Please insert user card")
print("\t\t\rPlease Enter to continue!!!")
input()
while True:
    print("1. Admin")
    print("2. User")
    print("3. Exit")
    u=int(input("Enter your choice:"))
    if(u==1):
        for i in range(0,3):
            st=input("Enter your username:")
            pi=int(input("Please enter your 4 digit pin number:"))
            for j in users:
                if(st==j[0] and pi==j[1]):
                    l=j
            admin(j[2])
            break
            if(l==None):
                print("No such user")
            if(i==2):
                print("Your account is temporarily blocked")
                print("Please try again later.")
    elif(u==2):
        for i in range(0,3):
            st=input("Enter your username:")
            pi=int(input("Please enter your 4 digit pin number:"))
            for j in users:
                if(st==j[0] and pi==j[1]):
                    l=j
                    user(j[2],j[1])
                    break
            else:
                print("No such user")
            if(i==2):
                print("Your account is temporarily blocked")
                print("Please try again later.")
    elif(u==3):
        print("Thank you")
        print("Please collect your card!!!")
        break
