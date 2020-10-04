import pandas as pd
import plotly.graph_objects as go
import plotly as py
import os
from plotly.subplots import make_subplots

sup=pd.read_csv(r'...\...\Data Results and Codes\codes\supporters of Prop 17 in CA.csv',sep=',',index_col=0)
sup['2020'][9:12]=[0,0,0]
month=list(sup.index.values)

pyplot=py.offline.plot
trace=list()

trace_1=go.Bar(
        x=month,
        y=list(sup['2016']),
        name='2016'
    )                  
trace_2=go.Bar(
        x=month,
        y=list(sup['2017']),
        name='2017'
    )       
trace_3=go.Bar(
        x=month,
        y=list(sup['2018']),
        name='2018'
    )   
trace_4=go.Bar(
        x=month,
        y=list(sup['2019']),
        name='2019'
    )    
trace_5=go.Bar(
        x=month,
        y=list(sup['2020']),
        name='2020'
    )    
trace=[trace_1,trace_2,trace_3,trace_4,trace_5]
layout = go.Layout(
            title = 'supporters to Prop 17 from 2016 to 2020 in CA'
    )
figure = go.Figure(data = trace, layout = layout)
pyplot(figure,filename='supporters to Prop 17.html')

