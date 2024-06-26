import streamlit as st  
import pandas as pd  

  
st.title("Charts Overview")  
  
@st.cache_data  
def load_data():  
    # Simulating CSV read operation  
    data = pd.read_csv("nba2024_playoff_stats.csv")  
    return data  
  
data = load_data()  
  
st.markdown("""  
## How to Use Charts in Streamlit  
Streamlit makes it easy to create and display charts. Here, we'll show you how to create a bar chart and a scatter plot.  
""")  
  
# Bar Chart  
st.markdown("### Bar Chart")  
st.markdown("A bar chart can be used to compare different categories of data.")  
bar_chart_data = data[['Team', 'PTS']].set_index('Team')  
st.bar_chart(bar_chart_data)  
  
# Scatter Plot  
st.markdown("### Scatter Plot")  
st.markdown("A scatter plot can be used to visualize the relationship between two numerical variables.")  
scatter_chart_data = data[['PTS', 'AST']]  
st.write("Scatter plot of Points vs Assists")  
st.scatter_chart(scatter_chart_data)  
  
st.markdown("""  
## Conclusion  
These examples show you how to create simple bar charts and scatter plots with Streamlit. You can customize these charts further by referring to the [Streamlit documentation](https://docs.streamlit.io/library/api-reference/charts/st.bar_chart).  
""")  