import os
from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient import discovery
import json

creds = None
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SERVICE_ACCOUNT_FILE = 'keys.json'
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)


service = discovery.build('sheets', 'v4', credentials=creds)
spreadsheet_id = '1YXMMcs73sIU5qZfDkGywbCXyeAXrOImGtWX-xYcMZac'  # TODO: Update placeholder value.

ranges = ["170Questions!G2:G171"]  # TODO: Update placeholder value.

include_grid_data = True  # TODO: Update placeholder value.

request = service.spreadsheets().get(spreadsheetId=spreadsheet_id, ranges=ranges, includeGridData=include_grid_data)
response = request.execute()
values = response['sheets'][0]['data'][0]['rowData']
count = 0
easy = []
medium = []
hard = []
for row in values:
    link = row['values'][0]['hyperlink']
    if count < 35:
        easy.append(link)
    elif count <140:
        medium.append(link)
    else:
        hard.append(link)
    # else:
    #     print(row)
    #     print(count)
    count += 1
    

print(len(easy))
print(len(medium))
print(len(hard))

sheet = service.spreadsheets()
result = sheet.values().get(spreadsheetId=spreadsheet_id,
                        range="170Questions!A2:A171").execute()
values = result.get('values')

retVal = {'easy': [], 'medium': [], 'hard':[]}


count = 0
midx = 0
hidx = 0

for val in values:
    val = val[0]
    words = val.split(".")
    categories = words[1][1:].split("/")

    if count <35:
        item = {'link':easy[count], 'categories':categories}
        retVal['easy'].append(item)
    elif count<140:
        item = {'link':medium[midx], 'categories':categories}
        retVal['medium'].append(item)
        midx+=1
    else:
        item = {'link':hard[hidx], 'categories':categories}
        retVal['hard'].append(item)
        hidx+=1
    count += 1

print(len(retVal['easy']))

with open('data.txt', 'w', encoding='utf8') as outfile:
    json.dump(retVal, outfile)