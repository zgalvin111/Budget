import gspread
from oauth2client.service_account import ServiceAccountCredentials
from string import ascii_lowercase

# returns a float
def getFullSum():
    # use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name('google_cred.json', scope)
    client = gspread.authorize(creds)

    # Find a workbook by name and open the first sheet
    # Budget, Info, Prices
    file = client.open("Python Budget")
    worksheet = file.worksheet("Info")

    # Extract and print all of the values
    # list_of_hashes = worksheet.get_all_records()
    fullSum = worksheet.acell('G7').value
    full100 = worksheet.acell('G8').value
    fullText = float(full100) - float(fullSum)
    return fullText

def getBudget():
    # use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds']
    creds = ServiceAccountCredentials.from_json_keyfile_name('google_cred.json', scope)
    client = gspread.authorize(creds)

    # Find a workbook by name and open the first sheet
    # Budget, Info, Prices
    file = client.open("Python Budget")
    worksheet = file.worksheet("Budget")

    # lastCell is used to hold the last value and then counter is used to calculate
    # when I need to add a second letter
    lastCellValue = ""
    lastCell = ""
    counter = 0
    for c in ascii_lowercase:
        cell = c + str(1)
        value = worksheet.acell(cell).value
        counter = counter + 1
        if float(value) == 0.00:
            cellNumber = ord(c) - 1
            lastCell = str(chr(cellNumber)) + str(1)
            lastCellValue = worksheet.acell(lastCell).value
            break
    return float(lastCellValue)

def beautifulBudget():
    fullSum = getFullSum()
    weekBudget = 100 - getBudget()

    formatedBudget = "Week Budget : " + str(weekBudget) + "\n" + "Full Budget: " + str(fullSum)

    return formatedBudget
