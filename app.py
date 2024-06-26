import streamlit as st

st.title("Hey Welcome BSMP 2024 Lesson on Streamlit🤖")

text = """

- More information on streamlit [here](https://docs.streamlit.io/)


- YAY Bam Acadmey

- My Name is Bing

"""

st.write(text)
st.success("Today is Thursday")
st.error("oops")

st.slider("This is a slider", 0, 100, (25, 75))
st.divider()  # 👈 Draws a horizontal rule
st.write("This text is between the horizontal rules.")

st.image("logos/microsoft_logo.png")

st.success("Success")

st.sidebar.header("Streamlit Sidebar")
st.sidebar.image("logos/microsoft_logo.png")

button1 = st.button("Click Me")













