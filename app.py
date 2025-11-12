import streamlit as st
from multiapp import MultiApp
import st_tailwind as tw

import calculator
import bmi
import area

app = MultiApp()

app.add_app("Calculator", calculator.app)
app.add_app("BMI Calculator", bmi.app)
app.add_app("Area Calculator", area.app)

app.run()
