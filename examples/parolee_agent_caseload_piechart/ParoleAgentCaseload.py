# import all basic libraries
from urllib.request import urlopen
import json
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import numpy as np

# read in parolee 2018 age data
df = pd.read_csv("../../docs/data/parole_agent_caseload.csv")
print(df)

# plot distribution on pie chart
fig = px.pie(df, values='stat_perc', names='status', color_discrete_sequence=px.colors.sequential.RdBu)
fig.write_html("parole_agent_caseload.html")
fig.show()
