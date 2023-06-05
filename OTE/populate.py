import psycopg2 
import psycopg2.extras
import config 
from OTE import *
from datetime import datetime
from time import sleep

connection = psycopg2.connect(host=config.DB_HOST,database=config.DB_NAME,user=config.DB_USER,password=config.DB_PASSWORD)
cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
# cursor.execute('SELECT * FROM ote_records')
# cursor.execute('DELETE FROM ote_records')

# rows = cursor.fetchall()

# for _ in rows:
#     print(_)

OTE_obj = OTE_Data()

#Pandas Data Frame 
# ote_df = OTE_obj.get_historical_data()
ote_df = OTE_obj.get_tomorrow_data()

# print(all_data)

for _,row in ote_df.iterrows():
    try:
        values = f"({row['Day_hour']},'{row['Price']}','{row['Amount']}','{row['Export']}','{row['Import']}','{row['Balance']}','{row['Date'].date().isoformat()}')"
        query = "INSERT INTO ote_records (day_hour,price,amount,export,import,balance,record_date) VALUES " + values + ';'
        print(query)
        
        cursor.execute(query)

        sleep(2)

    except Exception as e:
        print(f'INSERT QUERY FAILED! {e}')
    # print(query)