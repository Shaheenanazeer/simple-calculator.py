import streamlit as st

def calculate(num1, num2, operator):
    if operator == '+':  
        return num1 + num2
    elif operator == '-':  
        return num1 - num2
    elif operator == '*':  
        return num1 * num2
    elif operator == '/':  
        return num1 / num2 if num2 != 0 else "Cannot divide by zero"
    else:
        return "Invalid operator"

st.title("Calculator")

num1 = st.number_input("Enter the first number")
num2 = st.number_input("Enter the second number")
operator = st.selectbox("Select an operator", ["+", "-", "*", "/"])

# Function Call
result = calculate(num1, num2, operator)

#  Output
st.write("The result is:", result)
