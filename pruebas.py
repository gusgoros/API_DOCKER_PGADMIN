import requests
import json
import psycopg2

# /coins/markets
# para este ejemplo me bajo solo 5 monedas
''' 
"id": "bitcoin",
"id": "ethereum",
"id": "tether",
"id": "usd-coin",
"id": "binancecoin",
'''
url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=bitcoin%2C%20ethereum%2C%20tether%2C%20usd-coin%2C%20binancecoin&order=market_cap_desc&per_page=100&page=1&sparkline=false'
COINGECKO_COIN_URL=url


response = requests.get(url)




if response.status_code==200:
    #print(response)
    response_json=response.json() # Esto es un DICCIONARIO
    #print(response_json)
    print(len(response_json))
    print(response_json[0])

    #voy a recorrer el diccionario
    for p in response_json:
        del p['image'] #borro la etiqueta image de mi json
        del p['roi']
        del p['last_updated']
    print()
    print(len(response_json))
    print(response_json[0])

    with open('monedas.json','w') as f: # con el with no me preocupo de cerrar el archivo con close() asi lo dijo franco en el curso de coderhouse
        json.dump(response_json,f,indent=4) # con esto guardo un nuevo archivo con el nombre monedas.json

 
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


#Esto lo transformaron a
def get_ethereum_data():
    ethereum_data = {}
    response = requests.get(f"{COINGECKO_COIN_URL}")
    response.raise_for_status()
    data = response.json()
    ethereum_data["current_price"] = data["market_data"]["current_price"]["usd"]
    ethereum_data["market_cap"] = data["market_data"]["market_cap"]["usd"]
    ethereum_data["ath"] = data["market_data"]["ath"]["usd"]
    ethereum_data["ath_percentage"] = data["market_data"]["ath_change_percentage"]["usd"]
    ethereum_data["24h_percentage"] = data["market_data"]["price_change_percentage_24h"]
    ethereum_data["7d_percentage"] = data["market_data"]["price_change_percentage_7d"]
    ethereum_data["30d_percentage"] = data["market_data"]["price_change_percentage_30d"]
    ethereum_data["1y_percentage"] = data["market_data"]["price_change_percentage_1y"]
    return ethereum_data

#Esto:

def get_ethereum_data():
    response = requests.get(COINGECKO_COIN_URL)
    response.raise_for_status()

    data = response.json()    
    market_data = data["market_data"]
    
    return {
        "current_price": market_data["current_price"]["usd"],
        "market_cap": market_data["market_cap"]["usd"],
        "ath": market_data["ath"]["usd"],
        "ath_percentage": market_data["ath_change_percentage"]["usd"],
        "24h_percentage": market_data["price_change_percentage_24h"],
        "7d_percentage": market_data["price_change_percentage_7d"],
        "30d_percentage": market_data["price_change_percentage_30d"],
        "1y_percentage": market_data["price_change_percentage_1y"],
    }


'''Preguntas a las que quiero buscarle respuestas:

1 - Puedo con Pandas abrir un archivo json? o solo sirve para CSV? Ejemplo: pd.read_csv(archivo)
2 - Esta no es pregunta: Con PyArrow se puede trabajar con archivos Parquet en lugar de usar pandas que no es tan eficiente
    con archivos parquet. Lo que conto Diego fue que de 3hs bajo a 3minutos para procesar 1millon de registros de texto de twitter

'''


