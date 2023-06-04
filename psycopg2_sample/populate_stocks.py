import config
import alpaca_trade_api as tradeapi 
import psycopg2
import psycopg2.extras
import tqdm

connection = psycopg2.connect(host=config.DB_HOST,
                              database=config.DB_NAME,
                              user=config.DB_USER,
                              password=config.DB_PASS,
                              port=config.DB_PORT)

cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)

cursor.execute("SELECT * FROM stock")

api = tradeapi.REST(config.API_KEY, config.API_SECRET, base_url=config.API_URL)

assets = api.list_assets()

print(len(assets))

for asset in tqdm.tqdm(assets):
    #print(f"Inserting stock {asset.name} {asset.symbol}") 
    cursor.execute("""
      INSERT INTO stock (name, symbol, exchange, is_etf)
      VALUES (%s, %s, %s, false)
    """, (asset.name, asset.symbol, asset.exchange))

connection.commit()








##1 

#stocks = cursor.fetchall()

#print(cursor.fetchall())

#for stock in stocks:
#   print(stock['name'])


