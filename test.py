import random
import pandas as pd

# --- DATA YANG DIBERIKAN ---
# (Saya sedikit merapikan data, seperti menghapus dosen kosong)

MATA_KULIAH = {
    # Semester 1
    "Algoritma dan Pemrograman": {"sks": 3, "semester": 1}, "Bahasa Inggris": {"sks": 2, "semester": 1},
    "Fisika 1": {"sks": 3, "semester": 1}, "Matematika 1": {"sks": 3, "semester": 1},
    "Matematika Diskrit": {"sks": 3, "semester": 1}, "Pengantar Informatika": {"sks": 2, "semester": 1},
    "Sistem Digital": {"sks": 3, "semester": 1},
    # Semester 3
    "Agama Islam": {"sks": 2, "semester": 3}, "Agama Kristen": {"sks": 2, "semester": 3},
    "Agama Katolik": {"sks": 2, "semester": 3}, "Agama Buddha": {"sks": 2, "semester": 3},
    "Aljabar Liner dan Geometri": {"sks": 3, "semester": 2}, "Arsitektur Komputer": {"sks": 3, "semester": 3},
    "Pancasila": {"sks": 2, "semester": 3}, "Pengantar Kecerdasan Artifisial": {"sks": 3, "semester": 3},
    "Sistem Operasi": {"sks": 3, "semester": 3}, "Struktur Data": {"sks": 4, "semester": 3},
    # Semester 5
    "Desain Web": {"sks": 3, "semester": 5}, "Implementasi dan Pengujian Perangkat Lunak": {"sks": 3, "semester": 5},
    "Interaksi Manusia dan Komputer": {"sks": 3, "semester": 5}, "Manajemen Basis Data": {"sks": 3, "semester": 5},
    "Pemrograman Fungsional": {"sks": 3, "semester": 5}, "Pengolahan Citra Digital": {"sks": 3, "semester": 5},
    # Semester 6
    "Deep Learning": {"sks": 3, "semester": 6}, "Sistem Paralel dan Terdistribusi": {"sks": 3, "semester": 6},
    # Semester 7
    "Capstone Project": {"sks": 4, "semester": 7}, "Kapita Selekta": {"sks": 2, "semester": 7},
    "Keamanan Siber": {"sks": 3, "semester": 7}, "Kecerdasan Web": {"sks": 3, "semester": 7},
    "Keprofesian Informatika": {"sks": 2, "semester": 7}, "Komputasi Evolusioner": {"sks": 3, "semester": 7},
    "Manajemen Proyek TIK": {"sks": 3, "semester": 7}, "Pemrosesan Bahasa Alami": {"sks": 3, "semester": 7},
    "Pengembangan Aplikasi Perangkat Bergerak": {"sks": 3, "semester": 7}, "Sains Data": {"sks": 3, "semester": 7},
    "Visi Komputer": {"sks": 3, "semester": 7},
}

