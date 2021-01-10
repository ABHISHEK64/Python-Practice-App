import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sea
import numpy as np
from urllib.request import Request, urlopen

st.title("""
 Ipl Team Points Table
""")
st.markdown(""" 
This app perform web scrapping Extract Player Data from|
* ** Python libraries:**base64,pandas,numpy,steamlit
* ** Data Source:** [BasketBall-reference.com]
""")
st.sidebar.header('User Input Features')
selected_year=st.sidebar.selectbox('Year',list(reversed(range(2008,2020)))) #it will create option to the user to select diffrent year players stats
selected_categories=st.sidebar.selectbox('Categories',list(['most-runs','most-runs-over','most-fours','most-sixes','biggest-sixes','most-centuries','most-fifties','most-maidens']))
#Web scrapping using python
@st.cache
def load_data(year,categories):
    url = "https://www.iplt20.com/stats/"+str(year)+"/"+str(categories) 
    html=pd.read_html(url,header=0)
    df=html[0]
    #raw=df.drop(df[df.Age=='Age'].index)
    raw=df.fillna(0)
    playerstats=raw
    return playerstats
playerstats=load_data(selected_year,selected_categories)
# Sidebar -Team Selection
#sorted_unique_team=sorted(playerstats.Team.unique())
#selected_team=st.sidebar.multiselect('Team',sorted_unique_team,sorted_unique_team)   
#Sidebar -Position selection
unique_player=sorted(playerstats.PLAYER.unique())
selected_player=st.sidebar.multiselect('Player',list(unique_player))
#Filterin Data
df_selected_team=playerstats[(playerstats.PLAYER.isin(selected_player))]
st.header('Display Player Stats of selected Team(s)')
st.write('Data Dimension:' +str(df_selected_team.shape[0])+'rows and' +str(df_selected_team.shape[1])+'columns.')
st.dataframe(df_selected_team,width=900,height=900)
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download CSV File</a>'
    return href
st.markdown(filedownload(df_selected_team), unsafe_allow_html=True)
#heat map
# Heatmap
if st.button('Intercorrelation Heatmap'):
    st.header('Intercorrelation Matrix Heatmap')
    df_selected_team.to_csv('output.csv',index=False)
    df = pd.read_csv('output.csv')

    corr = df.corr()
    mask = np.zeros_like(corr)
    mask[np.triu_indices_from(mask)] = True
    with sea.axes_style("darkgrid"):
        f, ax = plt.subplots(figsize=(7, 5))
        ax = sea.heatmap(corr, mask=mask, vmax=1, square=True)
    st.pyplot()

if st.button('Bar Garaph'):
    st.title('Bar Graph Using')
    df_selected_team.to_csv('output.csv',index=False)
    df=pd.read_csv('output.csv')