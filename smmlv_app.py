import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
# Dictionary with velues per year
SMMLV = {
    2020: 980656,
    2021: 1014980,
    2022: 1117172,
    2023: 1300606,
    2024: 1462000,
    2025: 1623500,
}
#Set image to customize 
from PIL import Image
#Open de image
image = Image.open("colombia.png")
st.image(image, use_container_width=True)
# App title
st.title("SMMLV Calculator - Colombia💰")
st.write("This app allows you to calculate the total amount in COP based on the Colombian minimum wage (SMMLV).☕")
#set columns
col1, col2 = st.columns(2)
# year selection
with col1:
    year = st.selectbox("Select the year:", list(SMMLV.keys()), key="year")

# Input of the number of salaries
with col2:
    number = st.number_input("How many SMMLV do you want to calculate?", min_value=1, step=1, key="number")

# Caculate button
if st.button("Calculate"):
    total = SMMLV[year] * number
    st.success(f"The total amount is: {total:,} COP")

# Visualización
st.header("📈 Historical SMMLV Data (2020–2025)")

smmlv_df = pd.DataFrame(list(SMMLV.items()), columns=["Year", "SMMLV"])
smmlv_df["Change (%)"] = smmlv_df["SMMLV"].pct_change().fillna(0) * 100
smmlv_df["Change (%)"] = smmlv_df["Change (%)"].round(2)

st.dataframe(smmlv_df, use_container_width=True)

# Gráfico con matplotlib
fig, ax = plt.subplots()
ax.plot(smmlv_df["Year"], smmlv_df["SMMLV"], marker='o', linestyle='-', color='blue')
ax.set_title("SMMLV Evolution (2020–2025)")
ax.set_xlabel("Year")
ax.set_ylabel("SMMLV (COP)")
ax.grid(True)

st.pyplot(fig)
# If you want to run this program on your browser
# streamlit run smmlv_app.py