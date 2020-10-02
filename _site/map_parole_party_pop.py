from urllib.request import urlopen
import json
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objs as go
import pandas as pd
import numpy as np

mapbox_access_token = open(".mapbox_token").read()

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

dfFips = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/fips-unemp-16.csv",
                   dtype={"fips": str})

dfVoter = pd.read_csv("docs/data/voterreg18.csv")
dfVoter = dfVoter[dfVoter.notna()]
# convert str to float
dfVoter["Democratic"] = dfVoter["Democratic"].apply(pd.to_numeric, args=('coerce',))
dfVoter["Republican"] = dfVoter["Republican"].apply(pd.to_numeric, args=('ignore',))
dfVoter["Total Registered"] = dfVoter["Total Registered"].apply(pd.to_numeric, args=('coerce',))

index_percent = dfVoter[dfVoter['County'] == 'Percent'].index # get percent indices
dfVoter = dfVoter.drop(index_percent, axis=0) # remove entries named 'Percent' in County

dfVoter["DemocracticP"] = dfVoter["Democratic"] / dfVoter["Total Registered"]
dfVoter["RepublicanP"] = dfVoter["Republican"] / dfVoter["Total Registered"]

dfDummy = dfVoter[["DemocracticP", "RepublicanP"]]
dfVoter["MajorityP"] = dfDummy.max(axis=1) # percentage column
dfVoter["MajorityParty"] = dfDummy.idxmax(axis=1) # party-name column

dfVoter['color'] = np.where(dfVoter['DemocracticP']>dfVoter['RepublicanP'], 1*dfVoter['DemocracticP'], -1*dfVoter['RepublicanP'])

dfCCodes = pd.read_csv("docs/data/countyfips.csv", dtype={"fips": str})
dfCCodes = dfCCodes[dfCCodes.notna()]

dfDummy = pd.merge(dfVoter, dfCCodes, on='County', how='outer').dropna()
df = pd.merge(dfDummy, dfFips, on='fips', how='outer').dropna()

## major parolee data
dfPar = pd.read_csv("docs/data/parolee_counties_18.csv", dtype={"fips": str})
dfPar = dfPar[dfPar.notna()]

dfLoc = pd.read_csv("docs/data/longlat.csv")

df2 = pd.merge(dfPar, dfLoc, on='County', how='outer').dropna()

choro = go.Choroplethmapbox(z=np.array(df["color"]),
                            geojson=counties,
                            locations=df.fips.tolist(),
                            colorbar=dict(tickmode="array", tickvals=[-1, 1], ticktext=['rep','dem']),
                            colorscale='rdbu')

site_lat = df2.Lat
site_lon = df2.Long
location = df2.County.tolist()
text = df2.parolees.tolist()
scatt = go.Scattermapbox(lat=site_lat, lon=site_lon, 
                         mode='markers+text',
                         text=text,
                         marker=dict( size=df2.parolees.tolist()/df2.parolees.max()*70, color ='pink'))

layout = go.Layout(title ='Major Parolee Populations within California',
                    margin={"r":0,"t":0,"l":0,"b":0},
                    mapbox=dict(
                        accesstoken=mapbox_access_token,
                        bearing=0,
                        center=dict(lat=37.6017,lon=-121.7195),
                        pitch=0,
                        zoom=4.5,
                        style='dark'))

print(text)
fig=go.Figure(data=[choro, scatt], layout =layout)
#fig.update_geos(fitbounds="locations", visible=False)

fig.show()


# export html file for website use
import plotly.io as pio

pio.write_html(fig, file='_includes/parolees_partisan_county.html', auto_open=True)
