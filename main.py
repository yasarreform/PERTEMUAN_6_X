import pandas as pd

# 1. Membaca file CSV
data = pd.read_csv("dataset_nilai_kuis.csv")

# 2. Menampilkan lima data pertama
print("=== DATA NILAI KUIS TDC ===")
print(data.head())

# 3. Menampilkan jumlah baris dan kolom
print("\nUkuran dataset (baris, kolom):")
print(data.shape)

# 4. Menghitung rata-rata nilai kuis
rata_rata = data["nilai_kuis"].mean()
print("\nRata-rata nilai kuis:")
print(round(rata_rata, 2))

# 5. Menampilkan siswa dengan nilai minimal 75
print("\nSiswa dengan nilai minimal 75:")
nilai_baik = data[data["nilai_kuis"] >= 75]
print(nilai_baik[["nama", "nilai_kuis"]])
