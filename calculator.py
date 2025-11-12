import streamlit as st

def app():
  st.title("Calculator")
  st.write("Simple Calculator")

  num1 = st.number_input("Enter the first number", value=0.0)
  num2 = st.number_input("Enter the second number", value=0.0)

  operation = st.selectbox(
      "Select an operation",
      ("+", "-", "*", "/")
  )

  if st.button("Calculate"):
    result = 0
    if operation == "+":
      result = num1 + num2
    elif operation == "-":
      result = num1 - num2
    elif operation == "*":
      result = num1 * num2
    elif operation == "/":
      if num2 != 0:
        result = num1 / num2
      else:
        st.error("Cannot divide by zero!")
        return
    st.write(f"The result is: {result}")
