import pandas as pd

# 1. Membuat dataset secara manual di dalam kode
data = pd.DataFrame(
    [
        {"nama": "Andi", "kelas": "XI", "jam_belajar": 3, "nilai_kuis": 82},
        {"nama": "Bela", "kelas": "XI", "jam_belajar": 2, "nilai_kuis": 68},
        {"nama": "Citra", "kelas": "X", "jam_belajar": 5, "nilai_kuis": 95},
        {"nama": "Doni", "kelas": "X", "jam_belajar": 1, "nilai_kuis": 60},
        {"nama": "Eka", "kelas": "XI", "jam_belajar": 4, "nilai_kuis": 78},
        {"nama": "Farhan", "kelas": "X", "jam_belajar": 2, "nilai_kuis": 73},
        {"nama": "Gita", "kelas": "XI", "jam_belajar": 6, "nilai_kuis": 91},
        {"nama": "Hana", "kelas": "X", "jam_belajar": 3, "nilai_kuis": 75},
        {"nama": "Irfan", "kelas": "XI", "jam_belajar": 1, "nilai_kuis": 55},
        {"nama": "Jihan", "kelas": "X", "jam_belajar": 4, "nilai_kuis": 88},
    ]
)

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