import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
 
col1, col2 = st.columns([3, 8])

with col1:
    custom_title = st.text_input("Enter a custom title:", "Survivors and Deaths")
    st.write(f"## {custom_title}")
 
data = pd.read_excel(".\DataAnalysisAssignment4\data\Titanic Data.xlsx")

survival_counts = data["Survived"].value_counts()
survival_counts.index = ["Died", "Survived"] 

fig, ax = plt.subplots()
ax.bar(survival_counts.index, survival_counts.values)

with col2:
    st.pyplot(fig)
