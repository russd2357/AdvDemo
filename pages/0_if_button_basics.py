import streamlit as st  # Import the Streamlit library for web apps  
  
# Title of the Streamlit page  
st.title("Learn IF Statements with Interactive Buttons")    
  
# Tabs for different sections to organize our app  
tab1, tab2, tab3 = st.tabs(["Introduction", "Examples", "Practice"])    
  
# Introduction Tab  
with tab1:    
    st.header("Introduction to IF Statements")    
      
    # An expandable section that explains what an IF Statement is  
    with st.expander("What is an IF Statement?", expanded=True):    
        st.write("""  
        An **IF statement** in Python is a conditional statement that executes code based on a condition.     
        The syntax for an if statement is:    
        ```python    
        if condition:    
            statement(s)    
        ```  
        The if statement runs the statements inside it only if the condition is true. If false, it skips them.  
        """)    
  
    # Another expandable section with key points about IF statements  
    with st.expander("Key Points about IF Statements", expanded=True):    
        st.write("""  
        - **if statements** control the flow of your code.  
        - Use **elif** for multiple conditions.  
        - **else** executes code when conditions aren't met.  
        """)    
    
    with st.expander("Basic If Statement", expanded=True):   
        st.subheader("Basic If Statement")  
        st.code("""  
        number = 10  
        if number > 0:  
            print("The number is positive.")  
        """)  
        
        st.write("Try it out:")  
        number_input = st.number_input("Enter a number:", value=0)  
        if number_input > 0:  
            st.write("The number is positive.")  
        elif number_input < 0:  
            st.write("The number is negative.")  
        else:  
            st.write("The number is zero.")  
  
    # Add markdown separator for visual clarity  
    st.markdown("---")  
    # Markdown to display images as cheat sheets for if statements  
    st.markdown("""  
    ## Cheatsheets  
  
    ![](https://cdn.educba.com/academy/wp-content/uploads/2019/09/If-Else-in-Python.jpg.webp)
    > source: [educba.com/if-else-in-python](https://www.educba.com/if-else-in-python/)  
  
    ![](https://introcs.cs.princeton.edu/python/13flow/images/IfStatements.png)
    > source: [introcs.cs.princeton.edu/python/13flow](https://introcs.cs.princeton.edu/python/13flow/)  
    """)  
  
# Examples Tab  
with tab2:    
    st.header("Examples of IF Statements")    
  
    # Example 1: Simple IF Statement  
    with st.expander("Example 1: Simple IF Statement"):    
        st.write("Click the button below to see a simple if statement in action.")    
          
        button1 = st.button("Button1")  # Create a button  
        if button1:  # If the button is clicked  
            st.write("Hey, you clicked Button1!")  # Display this message  
            button1 = st.empty()  # Clear the button (optional)  
  
    # Example 2: IF-ELSE Statement  
    with st.expander("Example 2: IF-ELSE Statement"):    
        st.write("Do you like this app? Let us know!")    
  
        like = st.checkbox("Do you like this app?")  # Checkbox for input  
        button2 = st.button("Submit")  # Submit button  
        if button2:  # If the submit button is clicked  
            if like:  # And if the checkbox is checked  
                st.write("Thanks for liking the app! 😊")  # Show a thank you message  
            else:  # Otherwise  
                st.write("Sorry you didn't like the app. We'll do better next time! 😔")  # Show a different message  
  
    # Example 3: IF-ELIF-ELSE Statement  
    with st.expander("Example 3: IF-ELIF-ELSE Statement"):    
        st.write("Choose your favorite animal and see what happens.")    
          
        # Radio buttons to select a favorite animal  
        animals = st.radio("What is your favorite animal?", ("Cat", "Dog", "Bird"))    
        # Multiselect allows choosing more than one animal  
        animals2 = st.multiselect("Select multiple favorite animals", ("Cat", "Dog", "Bird"))    
        button3 = st.button("Show Action")  # Button to trigger the action  
        if button3:  # If the button is clicked  
            if animals2 == ["Dog"]:  # Check if 'Dog' is selected  
                st.write("Woof woof! 🐶")  # Dog response  
            elif animals2 == ["Dog", "Cat"]:  # Check if both 'Dog' and 'Cat' are selected  
                st.write("Dogs vs Cats! 🐶🐱")  # Dog and Cat response  
            else:  # For any other selection  
                st.write("Interesting choice!")  # General response  
  
# Practice Tab  
with tab3:    
    st.header("Practice IF Statements")    
  
    # A section where students can try out what they've learned  
    with st.expander("Try It Yourself"):    
        st.write("Let's make a PB&J sandwich! Decide if you have jelly and make a sandwich.")    
          
        # Dropdown for jelly selection  
        have_jelly = st.selectbox("Do you have jelly?", ("Yes", "No"))    
        button4 = st.button("Make Sandwich")  # Button to 'make' the sandwich  
        if button4:  # If the sandwich button is clicked  
            st.write("Let's make a PB&J sandwich!")  # Start the sandwich-making process  
            # Instructions for making the sandwich, with an IF statement for jelly  
            st.write("Get two slices of bread")    
            st.write("Get peanut butter")    
            st.write("Spread peanut butter on one slice of bread")    
            if have_jelly == "Yes":  # If jelly is available  
                st.write("Get jelly")    
                st.write("Spread jelly on the other slice of bread")    
            else:  # If no jelly  
                st.write("Add more peanut butter 😋")    
            st.write("Put the two slices of bread together")    
            st.write("Enjoy your sandwich! 🥪")    

st.divider()
# IF/ELSE Statements  
st.header("IF/ELSE Statements")  
st.markdown("""  
### String Example  
```python  
if lastName == "Bob":  
    print("Welcome Bob!")  
else:  
    print("You are not Bob!")  
```  
### Integer Example  
```python  
if age > 14:  
    print("Age is above 14")  
elif age > 10 and age <= 14:  
    print("Age is between 10 and 14")  
else:  
    print("Under 14")  
```  
""")  
