import streamlit as st  
import numpy as np  
  
# Title and Introduction  
st.title("Lesson 2: Functions and Control Flow")  
st.write("""  
Welcome to Lesson 2! In this lesson, we will cover functions and control flow in Python.   
We will learn how to define functions, use if statements, and explore loops.  
""")  
  
# Section: Functions  
st.header("Functions in Python")  
st.write("""  
Functions are reusable pieces of code that perform a specific task.   
They help us organize our code and make it more readable and maintainable.  
""")  
  
st.subheader("Defining a Function")  
st.code("""  
def greet(name):  
    return f"Hello, {name}!"  
""")  
def greet(name):  
    return f"Hello, {name}!"  

st.write("Try it out:")  
name = st.text_input("Enter your name:")  
if name:  
    st.write(greet(name))  
  
# Section: If Statements  
st.header("If Statements")  
st.write("""  
If statements allow us to execute certain parts of our code based on conditions.   
They help us make decisions in our programs.  
""")  
  
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
  
# Section: Loops  
st.header("Loops in Python")  
st.write("""  
Loops allow us to execute a block of code multiple times.   
There are two main types of loops in Python: for loops and while loops.  
""")  
  
st.subheader("For Loop")  
st.code("""  
for i in range(5):  
    print(i)  
""")  
  
st.write("Try it out:")  
for_loop_range = st.slider("Select range for loop:", min_value=1, max_value=10, value=5)  
st.write("Loop Output:")  
for i in range(for_loop_range):  
    st.write(i)  
  
st.subheader("While Loop")  
st.code("""  
count = 0  
while count < 5:  
    print(count)  
    count += 1  
""")  
  
st.write("Try it out:")  
while_loop_limit = st.slider("Select limit for while loop:", min_value=1, max_value=10, value=5)  
count = 0  
st.write("Loop Output:")  
while count < while_loop_limit:  
    st.write(count)  
    count += 1  