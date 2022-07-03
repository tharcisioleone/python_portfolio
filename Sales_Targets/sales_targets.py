# Author: Tharcisio Leone #
# Dataset: Targets of Sales #

## Maschine Learning using openpyxl and twilio.
# 0. Importing Libraries.
# 1. Opening the six files in Excel containing the sales values per salesperson.
# 2. Evaluating the values of sales.
# 3. Sending SMS with the message of target achieving reporting the month, salesperson and value.


# 0. Importing Libraries.
import pandas as pd
from twilio.rest import Client


# See: https://www.twilio.com/docs/libraries/python

# Copy and paste from homepage
# My Account SID from twilio.com/console
account_sid = "AC2a465d6668cd63f1d30b7ac11f206aa8"
# My Auth Token from twilio.com/console
auth_token  = "7ee8f2f490b0485d21da16cb87ff0f9f"
client = Client(account_sid, auth_token)


# 1. Opening the six files in Excel containing the sales values per salesperson.
list_months = ['january', 'february', 'march', 'april', 'may', 'june']

for months in list_months:
    #print(months)
    table_sales = pd.read_excel(f'{months}.xlsx')
    #print(table_sales)
    if (table_sales['Values'] > 55000).any(): # 2. Evaluating the values of sales
        salesperson = table_sales.loc[table_sales['Values'] > 55000, 'Salesperson'].values[0]
        values = table_sales.loc[table_sales['Values'] > 55000, 'Values'].values[0]
        print(f'In month {months} the target was achieved. Salesperson: {salesperson}. Value: {values}.')
        message = client.messages.create( # 3. Sending SMS with the message of target achieving reporting the month, salesperson and value.
            to="+4917681703460",
            from_="+19707143233",
            body=f'In month {months} the target was achieved. Salesperson: {salesperson}. Value: {values}.')
        print(message.sid)




