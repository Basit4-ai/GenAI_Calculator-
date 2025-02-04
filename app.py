import streamlit as st
import sympy as sp
import math

# Streamlit App
st.title("Advanced Calculator App")

# User Inputs
st.write("Enter numbers and select an operation:")

num1 = st.number_input("Enter first number:", value=0.0, format="%.2f")
num2 = st.number_input("Enter second number:", value=0.0, format="%.2f")
use_third = st.checkbox("Use a third number?")
num3 = None

if use_third:
    num3 = st.number_input("Enter third number:", value=0.0, format="%.2f")

operation = st.selectbox(
    "Select Operation",
    [
        "Addition", "Subtraction", "Multiplication", "Division", 
        "Derivative", "Integration", "Factorial"
    ]
)

# Function to Perform Calculation
def calculate(n1, n2, n3, op):
    if op == "Addition":
        return n1 + n2
    elif op == "Subtraction":
        return n1 - n2
    elif op == "Multiplication":
        return n1 * n2
    elif op == "Division":
        return n1 / n2 if n2 != 0 else "Error: Division by zero"
    elif op == "Derivative":
        # Symbolic differentiation using SymPy
        x = sp.symbols('x')
        expr = x**n1 + x**n2  # Example: x^num1 + x^num2
        derivative = sp.diff(expr, x)
        return derivative
    elif op == "Integration":
        # Symbolic integration using SymPy
        x = sp.symbols('x')
        expr = x**n1 + x**n2  # Example: x^num1 + x^num2
        integral = sp.integrate(expr, x)
        return integral
    elif op == "Factorial":
        # Factorial calculation for integers
        if n1.is_integer() and n1 >= 0:
            return math.factorial(int(n1))
        else:
            return "Error: Factorial is only defined for non-negative integers."

# Compute and Display Result
if st.button("Calculate"):
    if operation in ["Derivative", "Integration", "Factorial"]:
        result = calculate(num1, num2, num3 if use_third else None, operation)
    else:
        result = calculate(num1, num2, num3 if use_third else None, operation)
    st.success(f"Result: {result}")

# Footer
st.caption("Powered by Streamlit")
