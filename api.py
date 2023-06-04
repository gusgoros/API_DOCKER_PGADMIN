import requests
import json
import psycopg2

# /coins/markets
''' 
"id": "bitcoin",
"id": "ethereum",
"id": "tether",
"id": "usd-coin",
"id": "binancecoin",
'''
url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin%2C%20ethereum%2C%20tether%2C%20usd-coin%2C%20binancecoin&order=market_cap_desc&per_page=100&page=1&sparkline=false'

response = requests.get(url)


conn = psycopg2.connect(user="root",
                        password="root",
                        host="localhost",
                        port="5432",
                        database="root")


cur = conn.cursor()
# Creation of coin table
#cur.execute("DROP TABLE coin;")
cur.execute("CREATE TABLE IF NOT EXISTS coin (id varchar(50) NOT NULL, symbol varchar(50) NOT NULL, name  varchar(50) NOT NULL, current_price DECIMAL(20,3) NOT NULL, market_cap_rank INT, PRIMARY KEY (id));")

if response.status_code==200:
    #print(response)
    response_json=response.json() # Esto es un DICCIONARIO
    #print(response_json)
    #parseando datos de las monedas
    '''
    for coins in response_json:
        print("----------------------------------------------------")
        print("id:      "+coins['id'])
        print("symbol:      "+coins['symbol'])
        print("name:      "+coins['name'])
        print("current_price:      "+str(coins['current_price'])) #float
        print("Capitalización de mercado:      "+str(coins['market_cap_rank']))     #int
        print("----------------------------------------------------")
        '''
    for coins in response_json:
        insert_query = """INSERT INTO coin (id, symbol, name, current_price, market_cap_rank) 
        VALUES ('"""+coins['id']+"""', 
                '"""+coins['symbol']+"""', 
                '"""+coins['name']+"""',
                '"""+str(coins['current_price'])+"""',
                '"""+str(coins['market_cap_rank'])+"""'        
                );"""
        print(insert_query)
        cur = conn.cursor()
        cur.execute(insert_query)
        
# commit changes
conn.commit()
# Close the connection
conn.close()
