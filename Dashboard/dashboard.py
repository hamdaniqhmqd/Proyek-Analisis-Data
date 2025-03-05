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

# Tampilkan Dataset
st.write("## \U0001F4C1 Dataset Penyewaan Sepeda")
st.dataframe(data)

# Judul Dashboard
st.title("📊 Dashboard Penyewaan Sepeda 🚲")
st.markdown("Analisis penyewaan sepeda berdasarkan cuaca dan waktu.")

# --- Analisis 1: Penyewaan Sepeda Per Bulan dan Pengaruh Cuaca ---
st.write("## 📆 Penyewaan Sepeda Per Bulan dan Pengaruh Cuaca")

fig, ax = plt.subplots(figsize=(14, 6))
sns.lineplot(data=data, x="mnth", y="cnt", hue="weathersit", marker="o", palette="viridis", ax=ax)
ax.set_title("Tren Penyewaan Sepeda Berdasarkan Kondisi Cuaca", size=18)
ax.set_xlabel("Bulan", size=14)
ax.set_ylabel("Jumlah Penyewaan", size=14)
ax.legend(title="Kondisi Cuaca")
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(14, 6))
sns.barplot(data=data, x="mnth", y="cnt", palette="coolwarm", ax=ax)
ax.set_title("Jumlah Penyewaan Sepeda Per Bulan", size=18)
ax.set_xlabel("Bulan", size=14)
ax.set_ylabel("Jumlah Penyewaan", size=14)
st.pyplot(fig)

st.markdown("""
**Kesimpulan:**
- Tren penyewaan cenderung meningkat pada bulan-bulan tertentu.
- Faktor eksternal seperti musim dan liburan mungkin berpengaruh.
""")

# --- Analisis 2: Jam Puncak Penyewaan Sepeda ---
st.write("## ⏰ Jam Puncak Penyewaan Sepeda")

# Hitung rata-rata penyewaan per jam
hourly_rental = data.groupby("hr")["cnt"].mean().reset_index()
peak_hour = hourly_rental.loc[hourly_rental["cnt"].idxmax()]

fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(data=hourly_rental, x="hr", y="cnt", palette="coolwarm", ax=ax)
ax.axvline(peak_hour["hr"], color='red', linestyle='--', label=f'Puncak: {peak_hour["hr"]}')
ax.set_xlabel("Jam")
ax.set_ylabel("Rata-rata Penyewaan Sepeda")
ax.set_title("Jumlah Penyewaan Sepeda per Jam")
ax.legend()
st.pyplot(fig)

st.bar_chart(hourly_rental.set_index("hr"))

st.markdown(f"""
**Kesimpulan:**
- Penyewaan sepeda mencapai puncak pada jam **{peak_hour['hr']}**.
- Pola ini mengikuti jam kerja dan aktivitas harian.
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

# --- Kesimpulan Umum ---
st.write("## 📌 Kesimpulan Akhir")
st.markdown("""
- **Penyewaan sepeda mengalami pola fluktuatif sepanjang tahun.**
- **Jam puncak penyewaan terjadi di pagi dan sore hari.**
""")

st.write("🚀 Dibuat dengan ❤️ menggunakan Streamlit.")
