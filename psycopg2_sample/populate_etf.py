import config
import psycopg2
import psycopg2.extras
import tqdm
import csv 
import logging


connection = psycopg2.connect(host=config.DB_HOST,
                              database=config.DB_NAME,
                              user=config.DB_USER,
                              password=config.DB_PASS,
                              port=config.DB_PORT)

cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

cursor.execute("select * from stock where is_etf = TRUE")

etfs = cursor.fetchall()

dates = ['2022-12-09', '2022-12-10']

for current_date in dates:
    for etf in etfs:
   # print(etf)
 
        print(etf['symbol'])
        with open(f"data/2022-12-09/{etf['symbol']}.csv") as f:
        #with open(f"data/2022-12-09/ARKK.csv") as f:
           reader = csv.reader(f)    
           next(reader)
           for row in reader:
              try:
                ticker = row[3]
                shares = row[5]
                weight = row[7]
              except IndexError as e:
                # Row without 4th, 6th and 8th columns won't be handled.
                logging.warning(repr(e))
              else:
                cursor.execute("""
                    SELECT * FROM stock WHERE symbol = %s
                """, (ticker,))
                stock = cursor.fetchone()
                if stock:
                    cursor.execute("""
                        INSERT INTO etf_holding (etf_id, holding_id, dt, shares, weight)
                        VALUES (%s, %s, %s, %s, %s)                       
                        """, (etf['id'],
                        stock['id'],
                        current_date,
                        int(shares.replace(',', '')),
                        float(weight.replace('%', ''))/100))

connection.commit()
       
       #       
       # if ticker:
#print(row)

