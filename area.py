import streamlit as st
import math

def app():
  st.title("Area Calculator")
  st.write("Calculate the area of various shapes.")

  shape = st.selectbox(
      "Select a shape",
      ("Circle", "Rectangle", "Triangle")
  )

  area = 0
  if shape == "Circle":
    st.subheader("Circle Area Calculation")
    radius = st.number_input("Enter the radius of the circle", min_value=0.0, value=1.0)
    if st.button("Calculate Circle Area"):
      area = math.pi * (radius ** 2)
      st.write(f"The area of the circle is: {area:.2f}")
  
  elif shape == "Rectangle":
    st.subheader("Rectangle Area Calculation")
    length = st.number_input("Enter the length of the rectangle", min_value=0.0, value=1.0)
    width = st.number_input("Enter the width of the rectangle", min_value=0.0, value=1.0)
    if st.button("Calculate Rectangle Area"):
      area = length * width
      st.write(f"The area of the rectangle is: {area:.2f}")
  
  elif shape == "Triangle":
    st.subheader("Triangle Area Calculation")
    base = st.number_input("Enter the base of the triangle", min_value=0.0, value=1.0)
    height = st.number_input("Enter the height of the triangle", min_value=0.0, value=1.0)
    if st.button("Calculate Triangle Area"):
      area = 0.5 * base * height
      st.write(f"The area of the triangle is: {area:.2f}")
