# 📊 Dicoding Collection Dashboard

Dashboard ini digunakan untuk menganalisis data penyewaan sepeda berdasarkan berbagai faktor seperti cuaca, waktu, dan tren pengguna.

## 🚀 Setup & Installation

Ikuti langkah-langkah berikut untuk menginstal dan menjalankan proyek ini.

### **1️⃣ Impor proyek**

#### **🔹 Clone Repository**

```sh
# Clone repository dari GitHub
git clone <repo-url>
cd Proyek-Analisis-Data
```

#### **🔹 Ekstrak file zip dari Proyek ini**

Jika Anda memiliki file zip proyek, lakukan langkah berikut:

1. **Download file zip** dari sumber yang tersedia.
2. **Ekstrak file zip** menggunakan file manager bawaan sistem operasi Anda.
3. **Masuk ke folder proyek** hasil ekstraksi.

### **2️⃣ Buat Virtual Environment & Install Dependencies**

#### **🔹 Menggunakan Virtual Environment (venv)**

```sh
# Buat virtual environment
python -m venv venv

# Aktifkan virtual environment (Windows)
venv\Scripts\activate

# Aktifkan virtual environment (Mac/Linux)
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### **🔹 Menggunakan Anaconda**

```sh
# Buat environment baru
conda create --name bike-rental-dashboard python=3.9

# Aktifkan environment
conda activate bike-rental-dashboard

# Install dependencies
pip install -r requirements.txt
```

### **3️⃣ Jalankan Streamlit App**

```sh
streamlit run Dashboard/dashboard.py
```

📌 Pastikan Anda berada di direktori proyek sebelum menjalankan perintah ini.

---

### ⚠️ Catatan

Tidak semua sistem operasi mendukung langkah-langkah di atas secara langsung. Jika terjadi kendala:

- **Windows**: Pastikan Python dan pip sudah terinstal dengan benar.
- **Mac/Linux**: Gunakan perintah `python3` jika `python` tidak dikenali.
- **Anaconda**: Pastikan `conda` sudah dikonfigurasi dengan benar.

Sekarang, dashboard Anda seharusnya dapat berjalan dengan baik di browser! 🎉
