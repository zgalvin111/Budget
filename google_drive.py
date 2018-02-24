import gspread
from oauth2client.service_account import ServiceAccountCredentials


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
    fullText = "You have spent " + str(fullSum) + " out of " + str(full100)
    print(fullText)
    return fullText

# Integrate a loop that goes through an graps the last value before it is zeros
# then pretiffy the data
# then build Update function 
