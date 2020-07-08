print("----------WELCOME TO ZOYA'S RAILWAY BOOKING CENTRE----------")
print("----------DESIGNED BY ZOYA SHAKIL-------------")
print("Here you can book your rail tickets,check your pnr status and a lot more")
name=str(input("Enter your name:"))
age=int(input("Enter your age:"))
number=int(input("Enter your mobile number:"))
gender=str(input("Enter your gender:"))

distah=750
distda=742
distad=636
pkac1=8
pkac2=7
pkac3=6
pknac=5
print("Welcome to Zoya's railway booking centre")
print("Hello user,We have the following trains running:")
print("1.Allahabad to Howrah")
print("2.Durg to Allahabad")
print("3.Allahabad to Delhi")
ch=int(input("Enter your choice number:"))
if(ch==1):
    traintype=input("Enter Train Type:AC1/AC2/AC3/NON-AC:")
    nopass=int(input("Enter the number of passengers:"))
    for i in range(1,nopass+1):
        print("Enter name of passenger:",i)
        name=input()
        print("Enter age of passenger:",i)
        age=input()
        if(traintype=="AC1"):
            fare=nopass*distah*pkac1
            print(fare)
        elif(traintype=="AC2"):
            fare=nopass*distah*pkac2
            print(fare)
        elif(traintype=="AC3"):
            fare=nopass*distah*pkac3
            print(fare)
        elif(traintype=="NON-AC"):
            fare=nopass*distah*pknac
            print(fare)

elif(ch==2):
    traintype=input("Enter Train Type:AC1/AC2/AC3/NON-AC:")
    nopass=int(input("Enter the number of passengers:"))
    for i in range(1,nopass+1):
        print("Enter name of passenger:",i)
        name=input()
        print("Enter age of passenger:",i)
        age=input()
    if(traintype=="AC1"):
            fare=nopass*distda*pkac1
            print(fare)
    elif(traintype=="AC2"):
            fare=nopass*distda*pkac2
            print(fare)
    elif(traintype=="AC3"):
            fare=nopass*distda*pkac3
            print(fare)
    elif(traintype=="NON-AC"):
            fare=nopass*distda*pknac
            print(fare)
elif(ch==3):
    traintype=input("Enter Train Type:AC1/AC2/AC3/NON-AC:")
    nopass=int(input("Enter the number of passengers:"))
    for i in range(1,nopass+1):
        print("Enter name of passenger:",i)
        name=input()
        print("Enter age of passenger:",i)
        age=input()
    if(traintype=="AC1"):
            fare=nopass*distad*pkac1
            print(fare)
    elif(traintype=="AC2"):
            fare=nopass*distad*pkac2
            print(fare)
    elif(traintype=="AC3"):
            fare=nopass*distad*pkac3     
            print(fare)
    elif(traintype=="NON-AC"):
            fare=nopass*distad*pknac
            print(fare)


     
        
    

    


      
