import mysql.connector
from numpy import true_divide
from tabulate import tabulate

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=" ",
    database="mypythonproject"

)

mycursor = mydb.cursor()


# mycursor.execute("SELECT * FROM my_team")
# for x in mycursor:
#     print(x)


print("Welcome! You are now the new Manager of Newcastle ")
print("We need you to build the best team possible for this upcoming season!")

def main():

    headers = ["player_name", "position"]

    while True:
        
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
            # player_count = mycursor.execute("Select count(*) FROM my_team")
            
            # print("you have", player_count, "players!")
                


            print("These are your current team players.")
            print("Sell whoever you wish.")
            mycursor.execute("SELECT * FROM my_team")
            for n in mycursor:
                print(n)

            print("\t1. Sell a player ")
            print("\t2. Go back to main menu")
            while True:
                try:
                    sellinput = int(input("\nSelection: "))
                except ValueError:
                    print(ValueError)
                    print("Please enter a valid numerical number!")
                else:
                    break 
            if sellinput == 1:
                id = int(input("Please insert a valid player id: "))
                mycursor.execute(f"select sell_value from my_team where id ={id}")
                for sell_value in mycursor:
                    # print(sell_value[0])
                    # print(type(sell_value[0]))
                    mycursor.execute("select transfer_money from all_teams where team_name = 'Newcastle'")
                    for myFunds in mycursor:
                        mycursor.execute(f"update all_teams set transfer_money = {myFunds[0] + sell_value[0]} where team_name = 'Newcastle'")
                        # print(myFunds[0] + sell_value[0])
                        mycursor.execute(f"delete from my_team where id = {id}")

                        mydb.commit()

                

                # mycursor.close()



        elif sel ==2:
            mycursor.execute("select transfer_money From all_teams where team_name = 'Newcastle'" )
            for t in mycursor:
                print (t[0], "million")
        

        elif sel == 3:
            mycursor.execute("select transfer_money From all_teams where team_name = 'Newcastle'" )
            for t in mycursor: 
                availableFunds = t[0]
            mycursor.execute(f"SELECT * FROM market where team != 'Newcastle' AND cost <= {availableFunds}")
            for p in mycursor:
                print(p)
            print("These are the players that are up for sale")
            print("\t1. Buy a player")
            print("\t2. Go back to main menu")
            while True:
                try:
                    buyinput = int(input("\nSelection: "))
                except ValueError:
                    print(ValueError)
                    print("Please enter a valid numerical number!")
                else:
                    break 

            if buyinput == 1:
                player_id = int(input("Please insert a valid player id: "))
                mycursor.execute(f"select cost from market where player_id ={player_id}")
                for cost in mycursor:
                    playerCost = cost[0]
                
                    if availableFunds >= playerCost: 
                        mycursor.execute("SELECT transfer_money FROM all_teams WHERE team_name = 'Newcastle'")
                        for myFunds in mycursor:
                            mycursor.execute(f"UPDATE all_teams SET transfer_money = {myFunds[0] - playerCost} WHERE team_name = 'Newcastle'")
                            mycursor.execute("SELECT MAX(jersey_number) FROM my_team")
                            for jerseynum in mycursor:
                                num = jerseynum[0] + 1
                                mycursor.execute(f"SELECT player_name, position FROM market WHERE player_id ={player_id}")
                                for player in mycursor:
                                    myPlayer = player[0]
                                    position = player[1]

                                    # print(player_id)
                                    # print(myPlayer)
                                    # print(position)
                                    # print(num)
                                    # print(playerCost)
                                    mycursor.execute(f"INSERT INTO my_team VALUES({player_id},'{myPlayer}','{position}',{num},'Newcastle',{playerCost})")

                                    mydb.commit()
                    else:
                        print("You dont have enough funds for this transaction!")






        elif sel == 4:
            mycursor.execute("SELECT player_name, position FROM my_team")
            for x in mycursor:
                print(x)
           

            print("This is your current team roster!")
            print("\t1. press any digit to exit to main menu ")
            
            while True:
                try:
                    input1 = int(input("\nSelection: "))
                except ValueError:
                    print(ValueError)
                    print("Please enter a valid numerical number!")
                else:
                    break 

            



        elif sel == 5:
            print("You are know exiting the program, goodbye!")

            break



        else:
            print("please enter a valid input.")

            
            

main()
