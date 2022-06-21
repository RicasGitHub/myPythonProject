import mysql.connector
from numpy import true_divide

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Jennifer1992",
    database="myPythonProject"

)

mycursor = mydb.cursor()


# mycursor.execute("SELECT * FROM all_teams")
# for x in mycursor:
#     print(x)




def main():
    while True:
        print("Welcome! You are now the new Manager of Newcastle ")
        print("We need you to build the best team possible for this upcoming season!")
        print("You can sell and buy whoever you want aslong as you have the funds to do so")
        print("\t1. View my team and sell players. ")
        print("\t2. View available funds.")
        print("\t3. View market and buy players.")
        print("\t4. View team.")
        print("\t5. Exit")


        while True:
            try:
                sel = int(input("\nSelection: "))
            except ValueError:
                print(ValueError)
                print("Please enter a valid numerical number!")
            else:
                break 

            


        if sel == 1: 
            print("These are your current team players.")
            print("Sell whoever you wish.")
            team = mycursor.execute("SELECT * FROM my_team")
            for n in team:
                print(n)

            print("\t1. Sell players ")
            print("\t2. Go back to main menu")

        elif sel ==2:
            print ()

        

        elif sel == 3:
            print()



        elif sel == 4:
            print()


        elif sel == 5:
            print() 



        else:
            print("please enter a valid input.")
            
            

main()
