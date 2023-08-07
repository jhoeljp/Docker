import pandas as pd
import requests
from datetime import datetime, timedelta
from io import BytesIO

'''
1. Download historical data for the month
2. Download todays day 
'''

class OTE_Data:

    default_date = datetime(2022,6,8)

    def __init__(self) -> None:
        self.base_url = "https://www.ote-cr.cz/pubweb/attachments"

        #first date known for dateset
        self.OTE_UPDATE_TIME_CET = 15

        #first date known for dateset
        self.start_date = OTE_Data.default_date
        self.end_date = datetime.today()

        self.set_default_end_date()

    def print_start_and_end(self):
      print(f"start date: {self.start_date.day} of  {self.start_date.strftime('%B')} {self.start_date.year}")
      print(f"end date: {self.end_date.day} of  {self.end_date.strftime('%B')} {self.end_date.year}")

    def set_start_date(self, day: int, month: int, year: int) -> None:
        self.start_date = datetime(year,month,day)

    def set_end_date(self, day: int, month: int, year: int) -> None:
        self.end_date = datetime(year,month,day)

    def set_default_end_date(self) -> None:
        #OTE document get updated everyday 15:00 Central European Time
        date_today = datetime.now()

        if date_today.hour < self.OTE_UPDATE_TIME_CET:
            date_today = date_today - timedelta(days=1)

        self.end_date = datetime(date_today.year,date_today.month,date_today.day)

    # Function to download and process the xls file
    def get_data(self, date: datetime) -> pd.DataFrame:

      url = ""
      try:
          # Create the URL
          url = f"{self.base_url}/01/{date.year}/month{str(date.month).zfill(2)}/day{str(date.day).zfill(2)}/DT_{str(date.day).zfill(2)}_{str(date.month).zfill(2)}_{date.year}_CZ.xls"
          print(url)

          # Download the xls file
          response = requests.get(url)

          if response.status_code != 200:
              print(f"Error {response.status_code} | Failed to download data . URL: {url}")
              response.raise_for_status()

          # Load the data into a pandas DataFrame
          data = pd.read_excel(BytesIO(response.content), header=4, usecols="A:F", nrows=25)

          #create new column date
          #fix Date column to hold correct datetime string with
          data['Date'] = date

          return data

      except Exception as e:
        print(f"Could not download data from link: {e}")
        print(url)

      return None

    # Function to download data
    def download_data(self, start_date : datetime, end_date : datetime) -> pd.DataFrame:
        # Create a date range
        dates = pd.date_range(start_date, end_date)

        # Initialize an empty DataFrame to store all data
        all_data = pd.DataFrame()

        # Get data for each date in the range
        for date in dates:

            data = self.get_data(date)

            #Check for filled dataframe 
            if not data.empty:
                # print(f"Dataframe not empty, shape:{data.shape}")
                data = data.dropna()

                if data is not None:

                    #fix Date column to hold correct datetime string with Day hour value
                    tmp_hour = 0

                    for col_date in data['Date']:
                        new_date = col_date.replace(hour= tmp_hour,minute=0,second=0)
                        col_date = new_date.isoformat(" ", "seconds")
                        data.loc[tmp_hour+1, 'Date'] = col_date

                        tmp_hour+=1

                #re-arrange columns for dataframe until date 08.06.2022 to most updated column format
                #dataset specific date
                if date <= OTE_Data.default_date:

                    #rename column to up to date convention
                    data = data.rename(columns = {'Hodina':'Day_hour', 'Cena (EUR/MWh)':'Price', 'Množství\n(MWh)':'Amount','Saldo DT\n(MWh)':'Balance','Export\n(MWh)':'Export','Import\n(MWh)':'Import'}, inplace = True)

                    data = data[['Day_hour', 'Price', 'Amount','Balance','Export','Import']]


                #from 09.06.2023 no switch of columns from database schema
                else:
                    #Rename columns from czech to english
                    data = data.rename(columns = {'Hodina':'Day_hour', 'Cena (EUR/MWh)':'Price', 'Množství\n(MWh)':'Amount','Saldo':'Balance'}, inplace = False)

                # print(data)
                #append new data to dataframe
                all_data = pd.concat([all_data, data])
            else:
                print(f"Dataframe for date:{date} is empty ! ")
                print(data)

        return all_data

    #Download data from starting date to todays date
    def get_df_data(self) -> pd.DataFrame:

        return self.download_data(self.start_date,self.end_date)

    #Download data from yesterday
    def get_yesterdays_data(self) -> pd.DataFrame:

        yesterday = datetime.today() - timedelta(days=1)
        return self.download_data(yesterday,yesterday)

    #Download all existing data available
    def get_historical_data(self) -> pd.DataFrame:
        #first date known
        # start_date = OTE_Data.default_date

        return self.download_data(self.start_date,self.end_date)
