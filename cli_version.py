#Start of the salary calculation program.
print("<-------------Welcome------------->\n")

# this list will store the data of all the players as sub-lists.
# The first element is for referencing which index in the sub-lists stores what value and using in some print statements.
# There are dummy elements added to test some features of the program.
player_data=[["Name", "Speed", "Shooting", "Passing", "Defending", "Dribbling", "Physicality", "Overall rate", "Salary"],
            ['PlayerA', 2, 2, 2, 2, 2, 2, 40.0, [500, 400]],
            ['PlayerB', 3, 3, 3, 3, 3, 3, 60.0, [700, '']],
            ['PlayerC', 0, 1, 2, 3, 4, 5, 50.0, [700, 500]],
            ['PlayerD', 4, 4, 4, 4, 4, 4, 80.0, [1000, '']]]


# function to calculate the salary.
def salary_calc(overall_rate):

    if overall_rate >= 80:
        salary = 1000
        salary2 = ""
    
    elif 60 < overall_rate < 80:
        salary = 1000
        salary2 = 700
    
    elif overall_rate == 60:
        salary = 700
        salary2 = ""
    
    elif 45 < overall_rate < 60:
        salary = 700
        salary2 = 500
    
    elif overall_rate == 45:
        salary = 500
        salary2 = ""
    
    elif 30 < overall_rate < 45:
        salary = 500
        salary2 = 400
    
    else:
        salary = 400
        salary2 = ""

    return [salary, salary2]


# function to take input of a player's data, calculate the overall rate and salary, and return all that data as a list
def take_input():
    input_list = []

    #
    while(True):
        name = input("Name: ")
        
        if name.isalpha():
            input_list.append(name)
            break
        else:
            print("The name shouldn't contain numbers or special characters.\n")
            continue

    #
    sum_rating=0
    for x in range(6):
        while(True):
            value = input("{} rating: ".format(player_data[0][x+1]))
            
            if value not in ('0','1','2','3','4','5'):
                print("The rating should be between 0-5.\n")
                continue
            else:
                input_list.append(int(value))
                sum_rating+=int(value)
                break
    
    #
    input_list.append(round(sum_rating*100/30, 2))

    #
    sal = salary_calc(input_list[7])
    input_list.append(sal)

    return input_list


#main loop of the program
while(True):

    print("What would you like to do?")
    print("1.Calculate the salary of a new player")
    print("2.List the data of all players")
    print("3.Close the program\n")

    while(True):
        action = input("(1/2/3): ")


        if action == '1':
            print("\n<--------------------------------->\n")
            print("Enter player's details:")
            details = take_input()
            
            print("\n{}'s overall rate is {}".format(details[0], details[7]))
            print("Therefore {}'s salary should be ".format(details[0]), end = "")
            print(details[8][0], details[8][1])

            print("\nWould you like to store {}'s information?".format(details[0]))
            while(True):
                save_info = input("(y/n): ")
                if save_info == 'y':
                    player_data.append(details)
                    print("\nInformation stored.\nThank you.")
                    break
                elif save_info == 'n':
                    break
                else:
                    print("invalid choice\n")
            
            print("\n<--------------------------------->\n")
            break
        
        #
        if action == '2':
            print("\n<--------------------------------->\n")
            
            if len(player_data) == 1:
                print("No player info available")
                print("\n<--------------------------------->\n")
                break
            else:
                print("List of all players:")
                for x in range(1,len(player_data)):
                    print("{}.{}".format(x, player_data[x][0]))
                print("\n<--------------------------------->\n")
                break
        
        #
        if action == '3':
            print("\n<--------------------------------->\n")
            print("The program will now close\nThank you")
            print("\n<--------------------------------->\n")
            quit()

        else:
            print("invalid choice\n")
