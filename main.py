import streamlit as st

from lc_pet_names import lc_pet_names

st.title("Pet name suggestor")

pet_type= st.sidebar.selectbox(label="pet type", options=["dog", "cat"])
pet_colors = st.sidebar.multiselect(label="colors", options=["white", "red", "black"])

names = lc_pet_names(str(pet_type), str(pet_colors))

st.text(names)