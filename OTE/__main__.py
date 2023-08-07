from Postgres_db import *
from OTE import OTE_Data
from pandas import DataFrame

def get_historical_data(OTE_data_obj: OTE_Data) -> DataFrame:
    return OTE_data_obj.get_historical_data()

def get_yesterday_data(OTE_data_obj: OTE_Data) -> DataFrame:
    return OTE_data_obj.get_yesterdays_data()

if __name__ == '__main__': 
     
    try:
        #Pandas Data Frame
        OTE_data_obj = OTE_Data()

        # OTE_data_obj.set_start_date(day=1,month=6,year=2022)
        OTE_data_obj.set_start_date(day=1,month=1,year=2023)
        OTE_data_obj.set_start_date(day=1,month=4,year=2023)

        ote_df = get_historical_data(OTE_data_obj)
        # ote_df = get_yesterday_data(OTE_data_obj)

        #sql object for populating database 
        sql = Postgres_db()

        #populate database with dataframe 
        sql.populate_database(ote_df)
        
    #TODO: Catch exach exception separately 
    except Exception as ex:
        print(f"Exception: {ex}")