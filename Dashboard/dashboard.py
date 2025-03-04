import streamlit as st
import pandas as pd
import os

# Path ke file CSV
data_path = "../Data/day.csv"

# Load data
def load_data():
    if os.path.exists(data_path):
        return pd.read_csv(data_path)
    else:
        st.error(f"File {data_path} tidak ditemukan!")
        return None

df = load_data()

# Tampilan utama aplikasi
st.title("Bike Sharing Dataset Viewer")

if df is not None:
    # Menampilkan beberapa baris pertama
    st.subheader("Data Preview")
    st.write(df.head())
    
    # Menampilkan statistik dasar
    st.subheader("Statistik Data")
    st.write(df.describe())
    
    # Menampilkan jumlah penyewa sepeda berdasarkan hari
    st.subheader("Jumlah Penyewa Sepeda")
    st.line_chart(df[['casual', 'registered', 'cnt']])
else:
    st.warning("Data tidak tersedia. Pastikan file CSV berada di folder yang benar.")
