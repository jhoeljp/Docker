from Postgres_db import *
from OTE import OTE_Data
from pandas import DataFrame

if __name__ == '__main__': 
     
    try:
        #Pandas Data Frame
        OTE_data_obj = OTE_Data()
        

        #OTE start date
        OTE_data_obj.set_start_date(day=16,month=6,year=2021)
        OTE_data_obj.set_end_date(day=18,month=6,year=2021)
        # OTE_data_obj.set_start_date(day=1,month=8,year=2023)
        OTE_data_obj.print_start_and_end()

        #Download data
        ote_df = OTE_data_obj.get_historical_data()

        #sql object for populating database 
        sql = Postgres_db()

        #populate database with dataframe 
        sql.populate_database(ote_df)
        
    #TODO: Catch exach exception separately 
    except Exception as ex:
        print(f"Exception: {ex}")