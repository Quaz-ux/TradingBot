from django.http import HttpResponse, JsonResponse
from django.template import loader
from CoinbaseBot.CoinBaseConnector import CoinBaseConnector


def index(request):
    template = loader.get_template('CoinbaseBot/index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def getPrice(request):
    conn = CoinBaseConnector()
    price = conn.getProductPrice('BTC-USD')
    context = {'price': price}
    return JsonResponse(context)
