# Throughout this project, the use of data structures are not permitted 
# Minimal built in functions are to be used and the majority of functions must be
# created yourself

# More packages may be imported in the space below if approved by your instructor
import os
print(os.getcwd())
folder = os.getcwd()

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

'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''
def enterCustomerInfo():
    global fName
    global lName
    global city
    global pCode
    global ccNum

    fName = str(input("Enter first name: "))
    lName = str(input("Enter last name: "))
    city = str(input("Enter city name: "))
    while True:
        pCode = str(input("Enter postal code: "))
        if validatePostalCode(pCode):
            break
        print("Invalid postal code. Try again.\n")
    while True:
        ccNum = str(input("Enter credit card number: "))
        if validateCreditCard(ccNum):
            break
        print("Invalid credit card number. Try again.\n")
    


'''
    This function is to be edited to achieve the task.
    It is your decision to make this function a procedural or functional type
    You may place as many or as few parameters as needed
    This function may also be broken down further depending on your algorithm/approach
'''
def validatePostalCode(code):
    PCfile = open("postal_codes.csv", "r")
    for i in PCfile:
        if i[:3] == code:
            PCfile.close()
            return True
    PCfile.close()
    return False


def validateCreditCard(cardNum):
    try:
        int(cardNum)
    except:
        return False
    else:
        z = 0
        for k in cardNum:
            z+=1
        if z < 9:
            return False
        initialNum = cardNum[::-1]
        sum1 = 0
        x = 0
        for i in initialNum:
            if x % 2 == 0:
                sum1 += int(initialNum[x])
            x += 1
        sum2 = 0
        y = 0
        for j in initialNum:
            if y % 2 != 0:
                if int(initialNum[y])*2 < 9:
                    sum2 += int(initialNum[y])*2
                else:
                    tempNum = str(int(initialNum[y])*2)
                    sum2 += int(tempNum[0]) + int(tempNum[1])
            y += 1
        sumT = str(sum1 + sum2)
        if sumT[-1] == "0":
            return True
        else:
            return False


def generateCustomerDataFile(firstName, lastName, cityName, postalCode, creditCard):
    NameOfFile = str(input("Enter name of file: "))
    fileName = NameOfFile+".txt"
    try:
        userFile = open(fileName, "a")
        userFile.writelines(firstName+"|"+lastName+"|"+cityName+"|"+postalCode+"|"+creditCard+"\n")
    except:
        userFile = open(fileName, "w")
        userFile.writelines(firstName+"|"+lastName+"|"+cityName+"|"+postalCode+"|"+creditCard+"\n")
    finally:
        userFile.close()

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
        enterCustomerInfo()

    elif userInput == generateCustomerOption: 
        # Only the line below may be editted based on the parameter list and how you design the method return
        generateCustomerDataFile(fName,lName, city, pCode, ccNum)

    else:
        print("Please type in a valid option (A number from 1-9)")

#Exits once the user types 
print("Program Terminated")