# Author: Tharcisio Leone #
# Dataset: Targets of Sales #

## Maschine Learning using openpyxl and twilio.
# 0. Importing Libraries.
# 1. Opening the six files in Excel containing the sales values per salesperson.
# 2. Evaluating the values of sales
# --> If the value is higher than 55.000, then send SMS reporting the month, salesperson and value.


# 0. Importing Libraries.
import pandas as pd


# 1. Opening the six files in Excel containing the sales values per salesperson.
list_months = ['january', 'february', 'march', 'april', 'may', 'june']

for months in list_months:
    print(months)
    table_sales = pd.read_excel(f'{months}.xlsx')
    print(table_sales)
    if (table_sales['Values'] > 55000).any():
        print('Yes, target has been achieved.')