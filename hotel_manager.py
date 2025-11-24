import random
import numpy as np
main_dict={}
all_rooms=[]
def rooms_intializing (floor,room):
    
    price=int(input("Enter the price of the rooms"))
    i=0
    while (i<=floor):
        j=1
        print("In Floor",i,end="\t")
        while(j<=room):
            r=i*100+j
            print(r,end=" ")
            all_rooms.append(r)
            j+=1
        print()
        i+=1

    print("Do you want to add or remove any room")
    
    p_change=int(input("Enter 1 to remove a room else enter 0"))
    while(p_change!=1 and p_change!=0):
        p_change=int(input("Invalid Input. \nEnter 1 if yes else enter 0"))
    if(p_change==1):
        while(True):
            g_room=int(input("Enter the room number to remove"))
            while(g_room not in all_rooms):
                g_room=int(input("Invalid Input. \nEnter the room number to remove"))
            all_rooms.remove(g_room)
            choice=int(input("Enter 1 if you want to remove more rooms else enter 0"))
            while(choice!=1 and choice!=0):
                choice=int(input("Invalid input. \nEnter 1 if you want to remove more rooms else enter 0"))
            if(choice==0):
                break
    
    p_change=int(input("Enter 1 to add a room else enter 0"))
    while(p_change!=1 and p_change!=0):
        p_change=int(input("Invalid Input. \nEnter 1 if yes else enter 0"))
    if(p_change==1):
        while(True):
            g_room=int(input("Enter the room number to add"))
            while(g_room in all_rooms):
                g_room=int(input("Invalid Input. \nEnter the room number to add"))
            all_rooms.append(g_room)
            choice=int(input("Enter 1 if you want to remove more rooms else enter 0"))
            while(choice!=1 and choice!=0):
                choice=int(input("Invalid input. \nEnter 1 if you want to remove more rooms else enter 0"))
            if(choice==0):
                break

    all_rooms.sort()
    #all_rooms.reverse()
    
    n=len(all_rooms)
    room_a=np.array(all_rooms)
    i=0
    while(i<n):
        r=str(room_a[i])
        main_dict[r]={"Customer Name":"NA","Occupied":False,"Date-In":"NA","Phone number":"0","Date-Out":"NA","Verification ID type":"NA","ID number":"NA","outstanding amount":0,"Per-Day cost":price}
        i+=1
    print(main_dict)
            
    print(f"The Default price of all the rooms is {price}.Do you want to change the price of any specific room?")
    p_change=int(input("Enter 1 if yes else enter 0"))
    while(p_change!=1 and p_change!=0):
        p_change=int(input("Invalid Input. \nEnter 1 if yes else enter 0"))
    if(p_change==1):
        fl=True
        while(fl):
            g_room=int(input("Enter the room number to change the price"))
            while(str(g_room) not in main_dict.keys()):
                g_room=int(input("Invalid Input. \nEnter the room number to change the price"))
            g_price=int(input("Enter the price of the room"))
            main_dict[str(g_room)]["Per-Day cost"]=g_price
            p_change=int(input("Enter 1 if you want to change the price of more rooms yes else enter 0"))
            while(p_change!=1 and p_change!=0):
                p_change=int(input("Invalid Input. \nEnter 1 if yes else enter 0"))
            if(p_change==1):
                continue
            else:
                fl=False
    
            


