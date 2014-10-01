import csv
import os
import xlrd

current_dir = os.path.dirname(os.path.realpath(__file__))
para_dir = os.path.abspath(os.path.join(current_dir, os.pardir))

#
# File Actions
#
def coerce_file_to_csv(filename, multiple_files=True):
    pass

#
# Workbook Actions
#
def open_workbook(path):
    return xlrd.open_workbook(path)

def list_sheets_by_name(workbook):
    return workbook.sheet_names()

def load_sheet_by_name(workbook, sheet_name):
    return workbook.sheet_by_name(sheet_name)

def coerce_workbook_to_csv(workbook):
    pass

#
# Sheet Actions
#
def coerce_sheet_to_csv(sheet, filename=None):
    
    scroll_through_columns(sheet)
    '''
    if filename is None:
        filename = sheet.name + ".csv"
    with open(filename, 'wb') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for rownum in list(range(sheet.nrows)):
            print sheet.row_values(rownum)
            writer.writerow(sheet.row_values(rownum))
    '''
def scroll_through_columns(sheet):
    for column_number in list(range(sheet.ncols)):
        print is_column_empty(sheet.col_values(column_number))

def is_column_empty(column):
    column_values = list(set(column))
    return (('' in column_values) and (len(column_values) == 1))

def clear_empty_rows():
    print
