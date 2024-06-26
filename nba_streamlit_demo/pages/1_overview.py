import streamlit as st  
import pandas as pd  
  
st.title("NBA Playoffs 2024 Data Overview")  
  
@st.cache_data   
def load_data():  
    url = "https://www.basketball-reference.com/playoffs/NBA_2024.html#totals-team"  
    # Simulating CSV read operation  
    data = pd.read_csv("nba2024_playoff_stats.csv")  
    return data  
  
data = load_data()  
st.write(data)  
  
st.markdown("### Basic Statistics")  
st.write(data.describe())  