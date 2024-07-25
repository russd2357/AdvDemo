import streamlit as st

# Title of the Streamlit app
st.title("Text Input to File")

# Read the text file at startup
try:
    with open("user_input.txt", "r") as file:
        existing_text = file.read()
except FileNotFoundError:
    existing_text = ""

# Display the existing text
if existing_text:
   user_input = st.text_area("Existing text:", existing_text)
else:
    user_input = st.text_area("Enter your text here:")

# Button to submit the text
if st.button("Submit"):
    # Write the input text to a file
    with open("user_input.txt", "w") as file:
        file.write(user_input)
    st.success("Text has been written to user_input.txt")