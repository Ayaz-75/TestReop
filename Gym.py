




def menu():
    print()
   
    print("Choice 1 = Running ")
    print("Choice 2 = Weight lifting ")
    print("Choice 3 = leaving gym ")
    print("Choice 4 = Exit menu ")

    choice =int(input("Enter your choice: "))
  #  choice =int(input("Enter your choice"))





    if choice==1:
        print()
        print("-----Welcome to the running machine-----")
        print() 

        print("Enter how many kilometers you want to run")
        kilo=int(input("Enter destination kilometers: "))

        print("You are going to run: ",kilo,"  Kilometers")


        menu()




    elif choice==2:
        print()
        print("-----Welcome to weight lifting machine-----")
        print()

        print("Enter how many kilograms you want to liftL ")
        kilog=int(input("Enter Kilograms"))

        print("You are going to lift: ",kilog,"Kilograms")

        menu()





    elif choice==3:
        print()
        print("Kindly leave the gym time is over ")
        print()

        menu()



        

    else:

        print()
        print("you did not chose coming to the Gymnasim Take care bye")











print()
print("------Welcome to Gymnasim------")

#choice =int(input("Enter your choice"))
menu()