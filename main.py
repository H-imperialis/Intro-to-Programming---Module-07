# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# Axel Adams, 2/27/2012, Added Exception Handling and Pickling
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
ToDoFile = "ToDoList.txt"   # An object that represents To Do List
objFile = None #An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
import pickle #import pickle module


# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open(ToDoFile,"a")#Creates the text file if none exists
objFile.close()
objFile = open(ToDoFile, "r")#Here we import the text file data and convert to the list table
for row in objFile:
    lstRow = row.split(",")
    dicRow = {"Task" : lstRow[0], "Priority" : lstRow[1].strip()}
    lstTable.append(dicRow)


# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    How would you like to alter your To Do List?
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Pickle My List
    6) DePickle and Display My List
    7) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 8] - "))
    print()  # adding a new line for looks

    try:
        # Step 3 - Show the current items in the table
        if (strChoice.strip() == '1'):
            if len(lstTable) == 0:
                print("Your To Do List is empty")#If text file is empty
            else:
                for dicRow in lstTable:
                    print(dicRow["Task"]+","+dicRow["Priority"])#Print the list table


        # Step 4 - Add a new item to the list/Table
        elif (strChoice.strip() == '2'):
            print("Add a 'Task' and 'Priority' for your To Do List Table")
            userTask = input("Enter a Task:")
            userPriority = input("Enter a Priority:")
            dicRow = {"Task": str(userTask).lower(), "Priority": str(userPriority).lower()}
            lstTable.append(dicRow)#We add a dictionary row to the list table
            continue


        # Step 5 - Remove a new item from the list/Table
        elif (strChoice.strip() == '3'):
            if len(lstTable) == 0:
                print("The To Do List is empty.")
            else:
                strTask = str(input("Which task would you like to remove?:")).lower()
                #for dicRow in lstTable:
                while True:
                    try:
                        for row in lstTable:
                            if row["Task"].lower() == strTask.lower():
                                lstTable.remove(row)  # we remove the item from the list table
                                print("This item has been removed from your To Do List!")
                    except IndexError:
                        print("This task is not on your To Do List!")
                    else:
                        print("This task is not on your To Do List!")
                    break

        # Step 6 - Save tasks to the ToDoToDoList.txt file
        elif (strChoice.strip() == '4'):
            objFile = open(ToDoFile, "w") #We open the list in such a way as to be able to write it
            for dicRow in lstTable: #We convert the lstTable back to dictionary format to write in text file
                objFile.write(dicRow["Task"]+","+dicRow["Priority"]+"\n")
            print("Your To Do List has been updated!")
            continue

        #Step 7 - Pickle My List
        elif(strChoice.strip() == '5'):
            with open('ToDoListpkl.txt', 'wb') as f: #We create a separate pickled file, using the "write binary" context
                pickle.dump(lstTable, f) #we write the pickled data
                f.close()

        #Step 8 Depickle and Display list
        elif (strChoice.strip() == '6'):
            with open('ToDoListpkl.txt', 'rb') as f:  # we open the list and read in read binary contaxt
                ToDoList_pickle = pickle.load(f)
                print(ToDoList_pickle)

        #Step 9 - Exit program
        elif (strChoice.strip() == '7'):
            objFile.close()
            break  # and Exit the program

    except IndexError:
        print("Please choose from the choices above.")
    else:
        print("Please choose from the choices above.")
