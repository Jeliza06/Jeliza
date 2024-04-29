import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title('This is an example streamlit app')

data = pd.DataFrame({
    "x": np.arange(1, 101),
    "y": np.random.normal(0, 1, 100)
})

subset_size = st.slider("Select the number of data points", 10, 100, 50)

plt.plot(data["x"][:subset_size], data["y"][:subset_size], "-o")
st.pyplot(plt)

notes = st.text_area("Add your comments or notes here")
