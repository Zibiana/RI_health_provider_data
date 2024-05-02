import streamlit as st
import numpy as np
import pandas as pd
import re
import matplotlib.pyplot as plt


st.set_page_config(page_title="RI médica de español", layout="wide")
#Researching RI Healthcare provider for the Spanish Speaking Community
st.title("Búsqueda de proveedores de médica y especialidads de RI para la comunidad de habla español")
#This is an enhanced alternatives to the Nuestra Salud website
st.write("Esta es datos de sitio web Nuestra Salud(https://www.nuestrasalud.com/directorio-medico?search=sanchez)")

data = pd.read_csv('RI_Spanish_Doctors.csv', dtype={"Código Postal": str,"Estado":str}) 
data_census = pd.read_csv('CT_MA_RI_2020_Hispanic_census_data.csv') 
data_tipo = pd.read_csv('tipo_data.csv')

#####################################################
### Making Navigating stuff goes here
#######################################################

# #Choose one city from below:
# ciudad = st.selectbox(label = 'Elige una ciudad de las siguientes:', options = np.insert(np.sort(data["Ciudad"].unique()),0,"Todas las ciudades"))
# st.write('Usted seleccionó:', ciudad)

# mask=data_census["Ciudad"]== ciudad
# mask2=data["Ciudad"]== ciudad

#  ###Let's make an image
# fig = plt.figure(figsize=(9,5)) # figure size (width, height)
# arr = len(data[mask2]["Nombre"].unique())
# #fig, ax = plt.subplots()
# plt.title("Something!")
# plt.xlabel('Counts maybe')
# plt.hist(arr, bins=20)

#     # draw the fig here
# st.pyplot(fig)

# #filter data by the choice
# if ciudad != "Todas las ciudades":
#     #option 1: Using a mask:
# #    mask=data["Department"]==department
# #    data=data[mask]
#     data = data.query("Ciudad== '{}'".format(ciudad))
#     data_census=data_census.query("Ciudad== '{}'".format(ciudad))




# st.write("Currently there are {}".format(len(data["Nombre"].unique())),"doctors and nurses who speak spanish in {}.".format(ciudad))
# st.write("The census estimates there are {} people who identify as hispanic in RI with the highest concentration of English as a second lanuage speakers in Providence.".format(int(1095962*.176)), 
# "So that's {} people per 1 doctor or nurse".format(int(data_census[mask]["2020"]/len(data["Nombre"].unique()))), "in {}.".format(ciudad), "This is just a rough estimate as we don't know the actual count of those that are Native Spanish speakers and it doesn't know who is hispanic and has a different Native language.")



# #Choose one specialty from below:
# especialidad = st.selectbox(label = 'Elige una especialidad de las siguientes:', options = np.insert(np.sort(data["Especialidad"].unique()),0,"Todas las especialidads"))
# st.write('Usted seleccionó:', especialidad)

# #filter data by the choice
# if especialidad != "Todas las especialidads":
#     #option 1: Using a mask:
# #    mask=data["Department"]==department
# #    data=data[mask]
#     data = data.query("Especialidad== '{}'".format(especialidad))


# hospitales = st.text_input('Hospital')

# reg_ex= st.checkbox("Regular Expression", value=0)

# if hospitales:
#     if reg_ex==True:
#         data=data[data["Hospital"].str.contains(hospitales, regex=True)]
#     else:
#         data=data[data["Hospital"].str.contains(hospitales,regex=False)]   

# hopsitales_2 = st.selectbox(label = 'Elige un hospitales de las siguientes:', options = np.insert(np.sort(data["Hospital"].unique()),0,"Todos los hospitales"))
# if hopsitales_2 != "Todos los hospitales":
#     data = data.query("Hospital== '{}'".format(hopsitales_2))

# st.write("There is/are {}".format(len(data["Especialidad"].unique())),"different kind(s) of specialist(s) who speak spanish at {}.".format(hopsitales_2))

# st.write("The kinds of doctors/nurses {} has is".format(hopsitales_2),"{}.".format(data["Especialidad"].unique()))



# st.text("Estado:")
# estado_RI = st.checkbox('Rhode Island', value=1) # default value is checked. 
# estado_MA = st.checkbox('Massachusettes', value=1) # default value is checked. 
# estado_CT = st.checkbox('Connecticut', value=1) # default value is checked. 

# if not estado_RI:
#     mask_RI=data["Estado"].str.contains("RI")
#     data = data[~mask_RI]

# if not estado_MA:
#     mask_MA=data["Estado"].str.contains("MA")
#     data = data[~mask_MA]

# if not estado_CT:
#     mask_CT=data["Estado"].str.contains("CT")
#     data = data[~mask_CT]     

#####################################################
### Making Graphing or GIS stuff goes here (don't know how though)
#######################################################    

#Create the data frame with links, and hide_index deletes the index stamps
st.dataframe(data_tipo, hide_index=True)#, 
          #column_config={"URL": st.column_config.LinkColumn(display_text="Link")})


#st.dataframe(data_census, hide_index=True)