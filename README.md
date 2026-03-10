# Boundary Value Analysis (BVA) Testing Tool

Boundary Value Analysis (BVA) adalah aplikasi berbasis desktop yang dirancang untuk mengotomatisasi pengujian perangkat lunak menggunakan teknik analisis nilai batas. Proyek ini bertujuan untuk memvalidasi apakah sebuah sistem dapat menangani input pada batas minimum, maksimum, serta nilai di antaranya dengan benar, guna meminimalisir kesalahan logika pada rentang transisi data.

## 🧪 Konsep Pengujian

Aplikasi ini mengimplementasikan teknik *Black-Box Testing* yang fokus pada nilai ekstrem. Sebagai contoh, jika sebuah sistem menerima rentang input $1$ hingga $100$, BVA akan menguji nilai-nilai kritis seperti:
- **Nilai Batas Bawah:** $1$ (Min) dan $2$ (Min+1).
- **Nilai Batas Atas:** $99$ (Max-1) dan $100$ (Max).
- **Nilai di Luar Batas:** $0$ (Invalid) dan $101$ (Invalid).

## 🚀 Fitur Utama

- **Input Range Validation:** Menentukan parameter batas bawah dan batas atas secara dinamis.
- **Automated Test Generation:** Menghasilkan kasus uji (*test cases*) berdasarkan rentang yang ditentukan.
- **Status Verifikasi:** Menampilkan hasil "Pass" atau "Fail" untuk setiap input yang diuji.
- **Logika Perbandingan Akurat:** Menggunakan operator relasional yang presisi untuk menentukan validitas data.

## 🛠️ Teknologi yang Digunakan

- **Bahasa Pemrograman:** Visual Basic .NET (VB.NET)
- **Framework:** .NET Framework
- **Metodologi:** Software Quality Assurance (SQA) & Boundary Value Analysis.

## 📋 Mengapa BVA Penting?

Sebagian besar kesalahan dalam pemrograman terjadi pada nilai batas (misalnya penggunaan `<` yang seharusnya `<=` atau sebaliknya). Alat ini dikembangkan untuk membantu pengembang dan *Quality Assurance* (QA) dalam mendeteksi *off-by-one errors* secara sistematis.

## 🚀 Cara Menjalankan

1. **Clone Repositori:**
   ```bash
   git clone [https://github.com/asboyy/Boundary-Value-Analysis.git](https://github.com/asboyy/Boundary-Value-Analysis.git)
