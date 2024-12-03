x=int(input("enter any number : "))
match x:
    case 1:
        print("you are learning C")
    case 2:
        print("you are learning C++")
    case 3:
        print("you are learning Python")
    case _ if x==4:
        print("you are learning computer language")
    case _:
        print("you are lear nothing")
        
