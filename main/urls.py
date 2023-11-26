from django.urls import path
from . import views


urlpatterns =[
    path('',views.StockPicker, name = 'stockPicker'),
    path('stockTracker',views.StockTracker, name = 'stockTracker')
]