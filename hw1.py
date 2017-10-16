#!/usr/bin/env python3

recDB = open('records.txt', 'r')


#class User(curr):

#    def __init__(self, name, currencies):
#        self.name = name
#        self.currencies = currencies
#
#    def convert(currency):
#        #converts user balance to new currency
#        #CANNOT convert if desired converstion is greater than balance
#
#    def newCurr(currency):
#        #Adds a new currency to the user's account
#
#    def details():
#        #prints out the user name and all currencies in that users possesion

def ClearList(recList):
    for j in range(0, len(recList)):
        recList[j] = recList[j].replace("\n", "")
    return recList

def add_to_amount(array, amt):
    if(array[1].isdigit()):
        new_val = int(array[1]) + amt
        array[1] = str(new_val)
        return array
    else:
        print("WARNING: {} is not an integer".format(array[1]))
        return []

def UserMenu(userData):

    currDB = open('newcurr.txt', 'r')
    currList = list(currDB)
    newCurrList = []
    currency, inTheCurrency, reverse, toWhere  = [], [], [], []

    for i in range(0, len(currList)):
        newCurrList.append(currList[i].split())

    #Curr1 to Standard the from Standard
    for j in range (0, len(currList)):
        currency.append(newCurrList[j][0])
        inTheCurrency.append(newCurrList[j][-3])
        reverse.append(newCurrList[j][-2])
        toWhere.append(newCurrList[j][-1])

    choice = 0
    convertFrom = ''
    convertFromValue = 0
    total = 0

    print('What would you like to do?')
    while choice != 4:
        print('1. MAINT')
        print('2. ADD FUNDS')
        print('3. TAKE FUNDS')
        print('4. EXIT')
        choice = int(input())
        if choice == 1:
            print('What currency would you like to convert?')
            print('EX: USD, JPY, GBP')
            convertFrom = str(input())
            print (float(toDict[convertFrom]))
            convertFromValue = (float(toDict[convertFrom]))
            print('What currency would you like to convert to?')
            convertTo = str(input())
            convertToValue = float(fromDict[convertTo])
            print(convertToValue)
            print('What amount would you like to convert?')
            amount = float(input())
            convertAmount = amount * convertFromValue
            total = convertAmount * convertToValue
            print("Converting " + str(amount) + " " + convertFrom + "To " + convertTo)
            print("The final value is: " + str(total))

        elif choice == 2:
            userInput = input('Please enter an amout: ')
            add_to_amount(userData[1],int(userInput))
            print(userData[1])

        elif choice == 3:
            print('Goodbye')
        elif choice == 4:
            print('Goodbye')
        else:
            print('Invalid Entry')

    return userData
    currDB.close()

def UserFind(recList, user):
    uFound = 0
    findList = []
    findingNumber = 0
    for i in range(0, len(recList)):
        findList.append(recList[i].split())
        if user == str(findList[i][0]):
            uFound = 1
            findingNumber = i;

    if uFound == 1:
        print('Welcome ' + user)
        print('You currently have ' + findList[findingNumber][1] + ' '+ findList[findingNumber][2])
        UserMenu(findList[findingNumber])
    else:
        print('User not found')
        print('Would you like to add yourself as a user?')
        print('y/n?')
        newUser = str(input()).lower()
        if newUser == 'y':
            print('Enter new User Name')
            newUserName = str(input())
            exitCode = 0;
            while exitCode is not 1:
                typeOfCurrency = str(input('Please type in the currency (either USD, JPY, or PHP): '))
                if typeOfCurrency != 'USD' and typeOfCurrency != 'JPY' and typeOfCurrency != 'PHP':
                    print('Not a valid type of currency. please input either USD, JPY, PHP as the correct term')
                else:
                    exitCode = 1

            print('Would you like to add funds to your account? y/n')
            newUser = str(input()).lower()
            if newUser == 'y':
                theAmount = input('How much would you like to add in ' + typeOfCurrency + '?: ');
            else:
                theAmount = '0'
            recList.append(newUserName +' '+ theAmount+ ' ' + typeOfCurrency)
            print('Thank you, that will be the end of this transaction. Good bye')
        if newUser == 'n':
            print('Goodbye')

    return recList


def main():


    recDB = open('records.txt', 'r')


    print('Welcome to the Financial Calculator')
    #print('Enter your user name')

    user = str(input('Enter your user name\n'))
    recList = list(recDB)
    uFound = 0

    recList = ClearList(recList)
    UserFind(recList, user)

    recDB = open('records.txt', 'w')
    for x in range(len(recList)):
        recDB.write(str(recList[x]) + '\n')

    recDB.close()

if __name__ == "__main__":
    main()
