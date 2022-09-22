# import xlsxwriter module
import xlsxwriter

workbook = xlsxwriter.Workbook('Example3.xlsx')

# By default worksheet names in the spreadsheet will be
# Sheet1, Sheet2 etc., but we can also specify a name.
worksheet = workbook.add_worksheet("My sheet")

# Some data we want to write to the worksheet.
data = (
    ['ankit', 'moffi@gmail.com','1231231234','4.1','www.hehe.com'],
    ['rahul', 'moffi123@gmail.com','1521231234','4.6','www.nike.com'],

)

# Start from the first cell. Rows and
# columns are zero indexed.

worksheet.write('A1', 'Company_name')
worksheet.write('B1', 'Email')
worksheet.write('C1', 'Phone Number')
worksheet.write('D1', 'Google Rating')
worksheet.write('E1', 'Website')
# Iterate over the data and write it out row by row.

def saver(company_name, email, phone_number, google_rating, website):
    row = 1
    col = 0
    for company_name, email, phone_number, google_rating, website in (data):
        worksheet.write(row, col, company_name)
        worksheet.write(row, col + 1, email)
        worksheet.write(row, col + 2, phone_number)
        worksheet.write(row, col + 3, google_rating)
        worksheet.write(row, col + 4, website)
        row += 1

    workbook.close()


#data will be in format
