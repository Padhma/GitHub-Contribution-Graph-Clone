import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_file = os.path.join(SITE_ROOT,'static', 'Client_Secret.json')
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name(json_file, scope)
client = gspread.authorize(creds)

sheet = client.open('Daily Contribution').sheet1

def getLevel():
    date = sheet.col_values(1, value_render_option='FORMATTED_VALUE')
    task = sheet.col_values(2, value_render_option='FORMATTED_VALUE')
    numberOfTasks = sheet.col_values(3, value_render_option='FORMATTED_VALUE')
    level = sheet.col_values(4, value_render_option='FORMATTED_VALUE')
    data = [date, task, level]
    return data
