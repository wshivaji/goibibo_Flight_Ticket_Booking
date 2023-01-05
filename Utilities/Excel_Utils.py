import openpyxl
import pandas as pd


def read_csv():
    try:

        df = pd.read_csv('.//Test_Data//traveller_information.csv')
        print(df)
        x = df.shape
        counter = len(df)
        print(counter)
        print(x)
        rowLabels = df.index.tolist()
        col_names = df.columns.values
        print(col_names)
    except Exception as ex:
        print(ex)


class get_traveller_info:
    pass


read_csv()


def getRowCount(file, sheetName):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheetName]
    return sheet.max_row


def getColumnCount(file, sheetName):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheetName]
    return sheet.max_column


def readData(file, sheetName, row_num, column_num):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheetName]
    return sheet.cell(row=row_num, column=column_num).value


def writeData(file, sheetName, row_num, column_num, data):
    workbook = openpyxl.load_workbook(file)
    sheet = workbook[sheetName]
    sheet.cell(row=row_num, column=column_num).value = data
    workbook.save(file)
