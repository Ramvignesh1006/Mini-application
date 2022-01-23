import Return
import ListSplit
import dt
import Borrow
'Harry Potter,Rowling,30'
'Will Solve It,Zen Strom,40'
'Informed Devices,Casandra Clare,25'
'Martile Instrument,Casandra Clare,20'
'The Mystery Series,Elytn Blyton,50'
def listSplit():
    global name
    global author
    global available
    name=[]
    author=[]
    available=[]
    with open("stock.txt","r") as f:
        lines=f.readlines()
        lines=[x.strip('\n') for x in lines]
        for i in range(len(lines)):
            ind=0
            for a in lines[i].split(','):
                if(ind==0):
                    name.append(a)
                elif(ind==1):
                    author.append(a)
                elif(ind==2):
                    available.append(a)
                else:
                    print("invalid choice")
                ind+=1
def getdate():
    import datetime
    now=datetime.datetime.now
    #print("date: ",now().date())
    return str(now().date())
def getTime():
    import datetime
    now=datetime.datetime.now
    #print("Time: ",now().time())
    return str(now().time())
def borrowBook():
    success=False
    while(True):
        borrowername=input("Enter the name of the borrower: ")
        if borrowername.isalpha():
            break
        print("please input alphabet from A-Z")
    t="Borrow-"+borrowername+".txt"
    with open(t,"w+") as f:
        f.write("               Library Management System  \n")
        f.write("                   Borrowed By: "+borrowername+"\n")
        f.write("    Date: " + dt.getDate()+"    Time:"+ dt.getTime()+"\n\n")
        f.write("S.N. \t\t name \t      Author \n" )
    
    while success==False:
        print("Please select a option below:")
        for i in range(len(ListSplit.name)):
            print("Enter", i, "to borrow book", ListSplit.name[i])
    
        try:   
            a=int(input())
            try:
                if(int(ListSplit.quantity[a])>0):
                    print("Book is available")
                    with open(t,"a") as f:
                        f.write("1. \t\t"+ ListSplit.name[a]+"\t\t  "+ListSplit.author[a]+"\n")

                    ListSplit.quantity[a]=int(ListSplit.available[a])-1
                    with open("Stock.txt","w+") as f:
                        for i in range(3):
                            f.write(ListSplit.name[i]+","+ListSplit.author[i]+","+str(ListSplit.available[i])+"\n")


                    #multiple book borrowing code
                    loop=True
                    count=1
                    while loop==True:
                        choice=str(input("Do you want to borrow more books? However you cannot borrow same book more than 3 times. Press y for yes and n for no."))
                        if(choice.upper()=="Y"):
                            count=count+1
                            print("Please select an option below:")
                            for i in range(len(ListSplit.name)):
                                print("Enter", i, "to borrow book", ListSplit.name[i])
                            a=int(input())
                            if(int(ListSplit.available[a])>0):
                                print("Book is available")
                                with open(t,"a") as f:
                                    f.write(str(count) +". \t\t"+ ListSplit.name[a]+"\t\t  "+ListSplit.author[a]+"\n")
                                ListSplit.available[a]=int(ListSplit.available[a])-1
                                with open("Stock.txt","w+") as f:
                                    for i in range(3):
                                        f.write(ListSplit.name[i]+","+ListSplit.author[i]+","+str(ListSplit.available[i])+"\n")
                                        success=False
                            else:
                                loop=False
                                break
                        elif (choice.upper()=="N"):
                            print ("Thank you for borrowing books from us. ")
                            print("")
                            loop=False
                            success=True
                        else:
                            print("Please choose as instructed")
                        
                else:
                    print("Book is not available")
                    borrowBook()
                    success=False
            except IndexError:
                print("")
                print("Please choose book acording to their number.")
        except ValueError:
            print("")
            print("Please choose as suggested.")
def returnBook():
    name=input("Enter name of borrower: ")
    a="Borrow-"+name+".txt"
    try:
        with open(a,"r") as f:
            lines=f.readlines()
            lines=[a.strip("$") for a in lines]
    
        with open(a,"r") as f:
            data=f.read()
            print(data)
    except:
        print("The borrower name is incorrect")
        returnBook()

    b="return-"+name+".txt"
    with open(b,"w+")as f:
        f.write("                Library Management System \n")
        f.write("                   returned By: "+ name+"\n")
        f.write("    Date: " + dt.getDate()+"    Time:"+ dt.getTime()+"\n\n")
        f.write("S.N.\t\tBookname\t\tCost\n")


    total=0.0
    for i in range(3):
        if ListSplit.name[i] in data:
            with open(b,"a") as f:
                f.write(str(i+1)+"\t\t"+ListSplit.name[i]+"\n")
                ListSplit.available[i]=int(ListSplit.available[i])+1
            total+=float(ListSplit.cost[i])
            
    print("\t\t\t\t\t\t\t"+"$"+str(total))
    print("Is the book return date expired?")
    print("Press Y for Yes and N for No")
    stat=input()
    if(stat.upper()=="Y"):
        print("By how many days was the book returned late?")
        day=int(input())
        fine=2*day
        with open(b,"a")as f:
            f.write("\t\t\t\t\tFine: $"+ str(fine)+"\n")
        total=total+fine
    


    print("Final Total: "+ "$"+str(total))
    with open(b,"a")as f:
        f.write("\t\t\t\t\tTotal: $"+ str(total))
    
        
    with open("Stock.txt","w+") as f:
            for i in range(3):
                f.write(ListSplit.kname[i]+","+ListSplit.author[i]+","+str(ListSplit.available[i])+"\n")
def start():
    while(True):
        print("        Welcome to the library management system     ")
        print("------------------------------------------------------")
        print("Enter 1. To Display")
        print("Enter 2. To Borrow a book")
        print("Enter 3. To return a book")
        print("Enter 4. To exit")
        try:
            a=int(input("Select a choice from 1-4: "))
            print()
            if(a==1):
                with open("stock.txt","r") as f:
                    lines=f.read()
                    print(lines)
                    print ()
   
            elif(a==2):
                ListSplit.listSplit()
                Borrow.borrowBook()
            elif(a==3):
                ListSplit.listSplit()
                Return.returnBook()
            elif(a==4):
                print("Thank you for using library management system")
                break
            else:
                print("Please enter a valid choice from 1-4")
        except ValueError:
            print("Please input as suggested.")
start()
