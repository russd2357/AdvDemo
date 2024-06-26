import streamlit as st  
  
st.title("NBA Playoffs 2024 Stats Overview")  
  
st.markdown("""  
## Welcome to the NBA Playoffs 2024 Statistics Dashboard  
  
This Streamlit application allows you to explore and analyze the NBA playoffs statistics for 2024. The goal of this lesson is to help you understand how to:  
- Retrieve and prepare data  
- Display data in tables  
- Create simple visualizations  
- Use Streamlit's documentation for further learning  
  
Let's get started!  
  
### Objectives  
1. **Introduction to Streamlit**: Learn the basics of using Streamlit for building web applications.  
2. **Data Retrieval and Preparation**: Understand how to fetch and prepare data for analysis.  
3. **Data Visualization**: Learn how to create basic charts using Streamlit.  
4. **Using Documentation**: Understand how to use Streamlit's documentation to find additional functionalities.  
""")  

st.markdown("### Data Overview")

with st.expander("""NBA 2024 Playoffs Stats""", expanded=False):
    st.markdown("""### Data Source  
We are using data from [Basketball Reference](https://www.basketball-reference.com/playoffs/NBA_2024.html#totals-team).  
  
### How the Data Was Created  
Below are images showing the data table from the website and the corresponding CSV file. 
""")  
    col1, col2 = st.columns(2)  
    col1.image("media/nba_2024_total_stats_table.png", caption="Table of NBA 2024 Total Stats", use_column_width=True)  
    col2.image("media/nba_2024_total_stats_csv.png", caption="CSV of NBA 2024 Total Stats", use_column_width=True)  

st.divider()

with st.expander("""### Using Streamlit Documentation""", icon="📚"):
    #st.markdown("""### Using Streamlit Documentation  
    st.markdown("""Streamlit has excellent documentation that you can use to learn more about its features. Below are the key sections we will refer to during this lesson.  
    """)
    col1, col2 = st.columns(2)
    col1.image("media/streamlit_data_elements.png", caption="Data Elements", use_column_width=True)
    col2.image("media/streamlit_chart_elements.png", caption="Chart Elements", use_column_width=True)

    st.markdown("You can access the full documentation [here](https://docs.streamlit.io/develop/api-reference).")
  
st.markdown("### Let's Dive Into the Code!")  
st.markdown("""  
We'll start by loading our data and displaying it in a table. Then, we'll create some basic visualizations.  
  
#### Step 1: Loading and Displaying Data  
```python  
import pandas as pd  
  
@st.cache  
def load_data():  
    # Simulating CSV read operation  
    data = pd.read_csv("nba2024_playoffs_stats.csv")  
    return data  
  
data = load_data()  
st.dataframe(data)  
Step 2: Creating a Bar Chart

st.bar_chart(data[['Team', 'PTS']].set_index('Team'))  
 

Step 3: Creating a Scatter Plot

st.scatter_chart(data[['PTS', 'AST']])  
 
By the end of this lesson, you'll have a functional Streamlit app that displays and visualizes NBA playoff stats!
""")