from django.conf.urls import url 
from analysis import views
from django.urls import path 
from django.conf.urls.static import static

app_name = 'analysis'

urlpatterns=[
    path('',views.HomePageView.as_view(), name='home'),
    # path('getnum/',views.Api.getNums, name='get-num'),
    # path('getavg/',views.Api.getAvg, name='get-avg'),
    # path('getgraph/',views.Api.getGraph, name='get-graph'),
    path('getdata/',views.Api.getData, name='get-data'),
    path('get-unigrams-graph/',views.Api.getUnigramsGraph, name='get-unigrams-graph'),
    path('get-bigrams-graph/',views.Api.getBigramsGraph, name='get-bigrams-graph'),
    path('get-trigrams-graph/',views.Api.getTrigramsGraph, name='get-trigrams-graph'),
    # path('chart/',views.HomeView.as_view(), name='home-view'),
    # path('chart-api/',views.ChartData.as_view(), name='chart-api'),
    # path('plotly-chart/',views.PlotlyChartView.as_view(), name='plotly-chart'),

]