print("First we want to initialize so enter the total number of Floor and total number of rooms is each floor")
floors=int(input("Enter the total number of Floors in the hotel"))
rooms=int(input("Enter the total number of Rooms in each floor"))
rooms_intializing(floors,rooms)
print("\n\n\nMenu:")
choice=input("Enter 1 to Check in new guest.\nEnter 2 to extend the stay of an existing Guest. \nEnter 3 to check-out a Guest.\nEnter 4 to access the details of the room. \nEnter Exit to exit the program\n\n")
while(choice!="Exit"):
    if(choice=="1"):
        name=input("Enter the Guest name")
        room_ch=input((f"Does {name} has any specific room preference"))
        g_room=0
        while(room_ch=="Yes"):
            r_ch=input("Enter the room number")
            if((main_dict[r_ch])["Occupied"]):
                print(f"Sorry, {name} the room is already occupied")
                room_ch=input((f"Does {name} has any specific room preference left or should we allot you a random room? \nEnter Yes for specific room else Enter No"))
            else:
                g_room=r_ch
                break
        if(room_ch=="No"):
            g_room=str(random.choice(all_rooms))
            while(main_dict[g_room]["Occupied"]):
                  g_room=str(random.choice(all_rooms))
        main_dict[g_room]["Customer Name"]=name
        phone=input(f"Enter the phone number of {name}.")
        while(len(phone)!=10):
            phone=input(f"Invalid input. \nEnter the phone number of {name} .")
        main_dict[g_room]["Phone number"]=phone
        main_dict[g_room]["Occupied"]=True
        main_dict[g_room]["Date-In"]=input("Enter the date for Check in")
        main_dict[g_room]["Date-Out"]=input("Enter the date for Check out")
        days=int(input("Enter the number of days the Guest will live in out hotel"))
        main_dict[g_room]["Verification ID type"]=input("Enter the verification id type used")
        main_dict[g_room]["ID number"]=input("Enter the verification id credentials used for Verification")
        paid=int(input(f"Enter the amount {name} has payed"))
        main_dict[g_room]["outstanding amount"]=(main_dict[g_room]["Per-Day cost"]*days)-paid

    elif(choice=="2"):
        g_room=input("Enter the room for check out")
        while(main_dict.get(g_room, {"Occupied":False})["Occupied"]==False):
            g_room=input("Invalid input. \nEnter the room for check out")

        checking_out_date=input("Please enter today's date")
        while(checking_out_date==main_dict[g_room]['Date-Out']):
            print(f"The original checking out date was {main_dict[g_room]['Date-Out']} kindly enter the number of days {main_dict[g_room]['Customer Name']} stayed in the hotel")
            days=int(input())
            main_dict[g_room]['outstanding amount']=main_dict[g_room]['outstanding amount']+(days*main_dict[g_room]['Per-Day cost'])
        
        while(main_dict[g_room]['outstanding amount']!=0):
            print("There is an outstanding amount for the stay in the hotel. \nKindly clear are the remaing dues.\nRemaining amount=",main_dict[g_room]['outstanding amount'])
            paid=int(input())
            main_dict[g_room]['outstanding amount']=main_dict[g_room]['outstanding amount']-paid

        print("Thank you for staying with us. We hope your visit was relaxing and enjoyable, and we look forward to seeing you again soon!")

        old_price = main_dict[g_room]['Per-Day cost']
        main_dict[g_room]={"Customer Name":"NA","Occupied":False,"Date-In":"NA","Date-Out":"NA","Verification ID type":"NA","ID number":"NA","outstanding amount":0,"Per-Day cost":old_price}

    elif(choice=="3"):
        g_room=input("Enter the room for check out")
        while(main_dict[g_room]["Occupied"]==False):
            g_room=input("Invalid input. \nEnter the room for check out")

        print(f"Right now the check-out date is{main_dict[g_room]["Date-Out"]}")
        ch=int(input("So dou you really want to change the check out dates? \nEnter 1 to change else press 2"))
        if(ch==1):
            change=input("Enter the check out dates")
            days=int(input("Enter the extra number of days the Guest will be staying in the hotel"))
            main_dict[g_room]["outstanding amount"]=main_dict[g_room]["outstanding amount"]+(main_dict[g_room]["Per-Day cost"]*days)
        elif(ch==2):
            print("Okay no changes will be done at the check out dates")
    elif(choice=="4"):
        g_room=input("Enter the room no to get the details of the room")
        while(g_room not in main_dict.keys()):
            g_room=input("Invalid input. \nEnter the room no to get the details of the room.")
        for i in main_dict[g_room].keys():
            print(i,main_dict[g_room][i])
    else:
        choice=input("Invalid Input. \nEnter a valid choice")
        continue
    choice=input("\n\n\nEnter 1 to Check in new guest.\nEnter 2 to extend the stay of an existing Guest. \nEnter 3 to check-out a Guest.\nEnter 4 to access the details of the room. \nEnter exit to exit the program\n\n")
