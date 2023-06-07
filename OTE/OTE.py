import pandas as pd
import requests
from datetime import datetime
from io import BytesIO

'''
1. Download historical data for the month
2. Download todays day 
'''

class OTE_Data:

    def __init__(self):
        self.base_url = "https://www.ote-cr.cz/pubweb/attachments"

    # Function to download and process the xls file
    def get_data(self,date):
        # Create the URL
        
        url = f"{self.base_url}/01/{date.year}/month{str(date.month).zfill(2)}/day{str(date.day).zfill(2)}/DT_{str(date.day).zfill(2)}_{str(date.month).zfill(2)}_{date.year}_CZ.xls"
        print(url)
        
        # Download the xls file
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to download data. URL: {url}")
            return None

        # Load the data into a pandas DataFrame
        data = pd.read_excel(BytesIO(response.content), header=4, usecols="A:F", nrows=27)
        data['Date'] = date

        return data

    # Function to download data
    def download_data(self,start_date, end_date):
        # Create a date range
        dates = pd.date_range(start_date, end_date)

        # Initialize an empty DataFrame to store all data
        all_data = pd.DataFrame()

        # Get data for each date in the range
        for date in dates:
            data = self.get_data(date)
            if data is not None:
                all_data = pd.concat([all_data, data])

        #Rename columns from czech to english 
        all_data.rename(columns = {'Hodina':'Day_hour', 'Cena (EUR/MWh)':'Price', 'Množství\n(MWh)':'Amount','Saldo':'Balance'}, inplace = True)
        all_data = all_data.dropna()
        return all_data

    #Function to download date from starting date to todays date
    def get_historical_data(self):
        # Define the start and end dates
        start_date = datetime(2023, 1, 1)

        date_obj = datetime.now()
        end_year, end_day, end_month = date_obj.year , date_obj.day, date_obj.month
        end_date = datetime(end_year, end_month, end_day)  # for example, June 5, 2023

        return self.download_data(start_date,end_date)

    #Function to download todays date #after 3 pm czech time 
    def get_tomorrow_data(self):
        # Define the start and end dates
        #end_date == start_date

        date_obj = datetime.now()
        end_year, end_day, end_month = date_obj.year , date_obj.day, date_obj.month
        end_date = datetime(end_year, end_month, end_day+1)

        return self.download_data(end_date,end_date)
    def get_yesterdays_data(self):
        # Define the start and end dates
        #end_date == start_date

        date_obj = datetime.now()
        end_year, end_day, end_month = date_obj.year , date_obj.day, date_obj.month
        end_date = datetime(end_year, end_month, end_day-1)

        return self.download_data(end_date,end_date)