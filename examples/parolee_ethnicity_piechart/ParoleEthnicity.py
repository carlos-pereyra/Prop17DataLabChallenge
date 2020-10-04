# import all basic libraries
from urllib.request import urlopen
import json
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import numpy as np

# read in parolee 2018 age data
df = pd.read_csv("../../docs/data/parole_ethnicity.csv")
print(df)

# plot distribution on pie chart
fig = px.pie(df, values='eth_perc', names='ethnicity', color_discrete_sequence=px.colors.sequential.RdBu)
fig.write_html("../../docs/html/parole_ethnicity.html")
fig.show()
