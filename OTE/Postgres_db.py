import psycopg2 
import psycopg2.extras
import config 
from OTE import OTE_Data
from pandas import DataFrame

class Postgres_db():

    def __init__(self) -> None:
        pass

    def populate_database(self, dataframe:DataFrame) -> None:
        print('Populate databse begin!')

        #Establish connection with postgres Data base 
        connection = psycopg2.connect(host=config.DB_HOST,
                                      database=config.DB_NAME,
                                      user=config.DB_USER,
                                      password=config.DB_PASSWORD)
        
        cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

        if not dataframe.empty:

            #parse through entire dataset 
            for _,row in dataframe.iterrows():

                try:
                    #convert date type from timestamp to datetime
                    final_date = row['Date'].to_pydatetime()

                    #form query 
                    cursor.execute("""INSERT INTO ote_records (day_hour,price,amount,export,import,balance,record_date)
                                    VALUES (%s, %s, %s,%s,%s,%s,CAST(%s AS timestamp));
                                    """,(row['Day_hour'],row['Price'],row['Amount'],row['Export'],row['Import'],row['Balance'],final_date))
                    
                    print("Insert into ote_records")

                except Exception as e:
                    print(f'INSERT QUERY FAILED! {e}') 

        #TODO: raise exception
        else:
            print('ote data is empty !')

        #commit changes to database 
        connection.commit()

        #close database connection
        connection.close()        