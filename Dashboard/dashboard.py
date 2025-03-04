import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- Konfigurasi Halaman ---
st.set_page_config(page_title="Dashboard Penyewaan Sepeda", layout="wide")

# --- Membaca Dataset ---
@st.cache_data
def load_data():
    df = pd.read_csv("all_data.csv", parse_dates=["dteday"])
    return df

data = load_data()

# --- Sidebar untuk Filter ---
st.sidebar.header("Filter Data")
selected_hours = st.sidebar.slider("Pilih Rentang Jam", 0, 23, (0, 23))
selected_weather = st.sidebar.multiselect(
    "Pilih Kondisi Cuaca", options=data["weathersit"].unique(), default=data["weathersit"].unique()
)

# Filter Data Berdasarkan Jam dan Cuaca
filtered_data = data[
    (data["hr"] >= selected_hours[0]) & (data["hr"] <= selected_hours[1]) &
    (data["weathersit"].isin(selected_weather))
]

# --- Judul Dashboard ---
st.title("📊 Dashboard Penyewaan Sepeda 🚲")
st.markdown("Analisis penyewaan sepeda berdasarkan waktu dan kondisi cuaca.")

# --- Menampilkan Data ---
st.write("### Data Penyewaan Sepeda")
st.dataframe(filtered_data)

# --- Visualisasi 1: Pengaruh Cuaca terhadap Penyewaan Sepeda ---
st.write("### 🔆 Pengaruh Cuaca terhadap Penyewaan Sepeda")

fig, ax = plt.subplots(figsize=(8, 5))
sns.barplot(x="weathersit", y="cnt", data=data, ax=ax, palette="viridis")
ax.set_xlabel("Kondisi Cuaca")
ax.set_ylabel("Jumlah Penyewaan")
ax.set_xticklabels(["Clear", "Cloudy", "Light Rain", "Heavy Rain"])
st.pyplot(fig)

st.markdown(
    """
    - **Cuaca cerah** memiliki jumlah penyewaan tertinggi.
    - Saat hujan, jumlah penyewaan cenderung lebih rendah.
    """
)

# --- Visualisasi 2: Jam dengan Penyewaan Tertinggi ---
st.write("### ⏰ Jam Puncak Penyewaan Sepeda")

fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x="hr", y="cnt", data=data, ax=ax, marker="o", color="b")
ax.set_xlabel("Jam")
ax.set_ylabel("Jumlah Penyewaan")
st.pyplot(fig)

st.markdown(
    """
    - Penyewaan sepeda mencapai puncaknya pada jam tertentu (biasanya pagi dan sore hari).
    - Pola ini bisa dipengaruhi oleh jam kerja atau aktivitas rutin pengguna.
    """
)

# --- Kesimpulan ---
st.write("### 📌 Kesimpulan")
st.markdown(
    """
    - **Kondisi Cuaca Berpengaruh:** Cuaca cerah meningkatkan jumlah penyewaan sepeda.
    - **Jam Sibuk:** Penyewaan biasanya lebih tinggi pada jam kerja (07:00 - 09:00 dan 17:00 - 19:00).
    - **Tren Harian:** Analisis jam menunjukkan pola tertentu yang dapat dimanfaatkan untuk pengelolaan sepeda.
    """
)

st.write("🚀 Dibuat dengan ❤️ menggunakan Streamlit, Pandas, Seaborn, dan Matplotlib.")