PENGAJAR_MATKUL = {
    "Agama Islam": ["Suriansyah S.Pd,M.Pd.", "Muhammad Gufron S.Pd, M.Pd"], "Agama Kristen": ["Silas Ratu M.Pd.K."],
    "Agama Katolik": ["Andreas Joni Pasundan S.S,Bth"], "Agama Buddha": ["Maryono S.Si, M.Si."],
    "Algoritma dan Pemrograman": ["Rizal Kusuma Putra, M.T.", "Gusti Ahmad Fanshuri Alfarisy, S.Kom., M.Kom."],
    "Bahasa Inggris": ["Yustina Fitriani, S.Pd, M.Pd.", "Alif Suci Dirgantari S.Pd, M.Pd"],
    "Fisika 1": ["Febrian Dedi Sastrawan S.si, M.Sc.", "Fadli Robiandi S.Si, M.Si"],
    "Matematika 1": ["Winarni, S.Si, M.Si:", "Retno Wahyu Dewanti S.Si, M.Si"],
    "Pancasila": ["Akbar Taufik Amrullah S.H., M.Kn.", "Farida Nur Hidayah, S.H, M.H."],
    "Aljabar Liner dan Geometri": ["Ramadhan Paninggalih S.Si., M.Si., M.Sc."],
    "Arsitektur Komputer": ["Aninditya Anggari Nuryono, S.T., M.Eng.", "Riska Kurniyanto Abdullah, S.T., M.Kom."],
    "Capstone Project": ["Ramadhan Paninggalih S.Si., M.Si., M.Sc."], "Deep Learning": ["Boby Mogi Pratama, S.Si., M.Han."],
    "Desain Web": ["Rizal Kusuma Putra, M.T."], "Implementasi dan Pengujian Perangkat Lunak": ["Nur Fajri Azhar S.Kom., M.Kom."],
    "Interaksi Manusia dan Komputer": ["Nisa Rizqiya Fadhliana, S.Kom., M.T."], "Kapita Selekta": ["Nisa Rizqiya Fadhliana, S.Kom., M.T."],
    "Keamanan Siber": ["Darmansyah, S.Si., M.T.I"], "Kecerdasan Web": ["Gusti Ahmad Fanshuri Alfarisy, S.Kom., M.Kom."],
    "Keprofesian Informatika": ["Nur Fajri Azhar S.Kom., M.Kom.", "Darmansyah, S.Si., M.T.I"], "Kerja Praktek": ["Nisa Rizqiya Fadhliana, S.Kom., M.T."],
    "Komputasi Evolusioner": ["Muchammad Chandra Cahyo Utomo, S. Kom., M. Kom."], "Manajemen Basis Data": ["Bowo Nugroho, S.Kom., M.Eng."],
    "Manajemen Proyek TIK": ["Riska Kurniyanto Abdullah, S.T., M.Kom."], "Matematika Diskrit": ["Ramadhan Paninggalih S.Si., M.Si., M.Sc."],
    "Pemrograman Fungsional": ["Gusti Ahmad Fanshuri Alfarisy, S.Kom., M.Kom."], "Pemrosesan Bahasa Alami": ["Bima Prihasto, S.SI., M.Si., Ph.D."],
    "Pengantar Informatika": ["Muchammad Chandra Cahyo Utomo, S. Kom., M. Kom."],
    "Pengantar Kecerdasan Artifisial": ["Bima Prihasto, S.SI., M.Si., Ph.D.", "Gusti Ahmad Fanshuri Alfarisy, S.Kom., M.Kom."],
    "Pengembangan Aplikasi Perangkat Bergerak": ["Rizal Kusuma Putra, M.T."], "Pengolahan Citra Digital": ["Rizky Amelia, S.Si., M.Han."],
    "Proposal Tugas Akhir": ["Nisa Rizqiya Fadhliana, S.Kom., M.T."], "Sains Data": ["Ramadhan Paninggalih S.Si., M.Si., M.Sc."],
    "Sistem Digital": ["Boby Mugi Pratama, S.Si., M.Han."], "Sistem Operasi": ["Darmansyah, S.SI., M.T.I"],
    "Sistem Paralel dan Terdistribusi": ["Riska Kurniyanto Abdullah, S.T., M.Kom."],
    "Struktur Data": ["Muchammad Chandra Cahyo Utomo, S. Kom., M. Kom.", "Bowo Nugroho, S.Kom., M.Eng."],
    "Tugas Akhir": ["Nisa Rizqiya Fadhliana, S.Kom., M.T."], "Visi Komputer": ["Rizky Amelia, S.Si., M.Han."]
}

WAKTU_SLOT = {
    ("Senin", "07:30"): 1, ("Senin", "10:20"): 2, ("Senin", "13:00"): 3, ("Senin", "16:00"): 4,
    ("Selasa", "07:30"): 1, ("Selasa", "10:20"): 2, ("Selasa", "13:00"): 3, ("Selasa", "16:00"): 4,
    ("Rabu", "07:30"): 1, ("Rabu", "10:20"): 2, ("Rabu", "13:00"): 3, ("Rabu", "16:00"): 4,
    ("Kamis", "07:30"): 1, ("Kamis", "10:20"): 2, ("Kamis", "13:00"): 3, ("Kamis", "16:00"): 4,
    ("Jumat", "07:30"): 1, ("Jumat", "10:20"): 2, ("Jumat", "13:00"): 3, ("Jumat", "16:00"): 4,
}

