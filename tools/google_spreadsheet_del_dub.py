"""
    Dummy delete of duplicate lines in google spreadsheet.
"""
import gspread
from oauth2client.service_account import ServiceAccountCredentials as ServiceAC


def main():
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    credentials = ServiceAC.from_json_keyfile_name('gspread.json', scope)

    gc = gspread.authorize(credentials)

    # Open a worksheet from spreadsheet with one shot
    worksheet = gc.open("hacker-laws-ru-readme.md").sheet1
    deleted = True
    while deleted:
        deleted = False
        values_list = worksheet.col_values(1)
        values = set()
        for i, value in enumerate(values_list, 1):
            if value not in values:
                values = values.union({value})
            elif value != 'orig' and value:
                worksheet.delete_row(i)
                deleted = True
                break


if __name__ == '__main__':
    main()
