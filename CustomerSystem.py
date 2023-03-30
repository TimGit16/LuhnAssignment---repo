# Throughout this project, the use of data structures are not permitted 
# Minimal built in functions are to be used and the majority of functions must be
# created yourself

# More packages may be imported in the space below if approved by your instructor

def printMenu():
    print('''
          Customer and Sales System\n
          1. Enter Customer Information\n
          2. Generate Customer data file\n
          3. Report on total Sales (Not done in this part)\n
          4. Check for fraud in sales data (Not done in this part)\n
          9. Quit\n
          Enter menu option (1-9)
          ''')


def validatePostalCode(code):
    PCfile = open("postal_codes.csv", "r")
    for i in PCfile: # Loops through each line in postal code csv file where i contains the text of each line of the iteration
        if i[:3] == code: # Takes the first 3 characters of the line and checks if it is the same to the user inputted code
            PCfile.close() # Closes file
            return True # returns true if valid
    PCfile.close()
    return False # returns false in invalid


def validateCreditCard(cardNum):
    try: # Tries to convert user inputted credit card number to integer to make sure that there are no letters
        int(cardNum)
    except: # If an error occurs usually because there are letters present, returns false
        return False
    else:
        z = 0 # sets z to zero
        for k in cardNum: # goes through every character in cardNum
            z+=1 # accumulates for every iteration
        if z < 9:
            return False # returns false if there are less than 9 characters
        initialNum = cardNum[::-1] # reverses cardNum and stores in initialNum
        sum1 = 0 # sets sum1 to zero
        x = 0 # sets x to zero
        for i in initialNum: # goes through every character in initialNum
            if x % 2 == 0: # checks if physical iteration number is even / odd digit place
                sum1 += int(initialNum[x]) # indexes the iteration number to add to sum
            x += 1 # accumulates for every iteration
        sum2 = 0 # sets sum2 to zero
        y = 0 # sets y to 0
        for j in initialNum: # goes through every character in initialNum
            if y % 2 != 0: # checks if physical iteration number is odd / even digit place
                if int(initialNum[y])*2 <= 9: # indexes the iteration number, multiplies by two and checks if greater than 9
                    sum2 += int(initialNum[y])*2 # if less than 9, adds number to sum
                else: # if greater than 9...
                    tempNum = str(int(initialNum[y])*2) # store product in tempNum as string
                    sum2 += int(tempNum[0]) + int(tempNum[1]) # add the first index and the second index and add partial sum to sum2
            y += 1 # accumulates for every iteration
        sumT = str(sum1 + sum2) # adds both sums of odd digit places and even digit places
        if sumT[-1] == "0": # checks if the last digit is zero
            return True # if true returns true
        else:
            return False # if false returns false


def enterCustomerInfo():
    fName = str(input("Enter first name: ")) # Asks user for name
    lName = str(input("Enter last name: ")) # Asks user for last name
    city = str(input("Enter city name: ")) # Asks user for city name
    while True:
        pCode = str(input("Enter postal code: ")) # Asks user for postal code
        if validatePostalCode(pCode): # Calls postal code validation function and returns true or false
            break # Exits while loop if postal code is valid
        print("Invalid postal code. Try again.\n") # Tells user the postal code is invalid
    while True: 
        ccNum = str(input("Enter credit card number: ")) # Asks user for credit card number
        if validateCreditCard(ccNum): # Calls credit card validation function and returns true or false
            break # Exits while loop if postal code is valid
        print("Invalid credit card number. Try again.\n") # Tells user the credit card number is invalid
    infos = (fName+"|"+lName+"|"+city+"|"+pCode+"|"+ccNum) # concatenates all information separated by delimiter |
    return infos


def generateCustomerDataFile():
    NameOfFile = str(input("Enter name of file: ")) # asks user for name of file
    fileLocation = str(input("Enter location of file: ")) # asks user for location/path of file
    fileName = fileLocation+NameOfFile+".csv" # sets file name to path with custom name and sets file type to csv
    try:
        userFile = open(fileName, "a") # tries to open file in append mode usually will not work because it does not exist
        userFile.writelines(totalInfo) # appends totalInfo to file
    except:
        userFile = open(fileName, "w") # creates file in write mode
        userFile.writelines(totalInfo) # writes totalInfo to file
    finally:
        userFile.close() # always closes file

####################################################################
#       ADDITIONAL METHODS MAY BE ADDED BELOW IF NECESSARY         #
####################################################################




####################################################################
#                            MAIN PROGRAM                          #
#           DO NOT EDIT ANY CODE EXCEPT WHERE INDICATED            #
####################################################################

# Do not edit any of these variables
userInput = ""
enterCustomerOption = "1"
generateCustomerOption = "2"
exitCondition = "9"

# More variables for the main may be declared in the space below


while userInput != exitCondition:
    printMenu()                 # Printing out the main menu
    userInput = input();        # User selection from the menu

    if userInput == enterCustomerOption:
        # Only the line below may be editted based on the parameter list and how you design the method return
        # Any necessary variables may be added to this if section, but nowhere else in the code
        totalInfo = enterCustomerInfo() # sets totalInfo to value returned by enterCustomerInfo

    elif userInput == generateCustomerOption: 
        # Only the line below may be editted based on the parameter list and how you design the method return
        try:
            generateCustomerDataFile() # tries to generate file
        except NameError: # if NameError occurs because enterCustomerInfo has not been called before and totalInfo has no value
            print("Please enter customer info first") # tells user to enter customer info prior to generating file

    elif userInput == exitCondition: # checks if userInput is 9 (exitCondition)
        continue # goes to next iteration of loop where the comparison is false to exit loop

    else:
        print("Please type in a valid option (A number from 1-9)")

#Exits once the user types 
print("Program Terminated")