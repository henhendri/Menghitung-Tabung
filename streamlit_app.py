import streamlit as st
import math, time
import random

st.title("Menghitung total belanjaan dan kembalian di toko roti.")
  harga_roti_tawar = "12000"
  harga_kue_bolu = "25000"
  jumlah_roti_tawar = st.number_input("Masukan Jumlah roti ",0)
  jumlah_kue_bolu = st.number_input("Masukan Jumlah kue ",0)
  uang_bayar = st.number_input("Masukan Jumlah bayar ",0)

  total_harga = (harga_roti_tawar * jumlah_roti_tawar) + (harga_kue_bolu * jumlah_kue_bolu)
  kembalian = uang_bayar - total_harga

  print("Total belanjaan:", total_harga)
  print("Kembalian:", kembalian)



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
