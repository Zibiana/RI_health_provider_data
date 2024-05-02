import plotly.express as px
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

init_notebook_mode(connected=True)
import pandas as pd

# https://plotly.com/python/mapbox-county-choropleth/
from urllib.request import urlopen
import json

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

import pandas as pd
data = pd.read_csv('RI_Spanish_Doctors.csv', dtype={"Código Postal": str,"Estado":str}) 
data_geo=pd.read_csv("Combined_Health_FIPS_data.csv",dtype={"fips": str, "Proporción": int, "2020":int})

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)
fig = px.choropleth_mapbox(data_geo, geojson=counties, locations='fips', color='Proporción',
                           color_continuous_scale="Viridis",
                           range_color=(0, 4000),
                           mapbox_style="carto-positron",
                           zoom=7.5, center = {"lat": 41.5, "lon": -71.5},
                           opacity=0.5,
                           labels={'Ciudad':'Proporción'}
                          )

fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
fig.show()