#!/usr/bin/env python3
import getpass
from passlib.hash import pbkdf2_sha256
recDB = open('records.txt', 'r')

def ClearList(recList):
    for j in range(0, len(recList)):
        recList[j] = recList[j].replace("\n", "")
    return recList
# Why did i make this...... O this was a template on adding stuff to an account
# def wonderLust(array):
#     if(array[1].isdigit()):
#         new_val = int(array[1]) + 0
#         array[1] = str(new_val)
#         return array
#     else:
#         print("WARNING: {} is not an integer".format(array[1]))
#         return []

def add_to_amount(array, amt):
    if(array[1].isdigit()):
        new_val = int(array[1]) + amt
        array[1] = str(new_val)
        return array
    else:
        print("WARNING: {} is not an integer".format(array[1]))
        return []

def sub_to_amount(array, amt):
    if(array[1].isdigit()):
        new_val = int(array[1]) - amt
        array[1] = str(new_val)
        return array
    else:
        print("WARNING: {} is not an integer".format(array[1]))
        return []

def currencyExchange(userData):
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


    # choice = 0
    convertFrom = ''
    convertFromValue = 0
    total = 0

    print('What currency would you like to convert to?')
    print('EX: USD, JPY, PHP')
    print('you are currently using: '+userData[2])
    convertFrom = str(input()).upper()
    exitCurrency = 0
    while exitCurrency != 1:
        if userData[2] == 'USD':
            if convertFrom == 'USD':
                print('No change')
            elif convertFrom == 'JPY':
                for i in range(0, len(currency)):
                    if currency[i] == 'JPY' and toWhere[i] == 'toUSD':
                        calculations = 0
                        calculations = int(userData[1]) * float(inTheCurrency[i])
                        print('You would be at '+ str(calculations) + ' YEN or JPY')
                        # print( calculations + 'Yen or JPY')

            elif convertFrom == 'PHP':
                for i in range(0, len(currency)):
                    if currency[i] == 'PHP' and toWhere[i] == 'toUSD':
                        calculations = 0
                        calculations = int(userData[1]) * float(inTheCurrency[i])
                        print('You would be at '+ str(calculations) + ' Peso or PHP')
            exitCurrency = 1
        # JAPANESE EXCHANGE
        elif userData[2] == 'JPY':
            if convertFrom == 'USD':
                for i in range(0, len(currency)):
                    if currency[i] == 'USD' and toWhere[i] == 'toYen':
                        calculations = 0
                        calculations = int(userData[1]) * float(inTheCurrency[i])
                        print('You would be at '+ str(calculations) + ' USD or Dollars')
                        # print( calculations + 'Yen or JPY')
            elif convertFrom == 'JPY':
                print('No change')
            elif convertFrom == 'PHP':
                for i in range(0, len(currency)):
                    if currency[i] == 'PHP' and toWhere[i] == 'toYen':
                        calculations = 0
                        calculations = int(userData[1]) * float(inTheCurrency[i])
                        print('You would be at '+ str(calculations) + ' Peso or PHP')
            exitCurrency = 1
        elif userData[2] == 'PHP':
            if convertFrom == 'USD':
                for i in range(0, len(currency)):
                    if currency[i] == 'USD' and toWhere[i] == 'toPHP':
                        calculations = 0
                        calculations = int(userData[1]) * float(inTheCurrency[i])
                        print('You would be at '+ str(calculations) + ' USD or Dollars')
                        # print( calculations + 'Yen or JPY')
            elif convertFrom == 'JPY':
                for i in range(0, len(currency)):
                    if currency[i] == 'JPY' and toWhere[i] == 'toPHP':
                        calculations = 0
                        calculations = int(userData[1]) * float(inTheCurrency[i])
                        print('You would be at '+ str(calculations) + ' Yen or JPY')
            elif convertFrom == 'PHP':
                print('No change')
            exitCurrency = 1
        else:
            print('Not a valid input')

