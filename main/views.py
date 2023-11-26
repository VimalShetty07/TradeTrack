from django.shortcuts import render
from yahoo_fin.stock_info import *
from django.http import HttpResponse

# Create your views here.
def StockPicker(request):
    stock_picker = tickers_nifty50()
    return render(request,'main/stockPicker.html',{'StockPicker':stock_picker})


def StockTracker(request):
    StockPicker = request.GET.getlist('StockPicker')
    print(StockPicker)
    data ={}
    available_stocks = tickers_nifty50()
    for i in StockPicker:
        if i in available_stocks:
            pass
        else:
            return HttpResponse("Error")
    for i in StockPicker:
        details = get_quote_table(i)
        data.update(details)
    print(data)
        
    return render(request,'main/stockTracker.html')