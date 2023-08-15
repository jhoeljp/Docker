from Postgres_db import *
from OTE_Data import *
from time import sleep

if __name__ == '__main__': 

    #Repeat 

    while True:
        print("Checking to update db")

        #object for talking psql database 
        sql = Postgres_db()

        #object to get clean/valid data
        OTE_data_obj = OTE_Data()

        # db not empty 
        if sql.ote_fetch:
            print(f"latest date updated was {sql.latest_recorded_date}")
            OTE_data_obj.start_date = sql.latest_recorded_date
            
        # db empty  
        # else:  
            #Set historical download start/end date
            # OTE_data_obj.set_start_date(day=1,month=6,year=2021)
            # OTE_data_obj.set_end_date(day=13,month=8,year=2023)

        try:

            if OTE_data_obj.start_date != OTE_data_obj.end_date:
                #TODO: missing todays date so it has to run again and downlaod the latest 
                OTE_data_obj.print_start_and_end()

                #Download data
                ote_df = OTE_data_obj.get_historical_data() 

                #populate database with dataframe 
                sql.populate_database(ote_df)
            else:
                print(f"{OTE_data_obj.start_date} is the most up to date! ")
            
        #TODO: Catch exach exception separately 
        except Exception as ex:
            print(f"Exception: {ex}")


        #timeout 
        sleep(60)