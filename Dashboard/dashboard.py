import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Konfigurasi Halaman
st.set_page_config(page_title="Dashboard Penyewaan Sepeda", layout="wide")

# --- Membaca Dataset ---
@st.cache_data
def load_data():
    df = pd.read_csv("all_data.csv", parse_dates=["dteday"])
    return df

data = load_data()

# --- Tampilkan Dataset ---
st.write("## \U0001F4C1 Dataset Penyewaan Sepeda")
st.dataframe(data)

# --- Analisis 1: Penyewaan Sepeda Per Bulan dan Pengaruh Cuaca ---
st.write("## 📆 Penyewaan Sepeda Per Bulan dan Pengaruh Cuaca")

# Pilihan untuk filter cuaca
weather_options = data['weathersit'].unique()
selected_weather = st.multiselect("Pilih Kondisi Cuaca", options=weather_options, default=weather_options)

# Filter data berdasarkan pilihan pengguna
filtered_data = data[data['weathersit'].isin(selected_weather)]

fig, ax = plt.subplots(figsize=(14, 6))
sns.lineplot(data=filtered_data, x="mnth", y="cnt", hue="weathersit", marker="o", palette="viridis", ax=ax)
ax.set_title("Tren Penyewaan Sepeda Berdasarkan Kondisi Cuaca", size=18)
ax.set_xlabel("Bulan", size=14)
ax.set_ylabel("Jumlah Penyewaan", size=14)
ax.legend(title="Kondisi Cuaca")
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(14, 6))
sns.barplot(data=filtered_data, x="mnth", y="cnt", palette="coolwarm", ax=ax)
ax.set_title("Jumlah Penyewaan Sepeda Per Bulan", size=18)
ax.set_xlabel("Bulan", size=14)
ax.set_ylabel("Jumlah Penyewaan", size=14)
st.pyplot(fig)

st.write("### Kesimpulan 1: Penyewaan Sepeda Per Bulan dan Pengaruh Cuaca")
st.markdown("""
- Penyewaan sepeda cenderung meningkat pada bulan-bulan tertentu.
- Kondisi cuaca berpengaruh terhadap jumlah penyewaan sepeda.
- Cuaca yang lebih cerah cenderung meningkatkan jumlah penyewaan.
""")

# --- Analisis 2: Jam Puncak Penyewaan Sepeda ---
st.write("## ⏰ Jam Puncak Penyewaan Sepeda")

# Pilihan untuk filter hari
data['day'] = data['dteday'].dt.date
day_options = data['day'].unique()
selected_day = st.selectbox("Pilih Tanggal", options=day_options)

# Filter data berdasarkan pilihan pengguna
filtered_day_data = data[data['day'] == selected_day]

# Hitung total penyewaan per jam berdasarkan hari yang dipilih
hourly_rental = filtered_day_data.groupby("hr")["cnt"].sum().reset_index()
peak_hour = hourly_rental.loc[hourly_rental["cnt"].idxmax()]

fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(data=hourly_rental, x="hr", y="cnt", palette="coolwarm", ax=ax)
ax.axvline(x=hourly_rental[hourly_rental["hr"] == peak_hour["hr"].astype(int)].index[0], color='red', linestyle='--', label=f'Puncak: {peak_hour["hr"]}')
ax.set_xlabel("Jam")
ax.set_ylabel("Jumlah Penyewaan Sepeda")
ax.set_title("Jumlah Penyewaan Sepeda per Jam")
ax.legend()
st.pyplot(fig)

st.bar_chart(hourly_rental.set_index("hr"))

st.write("### Kesimpulan 2: Jam Puncak Penyewaan Sepeda")
st.markdown("""
- Jam puncak penyewaan sepeda terjadi pada jam tertentu dalam sehari.
- Jika ada beberapa jam dengan jumlah penyewaan yang sama, maka akan dipilih salah satu sebagai jam puncak.
- Pola penyewaan pada jam tertentu menunjukkan adanya kebiasaan pengguna.
""")

# --- Analisis 3: Perbandingan Penyewaan Sepeda per Tahun ---
st.write("## 📊 Perbandingan Penyewaan Sepeda per Tahun")

fig, ax = plt.subplots(figsize=(10, 6))
sns.barplot(data=data, x="yr", y="cnt", palette="magma", errorbar=None, ax=ax)
ax.set_xlabel("Tahun")
ax.set_ylabel("Rata-rata Jumlah Penyewaan Sepeda")
ax.set_title("Perbandingan Penyewaan Sepeda per Tahun")
st.pyplot(fig)

st.bar_chart(data.groupby("yr")["cnt"].sum())

st.write("### Kesimpulan 3: Perbandingan Penyewaan Sepeda per Tahun")
st.markdown("""
- Penyewaan sepeda mengalami peningkatan atau penurunan dari tahun ke tahun.
- Faktor eksternal seperti tren penggunaan sepeda dan kebijakan pemerintah dapat memengaruhi jumlah penyewaan.
""")

# --- Kesimpulan Umum ---
st.write("## 📌 Kesimpulan Akhir")
st.markdown("""
- **Penyewaan sepeda mengalami pola fluktuatif sepanjang tahun.**
- **Jam puncak penyewaan terjadi di pagi dan sore hari.**
- **Cuaca mempengaruhi pola penyewaan sepeda secara signifikan.**
""")

st.write("🚀 Dibuat dengan ❤️ menggunakan Streamlit.")
