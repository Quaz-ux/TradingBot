import requests
import json

class CoinBaseConnector:
    def __init__(self):
        self.url = "https://api.exchange.coinbase.com"
        self.headers = {"Accept": "application/json"}

    def getProducts(self, productId):
        return requests.request("GET", self.url+"/products/"+str(productId)+"/ticker", headers=self.headers)

    def getProductPrice(self, productId):
        result = json.loads(self.getProducts(productId).content)
        return result['price']

