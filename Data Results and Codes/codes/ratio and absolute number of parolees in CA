import pandas as pd
import plotly.graph_objects as go
import plotly as py
import os
from plotly.subplots import make_subplots

pa=pd.read_csv(r'C:\Users\Administrator\Desktop\competition\the number of parolees in CA.csv',sep=',',index_col=0)
pop=pd.read_csv(r'C:\Users\Administrator\Desktop\population in CA from 1998 to 2016.csv',sep=',',index_col=0)

ratio=list()
for i in range(1998,2017):
    ratio.append(list(pa['parolees in CA'])[i-1998]/list(pop['Population'])[2016-i])


fig = make_subplots(rows=1, cols=1,
                    specs=[[{"secondary_y": True}]])
fig.add_trace(go.Bar(x =list(range(1998,2017)),
                     y =list(pa['parolees in CA']),
                     name = 'parolees in California'
                    ),
              row=1, col=1, secondary_y=False
)

fig.add_trace(go.Scatter(x=list(range(1998,2017)),
                         y=ratio,
                         name='ratio of parolees and population in California'
                        ),
               row=1, col=1, secondary_y=True,
)
fig.update_layout(
    title_text='ratio and absolute number of parolees in California'
)

pyplot(fig,filename='ratio and absolute number of parolees in California')
