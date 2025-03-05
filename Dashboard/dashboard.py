import streamlit as st
import pandas as pd

# Konfigurasi Halaman
st.set_page_config(page_title="Dashboard Penyewaan Sepeda", layout="wide")

# --- Membaca Dataset ---
@st.cache_data
def load_data():
    df = pd.read_csv("all_data.csv", parse_dates=["dteday"])
    return df

data = load_data()

# Sidebar untuk Filter
st.sidebar.header("🔍 Filter Data")
selected_month = st.sidebar.slider("Pilih Bulan", 1, 12, (1, 12))
selected_weather = st.sidebar.multiselect(
    "Pilih Kondisi Cuaca", options=data["weathersit"].unique(), default=data["weathersit"].unique()
)

# Filter data berdasarkan bulan dan cuaca
filtered_data = data[
    (data["dteday"].dt.month >= selected_month[0]) & (data["dteday"].dt.month <= selected_month[1]) &
    (data["weathersit"].isin(selected_weather))
]

# Judul Dashboard
st.title("📊 Dashboard Penyewaan Sepeda 🚲")
st.markdown("Analisis penyewaan sepeda berdasarkan cuaca dan waktu.")

# --- Tabel Dataset ---
st.write("## 📄 Dataset Penyewaan Sepeda")
st.dataframe(filtered_data.head(15))  # Menampilkan 10 data pertama setelah difilter

# --- Analisis 1: Pengaruh Cuaca terhadap Penyewaan ---
st.write("## ☀️ Pengaruh Cuaca terhadap Penyewaan Sepeda")
st.markdown(
    """
    Cuaca sangat mempengaruhi jumlah penyewaan sepeda.  
    Berikut ini adalah grafik jumlah penyewaan berdasarkan suhu (*temp*), suhu terasa (*atemp*), dan kelembaban (*hum*) per bulan.
    """
)

# Agregasi data per bulan untuk suhu, suhu terasa, dan kelembaban
monthly_data = filtered_data.groupby(filtered_data["dteday"].dt.month)[["temp", "atemp", "hum", "cnt"]].mean()

# Menampilkan data dalam satu frame
st.line_chart(monthly_data)

st.markdown(
    """
    **Kesimpulan:**
    - Semakin tinggi suhu (*temp*), jumlah penyewaan cenderung meningkat.
    - Suhu terasa (*atemp*) juga memiliki pola yang mirip dengan suhu.
    - Kelembaban (*hum*) tinggi dapat menyebabkan penurunan jumlah penyewaan.
    """
)

# --- Analisis 2: Jam Puncak Penyewaan Sepeda ---
st.write("## ⏰ Jam Puncak Penyewaan Sepeda")
st.markdown(
    """
    Grafik berikut menunjukkan jumlah rata-rata penyewaan sepeda pada setiap jam dalam sehari.
    """
)

# Hitung rata-rata penyewaan per jam
hourly_rental = filtered_data.groupby("hr")["cnt"].mean().reset_index()

# Visualisasi jam puncak penyewaan
st.bar_chart(hourly_rental.set_index("hr"))

st.markdown(
    """
    **Kesimpulan:**
    - Penyewaan sepeda mencapai puncaknya pada jam **07:00 - 09:00 (pagi)** dan **17:00 - 19:00 (sore)**.
    - Pola ini mengikuti aktivitas harian seperti jam kerja dan jam sekolah.
    """
)

# --- Kesimpulan Umum ---
st.write("## 📌 Kesimpulan Akhir")
st.markdown(
    """
    - **Cuaca berpengaruh terhadap penyewaan sepeda.** Penyewaan lebih tinggi saat cuaca cerah dan suhu nyaman.
    - **Suhu, suhu terasa, dan kelembaban mempengaruhi jumlah penyewaan.** Semakin panas, semakin banyak penyewaan, tetapi kelembaban tinggi bisa menurunkannya.
    - **Jam puncak penyewaan terjadi di pagi dan sore hari.** Hal ini mengikuti jadwal kerja dan sekolah.
    """
)

st.write("🚀 Dibuat dengan ❤️ menggunakan Streamlit dan Pandas.")
