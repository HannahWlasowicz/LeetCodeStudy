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


service = discovery.build('sheets', 'v4', credentials=creds)
spreadsheet_id = '1YXMMcs73sIU5qZfDkGywbCXyeAXrOImGtWX-xYcMZac'  # TODO: Update placeholder value.

ranges = ["170Questions!G2:G3"]  # TODO: Update placeholder value.

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
	count += 1