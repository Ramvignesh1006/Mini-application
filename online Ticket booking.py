user={"ram":"1006","vicky":"1111","vignesh":"2222","ramu":"3333"}
user_info={"ram":("1","Banglore to Cochin","700"),
           "vicky": ("2","Cochin to Goa","500"),
           "vignesh":("3","Manglore to Banglore","800"),
           "ramu":("4","Goa to Banglore","500")}
station={"Banglore":1,"Goa":3,"Coachin":3,"Manglore":4}
Banglore={1: 'ram', 2: 'vicky', 3: 'vignesh', 4: 'ramu', 5: 'empty'}
Goa={1: "ram", 2: "empty", 3: "vignesh", 4: "empty", 5: "empty"}
Cochin={1: "ram", 2: "empty", 3: "vignesh", 4: "empty", 5: "empty"}
Manglore={1: "ram", 2: "empty", 3: "vignesh", 4: "empty", 5: "empty"}
seat_info={1:Banglore,2:Goa,3:Cochin,4:Manglore}
def userfun():
        global station
        global user
        global Banglore
        global user_name
        global seat_info
        global Banglore
        global Goa
        global Cochin
        global Manglore
        global user_info
        station_lst=list(station)
        print("1.Ticket booking\n2.Ticket info\n3.Ticket Cancellation")
        choice=int(input("Enter the choice:"))
        if(choice==1):
            boarding=str(input("From:"))
            station1=str(input("To:"))
            a=station.get(boarding)
            dc={"Banglore":Banglore,"Goa":Goa,"Cochin":Cochin,"Manglore":Manglore}
            dc1={"Banglore":1,"Goa":2,"Cochin":3,"Manglore":4}
            if(int(a)>=1):
               seat_pro=[]
               seat_lst = []
               print("Ticket cost:", 500)
               for i in range(1,6):
                   for pro in range(dc1[boarding],dc1[station1]+1):
                       if(seat_info[pro].get(i)== "empty"):
                               seat_pro.append(i)
                               if(((dc1.get(station1)-dc1.get(boarding))+1)==seat_pro.count(i)):
                                    seat_lst.append(i)
               if(len(seat_lst)==1):
                           print("available seat No:")
                           print("only seat no:",seat_lst[0],"is availbale")
                           choice1 = str(input("Are u sure u want to book the seat:Y/n:"))
                           if (choice1 == "y"):
                               for j in range(len(seat_lst)):
                                   dic1={"Banglore":1,"Goa":2,"Cochin":3}
                                   dic={"Goa":3,"Cochin":4,"Manglore":5}
                                   for y in range(dic1.get(boarding),dic.get(station1)):
                                        seat_info[y].update({seat_lst[0]: user_name})
                               station_keys=list(station.keys())
                               count=0
                               for z in range(len(station_keys)):
                                   if(station.get(z)=="empty"):
                                       count+=1
                                       station.update({z:count})
                               user_info.update({user_name: ("          ", str(seat_lst[0]), "       ", boarding, "to", station1, "      ", "500")})
                               available_seat = station.get(boarding) - 1
                               station.update({boarding: available_seat})
                               print("your seat is booked,Happy journey")
               elif(len(seat_lst)>1):
                           print("available seat No:")
                           print(seat_lst)
                           choice=int(input("select one of the seat no mentioned above:"))
                           if(choice in seat_lst):
                              choice1 = str(input("Are u sure u want to book the seat:Y/n:"))
                              if (choice1 == "y"):
                                   for j in range(len(seat_lst)):
                                       dic1 = {"Banglore": 1, "Goa": 2, "Cochin": 3}
                                       dic = {"Goa": 3, "Cochin": 4, "Manglore": 5}
                                       for y in range(dic1.get(boarding), dic.get(station1)):
                                           seat_info[y].update({choice: user_name})
                                   station_keys = list(station.keys())
                                   count = 0
                                   for z in range(len(station_keys)):
                                     if (station.get(z) == "empty"):
                                           count += 1
                                           station.update({z: count})
                                   dc[boarding].update({choice: user_name})
                                   dc[station1].update({choice: user_name})
                                   available_seat = station.get(boarding) - 1
                                   station.update({boarding: available_seat})
                                   user_info.update({user_name: ("          ",str(choice),"       ",boarding,"to",station1,"      ","500")})
                                   print("your seat is booked, Happy journey")
               else:
                   print("No seats is available please select next station")
            else:
                print("No seats is available")
        elif(choice==2):
            if(user_name not in user.keys()):
                print("No booking yet")
            else:
                print("Name       seat no        Board to Deboard:         ticket cost")
                print(user_name, *user_info.get(user_name))
        else:
            confirm=str(input("do you want to cancel the booking y/n:"))
            if(confirm=="y"):
                print("For Confirmation")
                choice1=str(input("enter the name"))
                choice=int(input("enter the seat number:"))
                user.pop(user_name)
                user_info.pop(user_name)
                for i in range(1,5):
                    seat_info[i].update({choice:"empty"})
                print("cancellation is done")
                intro()
            else:
                intro()
def intro():
    global station
    global user_name
    global Banglore
    global Goa
    global Cochin
    global Manglore
    print("\n1.user\n2.exit")
    choice=int(input("Enter the choice:"))
    if(choice==1):
        while True:
            print("1.new user\n2.existing user\n3.exit")
            choice=int(input("Enter the choice:"))
            if(choice==1):
                user_name=str(input("Enter the name:"))
                user_password=str(input("Enter the password:"))
                userfun()
                user.update({user_name: user_password})
                intro()
            elif(choice==2):
                user_name=str(input("Enter the name:"))
                user_password=str(input("Enter the password:"))
                if((user_name,user_password) in user.items()):
                    userfun()
                else:
                    print("Invalid username or password")
            else:
                intro()
    else:
            intro()
intro()
