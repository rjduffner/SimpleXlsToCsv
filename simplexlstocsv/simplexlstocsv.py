import csv
import os
from xlrd import open_workbook


current_dir = os.path.dirname(os.path.realpath(__file__))

print current_dir
para_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
print para_dir

simple_xlsx_path = os.path.join(para_dir, 'tests', 'resources','simple.xlsx')

book = open_workbook(simple_xlsx_path)
print book.nsheets
for sheet_index in range(book.nsheets):
    print book.sheet_by_index(sheet_index)
    print book.sheet_names()

for sheet_name in book.sheet_names():
    print book.sheet_by_name(sheet_name)

for sheet in book.sheets():
    print sheet

import xlrd
import csv

def csv_from_excel():

    wb = xlrd.open_workbook(simple_xlsx_path)
    sh = wb.sheet_by_name('Sheet1')
    your_csv_file = open('your_csv_file.csv', 'wb')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    # Below is equal to reading out row by row
    for rownum in xrange(sh.nrows):
        print sh.row_values(rownum)
        wr.writerow(sh.row_values(rownum))

    your_csv_file.close()


csv_from_excel()