def currencyExchangeCalculator(userData,toChangeTo, amount):
    toReturn = 0
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


    convertFrom = ''
    convertFromValue = 0
    total = 0

    convertFrom = toChangeTo
    exitCurrency = 0
    while exitCurrency != 1:
        # USD Exchange
        if userData[2] == 'USD':
            if convertFrom == 'USD':
                # print('No change')
                toReturn = int(amount)
            elif convertFrom == 'JPY':
                for i in range(0, len(currency)):
                    if currency[i] == 'JPY' and toWhere[i] == 'toUSD':
                        calculations = 0
                        calculations = int(amount) * float(inTheCurrency[i])
                        toReturn = calculations
            elif convertFrom == 'PHP':
                for i in range(0, len(currency)):
                    if currency[i] == 'PHP' and toWhere[i] == 'toUSD':
                        calculations = 0
                        calculations = int(amount) * float(inTheCurrency[i])
                        toReturn = calculations
            exitCurrency = 1
        # JAPANESE EXCHANGE
        elif userData[2] == 'JPY':
            if convertFrom == 'USD':
                for i in range(0, len(currency)):
                    if currency[i] == 'USD' and toWhere[i] == 'toYen':
                        calculations = 0
                        calculations = int(amount) * float(inTheCurrency[i])
                        toReturn = calculations
            elif convertFrom == 'JPY':
                # print('No change')
                toReturn = int(amount)
            elif convertFrom == 'PHP':
                for i in range(0, len(currency)):
                    if currency[i] == 'PHP' and toWhere[i] == 'toYen':
                        calculations = 0
                        calculations = int(amount) * float(inTheCurrency[i])
                        toReturn = calculations
            exitCurrency = 1
        # PHP Exchange
        elif userData[2] == 'PHP':
            if convertFrom == 'USD':
                for i in range(0, len(currency)):
                    if currency[i] == 'USD' and toWhere[i] == 'toPHP':
                        calculations = 0
                        calculations = int(amount) * float(inTheCurrency[i])
                        toReturn = calculations
            elif convertFrom == 'JPY':
                for i in range(0, len(currency)):
                    if currency[i] == 'JPY' and toWhere[i] == 'toPHP':
                        calculations = 0
                        calculations = int(amount) * float(inTheCurrency[i])
                        toReturn = calculations
            elif convertFrom == 'PHP':
                # print('No change')
                toReturn = int(amount)
            exitCurrency = 1
        else:
            print('Not a valid input')
        return toReturn


def UserMenu(userData, recList):
    SendBack = []
    choice = 0
    exitCounter = 0
    print('What would you like to do?')
    while choice != 6 and exitCounter <= 6:
        print('1. MAINT')
        print('2. ADD FUNDS')
        print('3. TAKE FUNDS')
        print('4. DELETE USER')
        print('5. TRANSFER FUNDS')
        print('6. EXIT')
        choice = int(input())
        if choice == 1:
            currencyExchange(userData)
        elif choice == 2:
            userInput = input('Please enter an amout you want to add: ')
            userData = add_to_amount(userData,int(userInput))
            print('your new ammount is: '+userData[1])

        elif choice == 3:
            userInput = input('Please enter an amout you want to take away: ')
            userData = sub_to_amount(userData,int(userInput))
            print('your new ammount is: '+userData[1])
        elif choice == 4:
            userInput = input('Please enter a user you would like to delete: ')
            recList = UserDeleting(userInput, recList)
        elif choice == 5:
            transferedAccounts = []
            userInput = input('Please enter a user you would like to transfer funds to: ')
            transferAccount = accountFinding(recList,userInput)
            transferedAccounts = transferFunds(userData, transferAccount)
            # print(transferedAccounts)
        elif choice == 6:
            print('Goodbye')
            exitCounter = 6
        else:
            print('Invalid Entry or too many tries ')
            exitCounter += 1
    SendBack.append(userData)
    SendBack.append(recList)
    return SendBack
    currDB.close()

