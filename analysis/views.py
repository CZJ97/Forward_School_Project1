from django.shortcuts import render
from django.http import HttpResponse
from project1.settings import MEDIA_URL,MEDIA_ROOT
from django.conf.urls.static import static
from django.views.generic import TemplateView, View 

import numpy as np
import pandas as pd
import matplotlib as pl
pl.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sb

# Data loading
pickle_path = MEDIA_ROOT+"/Data/df_hotstock_analysis.pkl"
df = pd.read_pickle(pickle_path)

df.rename(columns={
'Rank'           : 'Popularity Rank'     ,
'Stock_Name'     : 'Stock Name'          ,
'Company'        : 'Company Name'        ,
'Score'          : 'Trends Score'        ,
'total_comments' : 'Total Comments'      ,
'unique_user'    : 'Unique User'         ,
'min_comments_dt': 'Oldest Comment Date' ,
'max_comments_dt': 'Latest Comment Date' ,
'dt_difference'  : 'Time Differences'    ,
'avg_negative'   : 'Negative Sentiment'  ,
'avg_neutral'    : 'Neutral Sentiment'   ,
'avg_positive'   : 'Positive Sentiment'  ,
'avg_compound'   : 'Overall Sentiment'   ,
'top_n1'         : 'Top Unigrams Keyword',
'top_n2'         : 'Top Bigrams Keyword' ,
'top_n3'         : 'Top Trigrams Keyword',}, inplace=True)

class HomePageView(TemplateView):
    def get(self,request,**kwargs):
        return render(request, 'analysis/index.html', context=None)

class Api(TemplateView):
    # Create your views here.
    def getData(request):

        return HttpResponse(df.to_html(classes='table table-bordered'))

    def getUnigramsGraph(request):

        sn=request.GET.get("val","")
        stock_mask = df['Stock Name'] == sn

        if stock_mask.any():
            print("im here")
            topn= df[stock_mask]['Top Unigrams Keyword'].values[0]

            top_df= pd.DataFrame(topn)
            top_df.columns=["Word","Freq"]
            sb.set(rc={'figure.figsize':(13,8)})
            graph = sb.barplot(x="Word",y="Freq", data=top_df)
            graph.set_xticklabels(graph.get_xticklabels(),rotation=30)
            response = HttpResponse(content_type="image/jpeg")
            graph.figure.savefig(response, format="png")
            return response

        else:
            return HttpResponse("none")

    def getBigramsGraph(request):

        sn=request.GET.get("val","")
        stock_mask = df['Stock Name'] == sn

        if stock_mask.any():
            print("im here")
            topn= df[stock_mask]['Top Bigrams Keyword'].values[0]

            top_df= pd.DataFrame(topn)
            top_df.columns=["Word","Freq"]
            sb.set(rc={'figure.figsize':(13,8)})
            graph = sb.barplot(x="Word",y="Freq", data=top_df)
            graph.set_xticklabels(graph.get_xticklabels(),rotation=30)
            response = HttpResponse(content_type="image/jpeg")
            graph.figure.savefig(response, format="png")
            return response

        else:
            return HttpResponse("none")

    def getTrigramsGraph(request):

        sn=request.GET.get("val","")
        stock_mask = df['Stock Name'] == sn

        if stock_mask.any():
            print("im here")
            topn= df[stock_mask]['Top Trigrams Keyword'].values[0]

            top_df= pd.DataFrame(topn)
            top_df.columns=["Word","Freq"]
            sb.set(rc={'figure.figsize':(13,8)})
            graph = sb.barplot(x="Word",y="Freq", data=top_df)
            graph.set_xticklabels(graph.get_xticklabels(),rotation=30)
            response = HttpResponse(content_type="image/jpeg")
            graph.figure.savefig(response, format="png")
            return response

        else:
            return HttpResponse("none")
        