RUANGAN = [f'G{f}{r}' for f in range(1, 4) for r in range(101, 107)] + \
          [f'F{f}{r}' for f in range(1, 4) for r in range(101, 107)] + \
          [f'E{f}{r}' for f in range(1, 4) for r in range(101, 107)]
          
# --- PRE-PROCESSING DATA ---
# Membuat daftar semua kelas yang akan dijadwalkan (masing-masing 2 kelas A dan B)
DAFTAR_KELAS = []
for nama_matkul, detail in MATA_KULIAH.items():
    if nama_matkul in PENGAJAR_MATKUL and PENGAJAR_MATKUL[nama_matkul]:
        DAFTAR_KELAS.append({"nama_kelas": f"{nama_matkul} A", "matkul": nama_matkul, "sks": detail["sks"]})
        DAFTAR_KELAS.append({"nama_kelas": f"{nama_matkul} B", "matkul": nama_matkul, "sks": detail["sks"]})

LIST_WAKTU = list(WAKTU_SLOT.keys())

# --- PARAMETER ALGORITMA GENETIKA ---
UKURAN_POPULASI = 100
TINGKAT_MUTASI = 0.02
JUMLAH_GENERASI = 500
UKURAN_TURNAMEN = 5
JUMLAH_ELITE = 2

# --- FUNGSI-FUNGSI ALGORITMA GENETIKA ---

def buat_individu():
    """Membuat satu individu (satu jadwal lengkap) secara acak."""
    jadwal = []
    for kelas in DAFTAR_KELAS:
        dosen = random.choice(PENGAJAR_MATKUL[kelas["matkul"]])
        waktu = random.choice(LIST_WAKTU)
        ruang = random.choice(RUANGAN)
        jadwal.append({
            "kelas": kelas["nama_kelas"],
            "matkul": kelas["matkul"],
            "sks": kelas["sks"],
            "dosen": dosen,
            "waktu": waktu,
            "ruang": ruang,
            "sesi": WAKTU_SLOT[waktu]
        })
    return jadwal

def hitung_fitness(individu):
    """Menghitung fitness berdasarkan jumlah penalti. Semakin sedikit penalti, semakin tinggi fitness."""
    penalti = 0
    
    # Check tabrakan (dosen atau ruangan pada waktu yang sama)
    slot_dosen = {}
    slot_ruang = {}

    for item in individu:
        waktu = item["waktu"]
        dosen = item["dosen"]
        ruang = item["ruang"]
        
        # Penalti 1: Dosen yang sama mengajar di waktu yang sama
        if (waktu, dosen) in slot_dosen:
            penalti += 1
        else:
            slot_dosen[(waktu, dosen)] = True
            
        # Penalti 2: Ruangan yang sama dipakai di waktu yang sama
        if (waktu, ruang) in slot_ruang:
            penalti += 1
        else:
            slot_ruang[(waktu, ruang)] = True
            
        # Penalti 3: Matkul >= 3 SKS di sesi 2 atau 4
        if item["sks"] >= 3 and item["sesi"] in [2, 4]:
            penalti += 1
            
    # Fitness dihitung agar nilai yang lebih tinggi lebih baik
    return 1 / (1 + penalti)

def seleksi_turnamen(populasi):
    """Memilih individu terbaik dari sejumlah kecil individu acak."""
    turnamen = random.sample(populasi, UKURAN_TURNAMEN)
    pemenang = max(turnamen, key=lambda x: x['fitness'])
    return pemenang['individu']

def crossover(parent1, parent2):
    """Menggabungkan dua parent untuk membuat child baru (single-point crossover)."""
    titik_crossover = random.randint(1, len(parent1) - 1)
    child = parent1[:titik_crossover] + parent2[titik_crossover:]
    return child

