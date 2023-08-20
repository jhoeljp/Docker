import psycopg2 
import psycopg2.extras
from pandas import DataFrame
import os
from datetime import datetime

class Postgres_db():

    def __init__(self) -> None:

        #init database config
        self.host=os.environ['POSTGRES_HOST']
        self.port=int(os.environ['POSTGRES_PORT'])
        self.database=os.environ['POSTGRES_DB']
        self.user=os.environ['POSTGRES_USER']
        self.password=os.environ['POSTGRES_PASSWORD']

        #ote server update hour 
        self.ote_update_hour = 15

        #TODO: add table on higher layer
        max_date_query = f"select max(record_date) as max_date from ote_records;"

        #YYYY-MM-DD
        self.latest_recorded_date = self.database_fetchone(max_date_query)

        #determine if fetching specifications 
        self.ote_fetch = self.update_records(self.latest_recorded_date)

        print(f"Latest date on record: {self.latest_recorded_date}")


    def update_records(self,latest_date):

        #determine if fetching specifications 
        fetch = False
        
        latest_date = latest_date[0]

        #db has records 
        if latest_date != None:
            latest_date = datetime.strptime(str(latest_date), "%Y-%m-%d")
            self.latest_recorded_date = latest_date

            #is latest record up to date ? 
            self.date_today = datetime.now()

            #has not updated today or in the past ! 
            if latest_date <= self.date_today:
                fetch = True

                #db has been updated already 
                if latest_date == self.date_today:
                    fetch = False
                    

        return fetch


    def database_fetchone(self,query:str):
        result = None

        try:
            connection = psycopg2.connect(
            host=self.host,
            port=self.port,
            database=self.database,
            user=self.user,
            password=self.password
            )

            cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

            cursor.execute(query)

            # Fetch the result
            result = cursor.fetchone()  # Use fetchone() for a single row result or fetchall() for multiple rows

            # Close the cursor and the connection
            cursor.close()
            connection.close()

        except psycopg2.OperationalError as error:
            print("Could not connect to the PostgreSQL server: ", error)

        if result == "None":
            return None 
        
        return result


    def populate_database(self, dataframe:DataFrame) -> None:
        print('Populate database begin!')
        
        try:
            # Connect to the PostgreSQL server
            connection = psycopg2.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password
            )

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
                        print(row)
                        
            #commit changes to database 
            connection.commit()

            #close database connection
            connection.close() 

        #TODO: raise exception
        except psycopg2.OperationalError as error:
            print("Could not connect to the PostgreSQL server: ", error)
       