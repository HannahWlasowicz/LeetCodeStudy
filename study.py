import os
from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient import discovery
from pprint import pprint



creds = None
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
SERVICE_ACCOUNT_FILE = 'keys.json'
creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
# The ID and range of a sample spreadsheet.
# SAMPLE_SPREADSHEET_ID = '1YXMMcs73sIU5qZfDkGywbCXyeAXrOImGtWX-xYcMZac'
# service = build('sheets', 'v4', credentials=creds)
# # Call the Sheets API
# sheet = service.spreadsheets()
# result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
#                             range="170Questions!A1:G10", valueRenderOption='FORMULA').execute()
# values = result.get('values', [])




service = discovery.build('sheets', 'v4', credentials=creds)
spreadsheet_id = '1YXMMcs73sIU5qZfDkGywbCXyeAXrOImGtWX-xYcMZac'  # TODO: Update placeholder value.

ranges = ["170Questions!G2:G3"]  # TODO: Update placeholder value.

# True if grid data should be returned.
# This parameter is ignored if a field mask was set in the request.
include_grid_data = True  # TODO: Update placeholder value.

request = service.spreadsheets().get(spreadsheetId=spreadsheet_id, ranges=ranges, includeGridData=include_grid_data)
response = request.execute()
values = response['sheets'][0]['data'][0]['rowData']
for row in values:
    test = row['values']
    for val in test:
        print(val['hyperlink'])
# print(values)
# pprint(response)
# print(values)
# print(values[2][6])
# # sentences = []
# for val in values:
#     if len(val) > 0:
#         sentences.append(val[0])
# df = px.data.gapminder().query("continent=='Oceania'")

