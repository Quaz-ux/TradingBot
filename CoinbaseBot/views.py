from django.http import HttpResponse
from django.template import loader
from CoinbaseBot.CoinBaseConnector import CoinBaseConnector


def index(request):
    conn = CoinBaseConnector()
    price = conn.getProductPrice('BTC-USD')
    template = loader.get_template('CoinbaseBot/index.html')
    context = {'price': price}
    return HttpResponse(template.render(context, request))
