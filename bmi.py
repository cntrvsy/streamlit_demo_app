import streamlit as st

def app():
  st.title("BMI Calculator")
  st.write("Calculate your Body Mass Index")

  weight = st.number_input("Enter your weight in kilograms (kg)", min_value=1.0, value=70.0)
  height = st.number_input("Enter your height in meters (m)", min_value=0.1, value=1.75)

  if st.button("Calculate BMI"):
    if height > 0:
      bmi = weight / (height ** 2)
      st.write(f"Your BMI is: {bmi:.2f}")

      if bmi < 18.5:
        st.warning("Category: Underweight")
      elif 18.5 <= bmi < 24.9:
        st.success("Category: Normal weight")
      elif 25 <= bmi < 29.9:
        st.warning("Category: Overweight")
      else:
        st.error("Category: Obesity")
    else:
      st.error("Height cannot be zero or negative!")
