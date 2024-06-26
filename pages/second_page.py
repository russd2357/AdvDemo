
import streamlit as st

text = st.sidebar.text_area("Paste Text Here")

st.write(text) # write text to sidebar

col1, col2 = st.columns(2)
col1_expander = col1.expander("Expand Original")

sidebarButton = st.sidebar.button("Clean Text")
if sidebarButton:
  with col1_expander:
    col1_expander.write(text)


col2.header("Col 2") 
with col2:
  st.image("./logos/dallas_cowboys_logo.png", use_column_width=True)