def transferFunds(toTransferFrom, toTransferTo):
    toReturn = []
    userAmountToGive = input('Please enter the amount you want to give: ')
    amountGive = currencyExchangeCalculator(toTransferFrom,toTransferTo[2],userAmountToGive)
    # print(amountGive)
    amountFrom = currencyExchangeCalculator(toTransferTo,toTransferFrom[2], amountGive)
    # print(amountFrom)
    toReturn = transferHelper(toTransferFrom, toTransferTo, userAmountToGive, amountGive)
    return toReturn

def transferHelper(toTransferFrom, toTransferTo, amoutToTakeAway, amountToGive):
    transferSendBack = []
    add_to_amount(toTransferTo, amountToGive)
    sub_to_amount(toTransferFrom, int(amoutToTakeAway))
    transferSendBack.append(toTransferFrom)
    transferSendBack.append(toTransferTo)
    return transferSendBack

def UserDeleting(userTobeDeleted,recList):
    finderNumber = 0
    for i in range(0, len(recList)):
        if userTobeDeleted == recList[i][0]:
            finderNumber = i
    if finderNumber != 0:
        userInput = input('We have found the droids you were looking for. are you sure you want to delete? (y/n) ')
        verifyInput = input('Are you sure? all funds in the account go back to the bank. (y/n) ')
    if userInput.upper() == verifyInput.upper():
        print('User has been deleted')
        recList[finderNumber:finderNumber+1] = []
    else:
        print('Verification failed. did not delete')
    return recList

def accountFinding(recList, userToBeFound):
    finderNumber = 0
    for i in range(0, len(recList)):
        if userToBeFound == recList[i][0]:
            return recList[i]

def UserIs(recList,user, password):
    hash = pbkdf2_sha256.hash(password)
    if user == str(recList[0]) and pbkdf2_sha256.verify(password,recList[3]) == True:
        return True

def UserFind(recList, user):
    uFound = 0
    findList = []
    findingNumber = 0
    x = getpass.getpass()
    isThisTheGuy = False
    for i in range(0, len(recList)):
        findList.append(recList[i].split())
        recList[i] = findList[i]
        isThisTheGuy = UserIs(findList[i],user, x)
        if isThisTheGuy == True:
            uFound = 1
            findingNumber = i;

    if uFound == 1:
        print('Welcome ' + user)
        print('You currently have ' + findList[findingNumber][1] + ' '+ findList[findingNumber][2])
        ListFinder = UserMenu(findList[findingNumber],findList)
        recList[findingNumber] = ListFinder[0]
        recList = ListFinder[1]
    else:
        print('User not found')
        print('Would you like to add yourself as a user?')
        print('y/n?')
        newUser = str(input()).lower()
        if newUser == 'y':
            print('Enter new User Name')
            newUserName = str(input())
            print('Enter new Password')
            newPassword = getpass.getpass()
            print('Verify new Password')
            VarifyPassword = getpass.getpass()
            if newPassword == VarifyPassword:
                newPassword = pbkdf2_sha256.hash(VarifyPassword)
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
                        tempList = [newUserName,theAmount,typeOfCurrency,newPassword]
                        ' '.join(tempList)
                        recList.append(tempList)
                        print('Thank you, that will be the end of this transaction. Good bye')
            else:
                print("Passwords did not match. Please try again at a later date.")
        if newUser == 'n':
            print('Goodbye')
    return recList


def main():
    recDB = open('records.txt', 'r')
    print('Welcome to the Financial Calculator')
    user = str(input('Enter your user name\n'))
    recList = list(recDB)
    uFound = 0
    recList = ClearList(recList)
    recList = UserFind(recList, user)
    recDB = open('records.txt', 'w')
    for x in range(0, len(recList)):
        recDB.write(' '.join(recList[x]) + '\n' )

    recDB.close()

if __name__ == "__main__":
    main()
