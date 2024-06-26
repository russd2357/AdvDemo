import streamlit as st  
import pandas as pd  
  
st.title("Team Statistics")  
  
@st.cache_data  
def load_data():  
    # Simulating CSV read operation  
    data = pd.read_csv("nba2024_playoff_stats.csv")  
    return data  
  
data = load_data()  
  
team = st.selectbox("Select a team:", data['Team'].unique())  
team_data = data[data['Team'] == team]  
  
st.write(team_data)  
  
st.markdown("### Team Summary")  
st.write(team_data.describe())  