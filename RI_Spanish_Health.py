import streamlit as st
import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-whitegrid')
import plotly.express as px

# https://plotly.com/python/mapbox-county-choropleth/
from urllib.request import urlopen
import json
import plotly.graph_objects as go

st.set_page_config(page_title="RI médica de español", layout="wide")
#Researching RI Healthcare provider for the Spanish Speaking Community
st.title("Búsqueda de proveedores de médica de RI para la comunidad de habla español")
#This is an enhanced alternatives to the Nuestra Salud website
st.write("Esta es una alternativa mejorada al sitio web Nuestra Salud(https://www.nuestrasalud.com/directorio-medico?search=sanchez)")

data = pd.read_csv('RI_Spanish_Doctors.csv', dtype={"Código Postal": str,"Estado":str}) 
data_census = pd.read_csv('CT_MA_RI_2020_Hispanic_census_data.csv',dtype={"2020": int}) 
data_tipo = pd.read_csv('tipo_data.csv')
data_geo=pd.read_csv("Combined_Health_FIPS_data.csv",dtype={"fips": str, "Proporción": int, "2020":int})


#####################################################
### Making Navigating stuff goes here
#######################################################

#Choose one city from below:
col1, col2 = st.columns([0.5,0.5])
with col1:
    ciudad = st.selectbox(label = 'Elige una ciudad de las siguientes:', options = np.insert(np.sort(data["Ciudad"].unique()),0,"Todas las ciudades"))
    st.write('Usted seleccionó:', ciudad)

    mask=data_census["Ciudad"]== ciudad
    mask2=data["Ciudad"]== ciudad

    #filter data by the choice
    if ciudad != "Todas las ciudades":
        #option 1: Using a mask:
    #    mask=data["Department"]==department
    #    data=data[mask]
        data = data.query("Ciudad== '{}'".format(ciudad))
        data_census=data_census.query("Ciudad== '{}'".format(ciudad))




    st.write("Currently there are {}".format(len(data["Nombre"].unique())),"doctors and nurses who speak spanish in {}.".format(ciudad))
    st.write("The census estimates there are {} people who identify as hispanic in RI with the highest concentration of English as a second lanuage speakers in Providence.".format(int(1095962*.176)), 
"So that's {} people per 1 doctor or nurse".format(int(data_census[mask]["2020"]/len(data["Nombre"].unique()))), "in {}.".format(ciudad), "This is just a rough estimate as we don't know the actual count of those that are Native Spanish speakers and it doesn't know who is hispanic and has a different Native language.")


with col2:
    fig = plt.figure(figsize=(9,5)) # figure size (width, height)
    x = data_geo["2020"]
    y= data_geo["Numero"]
    #fig, ax = plt.subplots()
    plt.title("Comparing number of hispanic residence vs Spanish speaking health service providers")
    plt.xlabel('Number of Spanish speaking Doctors and Nurses in the county')
    plt.ylabel('Number of people who identified as Hispanic in the 2020 census')
    plt.text(160,75000, "Providence")
    if ciudad !="Todas las ciudades":
        plt.text(data_geo[data_geo["Ciudad"]==ciudad]["Numero"],data_geo[data_geo["Ciudad"]==ciudad]["2020"], "{}".format(ciudad))
    plt.scatter(y,x)

    #     # draw the fig here
    st.pyplot(fig)




col1, col2 = st.columns([0.5,0.5])
with col1:
    #Choose one specialty from below:
    especialidad = st.selectbox(label = 'Elige una especialidad de las siguientes:', options = np.insert(np.sort(data["Especialidad"].unique()),0,"Todas las especialideds"))
    st.write('Usted seleccionó:', especialidad)

    #filter data by the choice
    if especialidad != "Todas las especialideds":
        #option 1: Using a mask:
    #    mask=data["Department"]==department
    #    data=data[mask]
        data = data.query("Especialidad== '{}'".format(especialidad))

    hopsitales_2 = st.selectbox(label = 'Elige un hospitales de las siguientes:', options = np.insert(np.sort(data["Hospital"].unique()),0,"Todos los hospitales"))
    if hopsitales_2 != "Todos los hospitales":
        data = data.query("Hospital== '{}'".format(hopsitales_2))

    st.write("There is/are {}".format(len(data["Especialidad"].unique())),"different kind(s) of specialist(s) who speak spanish at {}.".format(hopsitales_2))

    st.write("The kinds of doctors/nurses {} has is".format(hopsitales_2),"{}.".format(data["Especialidad"].unique()))    
with col2:
    hospitales = st.text_input('Buscar un hospital para nombre')

    reg_ex= st.checkbox("Regular Expression", value=0)

    if hospitales:
        if reg_ex==True:
            data=data[data["Hospital"].str.contains(hospitales, regex=True)]
        else:
            data=data[data["Hospital"].str.contains(hospitales,regex=False)]   



    



st.text("Estado:")
estado_RI = st.checkbox('Rhode Island', value=1) # default value is checked. 
estado_MA = st.checkbox('Massachusettes', value=1) # default value is checked. 
estado_CT = st.checkbox('Connecticut', value=1) # default value is checked. 

if not estado_RI:
    mask_RI=data["Estado"].str.contains("RI")
    data = data[~mask_RI]

if not estado_MA:
    mask_MA=data["Estado"].str.contains("MA")
    data = data[~mask_MA]

if not estado_CT:
    mask_CT=data["Estado"].str.contains("CT")
    data = data[~mask_CT]     

#####################################################
### Making Graphing or GIS stuff goes here (don't know how though)
#######################################################    

with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)
fig2 = px.choropleth_mapbox(data_geo, geojson=counties, locations='fips', color='Proporción',
                           color_continuous_scale="Viridis",
                           range_color=(0, 500),
                           mapbox_style="carto-positron",
                           zoom=6, center = {"lat": 41.5, "lon": -71.5},
                           opacity=0.5,
                           labels={'Ciudad':'Proporción'}
                          )

fig2.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
st.plotly_chart(fig2)


#Create the data frame with links, and hide_index deletes the index stamps
st.dataframe(data, hide_index=True)#, 
          #column_config={"URL": st.column_config.LinkColumn(display_text="Link")})


#st.dataframe(data_census, hide_index=True)