def mutasi(individu):
    """Mengubah satu gen (satu jadwal kelas) secara acak pada individu."""
    for i in range(len(individu)):
        if random.random() < TINGKAT_MUTASI:
            # Pilih item jadwal yang akan diubah
            item_jadwal = individu[i]
            
            # Pilih atribut yang akan diubah (dosen, waktu, atau ruang)
            atribut_mutasi = random.choice(['dosen', 'waktu', 'ruang'])
            
            if atribut_mutasi == 'dosen':
                item_jadwal['dosen'] = random.choice(PENGAJAR_MATKUL[item_jadwal["matkul"]])
            elif atribut_mutasi == 'waktu':
                waktu_baru = random.choice(LIST_WAKTU)
                item_jadwal['waktu'] = waktu_baru
                item_jadwal['sesi'] = WAKTU_SLOT[waktu_baru]
            elif atribut_mutasi == 'ruang':
                item_jadwal['ruang'] = random.choice(RUANGAN)
    return individu

def tampilkan_jadwal(individu):
    """Menampilkan jadwal dalam format yang mudah dibaca."""
    df = pd.DataFrame(individu)
    df['hari'] = df['waktu'].apply(lambda x: x[0])
    df['jam'] = df['waktu'].apply(lambda x: x[1])
    
    # Urutkan berdasarkan hari dan jam
    hari_order = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"]
    df['hari'] = pd.Categorical(df['hari'], categories=hari_order, ordered=True)
    df = df.sort_values(by=['hari', 'jam'])
    
    # Hapus kolom bantu
    df = df.drop(columns=['waktu', 'matkul', 'sks'])
    
    print(df[['hari', 'jam', 'kelas', 'dosen', 'ruang', 'sesi']].to_string(index=False))

# --- MAIN LOOP ALGORITMA GENETIKA ---

def main():
    print("Membuat populasi awal...")
    populasi = [{'individu': buat_individu(), 'fitness': 0} for _ in range(UKURAN_POPULASI)]

    for gen in range(JUMLAH_GENERASI):
        # Hitung fitness untuk setiap individu
        for i in range(UKURAN_POPULASI):
            populasi[i]['fitness'] = hitung_fitness(populasi[i]['individu'])
            
        # Urutkan populasi berdasarkan fitness
        populasi.sort(key=lambda x: x['fitness'], reverse=True)
        
        # Cek apakah solusi optimal ditemukan (fitness = 1.0)
        if populasi[0]['fitness'] == 1.0:
            print(f"\nSolusi Optimal Ditemukan pada Generasi {gen+1}!")
            break
            
        if (gen + 1) % 50 == 0:
            print(f"Generasi {gen+1:03d} | Fitness Terbaik: {populasi[0]['fitness']:.4f} | Penalti: {int(1/populasi[0]['fitness'] - 1)}")

        # Buat populasi baru
        populasi_baru = []
        
        # Elitisme: Bawa individu terbaik ke generasi berikutnya
        for i in range(JUMLAH_ELITE):
            populasi_baru.append(populasi[i]['individu'])

        # Crossover dan Mutasi
        while len(populasi_baru) < UKURAN_POPULASI:
            parent1 = seleksi_turnamen(populasi)
            parent2 = seleksi_turnamen(populasi)
            child = crossover(parent1, parent2)
            child_mutasi = mutasi(child)
            populasi_baru.append(child_mutasi)
            
        # Ganti populasi lama dengan populasi baru
        populasi = [{'individu': ind, 'fitness': 0} for ind in populasi_baru]

    # Ambil solusi terbaik dari generasi terakhir
    for i in range(UKURAN_POPULASI):
        populasi[i]['fitness'] = hitung_fitness(populasi[i]['individu'])
    populasi.sort(key=lambda x: x['fitness'], reverse=True)
    
    jadwal_terbaik = populasi[0]['individu']
    fitness_terbaik = populasi[0]['fitness']
    penalti_terbaik = int(1/fitness_terbaik - 1)
    
    print("\n" + "="*50)
    print("JADWAL TERBAIK YANG DITEMUKAN")
    print("="*50)
    print(f"Total Penalti: {penalti_terbaik}")
    print(f"Fitness Score: {fitness_terbaik:.4f}")
    print("-"*50)
    tampilkan_jadwal(jadwal_terbaik)

if __name__ == '__main__':
    main()