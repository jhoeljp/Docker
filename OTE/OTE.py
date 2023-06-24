import pandas as pd
import requests
from datetime import datetime
from io import BytesIO

'''
1. Download historical data for the month
2. Download todays day 
'''
URL = "https://www.ote-cr.cz/pubweb/attachments"

class OTE_Data:

    def __init__(self) -> None:
        self.base_url = URL

        #first date known for dateset 
        start_date = datetime(2022, 6, 8)

        #historical date range is default
        self.get_date(start_date.day, start_date.month, start_date.year)
        
    def __init__(self, day: int, month: int, year: int):
        self.base_url = URL
        self.get_date(day,month,year)
    
    def get_date(self,day: int, month: int, year: int) -> None:
        #OTE document get updated everyday 15:00 Central European Time
        date_today = datetime.now()

        if date_today.hour < 15:
            date_today.day -= 1

        self.end_date = datetime(date_today.year,date_today.month,date_today.day)
        self.start_date = datetime(year,month,day)

    # Function to download and process the xls file
    def get_data(self, date: datetime) -> pd.DataFrame:
        
        # Create the URL
        url = f"{self.base_url}/01/{date.year}/month{str(date.month).zfill(2)}/day{str(date.day).zfill(2)}/DT_{str(date.day).zfill(2)}_{str(date.month).zfill(2)}_{date.year}_CZ.xls"
        print(url)
        
        # Download the xls file
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Error {response.status_code} | Failed to download data . URL: {url}")
            response.raise_for_status()

        # Load the data into a pandas DataFrame
        data = pd.read_excel(BytesIO(response.content), header=4, usecols="A:F", nrows=27)
        # data = pd.read_excel(BytesIO(response.content), header=4, nrows=27)
        data['Date'] = date

        return data

    # Function to download data
    def download_data(self, start_date : datetime, end_date : datetime) -> pd.DataFrame:
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

    #Download data from starting date to todays date
    def get_df_data(self) -> pd.DataFrame:

        return self.download_data(self.start_date,self.end_date)
    
    #Download data from yesterday
    def get_yesterdays_data(self) -> pd.DataFrame:

        start_date = self.end_date
        start_date = start_date.day -1 

        return self.download_data(start_date,self.end_date)
    
    #Download all existing data available 
    def get_historical_data(self) -> pd.DataFrame:
        #first date known 
        start_date = datetime(2022, 6, 8)

        return self.download_data(start_date,self.end_date)