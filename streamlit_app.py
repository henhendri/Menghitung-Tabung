import streamlit as st
import math, time
from st_pages import add_page_title, get_nav_from_toml

st.set_page_config(layout="wide")

sections = st.sidebar.toggle("Sections", value=True, key="use_sections")

nav = get_nav_from_toml(
    ".streamlit/pages_sections.toml" if sections else ".streamlit/pages.toml"
)

st.logo("logo.png")

pg = st.navigation(nav)

add_page_title(pg)

pg.run()


st.title("Menghitung :blue[Volume Tabung] :rocket:")

r = st.number_input("Masukan Jari-Jari (cm): ",0)
t = st.number_input("Masukan Tinggi (cm): ",0)

if st.button("Hitung Volume", type="primary"):
  loading = st.progress(0)
  for i in range(100):
    time.sleep(0.01)
    loading.progress(i+1)
    
  v = math.pi*(r**2)*t
  st.success(f'Volume tabung adalah {v:.2f}')

col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")
