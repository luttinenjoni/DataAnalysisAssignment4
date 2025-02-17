import streamlit as st
import pandas as pd
 
st.write("""
# Survived vs Surviwont
""")
 
data = pd.read_excel(".\DataAnalysisAssignment4\data\Titanic Data.xlsx")

survival_counts = data["Survived"].value_counts()

st.bar_chart(survival_counts)
