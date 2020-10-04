import pandas as pd
import plotly.graph_objects as go
import plotly as py
import os
from plotly.subplots import make_subplots

sup=pd.read_csv(r'C:\Users\Administrator\Desktop\competition\supporters of Prop 17 in CA.csv',sep=',',index_col=0)
opp=pd.read_csv(r'C:\Users\Administrator\Desktop\competition\opponents of Prop 17 in CA.csv',sep=',',index_col=0)

sup['2020'][9:12]=[0,0,0]
opp["2020"][9:12]=[0,0,0]

sup.loc["sum of year"] =sup.apply(lambda x:x.sum()) 
opp.loc['sum of year'] =opp.apply(lambda x:x.sum())


sumplot=py.offline.plot
trace_=list()

trace_1=go.Bar(
    x=['2016','2017','2018','2019','2020'],
    y=list(sup.loc['sum of year']),
    name='supporter')
trace_2=go.Bar(
    x=['2016','2017','2018','2019','2020'],
    y=list(opp.loc['sum of year']),
    name='opponent')
trace_=[trace_1,trace_2]
layout=go.Layout(title='supporters & opponents of Prop 17 from 2016 to 2020')
figure=go.Figure(data=trace_,layout=layout)
sumplot(figure,filename='s&o of Prop 17.html')
