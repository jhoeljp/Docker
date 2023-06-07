import psycopg2 
import psycopg2.extras
import config 
from OTE import *

#Establish connection with postgres Data base 
connection = psycopg2.connect(host=config.DB_HOST,database=config.DB_NAME,user=config.DB_USER,password=config.DB_PASSWORD)
cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

#Data Class 
OTE_obj = OTE_Data()

#Pandas Data Frame 
ote_df = OTE_obj.get_historical_data()
# ote_df = OTE_obj.get_yesterdays_data()

#parse through entire dataset 
for _,row in ote_df.iterrows():

    try:
        #convert date type from typestamp 
        final_date = row['Date'].date().isoformat()

        #form query 
        cursor.execute("""INSERT INTO ote_records (day_hour,price,amount,export,import,balance,record_date)
                        VALUES (%s, %s, %s,%s,%s,%s, %s );
                        """,(row['Day_hour'],row['Price'],row['Amount'],row['Export'],row['Import'],row['Balance'],final_date))
        
        print("Insert into ote_records")

    except Exception as e:
        print(f'INSERT QUERY FAILED! {e}') 

#commit changes to database 
connection.commit()

#close database connection
connection.close()        