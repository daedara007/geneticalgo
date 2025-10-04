# Implementasi Genetic Algorithm untuk pencarian jadwal Mahasiwa Informatika Semester Ganjil
import random
import copy

MATA_KULIAH = {
    # Semester 1
    "Algoritma dan Pemrograman": {"sks": 3, "semester": 1},
    "Bahasa Inggris": {"sks": 2, "semester": 1},
    "Fisika 1": {"sks": 3, "semester": 1},
    "Matematika 1": {"sks": 3, "semester": 1},
    "Matematika Diskrit": {"sks": 3, "semester": 1},
    "Pengantar Informatika": {"sks": 2, "semester": 1},
    "Sistem Digital": {"sks": 3, "semester": 1},

    # Semester 3
    "Agama Islam": {"sks": 2, "semester": 3},
    "Agama Kristen": {"sks": 2, "semester": 3},
    "Agama Katolik": {"sks": 2, "semester": 3},
    "Agama Buddha": {"sks": 2, "semester": 3},
    "Aljabar Liner dan Geometri": {"sks": 3, "semester": 2},
    "Arsitektur Komputer": {"sks": 3, "semester": 3},
    "Pancasila": {"sks": 2, "semester": 3},
    "Pengantar Kecerdasan Artifisial": {"sks": 3, "semester": 3},
    "Sistem Operasi": {"sks": 3, "semester": 3},
    "Struktur Data": {"sks": 4, "semester": 3},

    # Semester 5
    "Desain Web": {"sks": 3, "semester": 5},
    "Implementasi dan Pengujian Perangkat Lunak": {"sks": 3, "semester": 5},
    "Interaksi Manusia dan Komputer": {"sks": 3, "semester": 5},
    "Manajemen Basis Data": {"sks": 3, "semester": 5},
    "Pemrograman Fungsional": {"sks": 3, "semester": 5},
    "Pengolahan Citra Digital": {"sks": 3, "semester": 5},
    
    # Semester 6
    "Deep Learning": {"sks": 3, "semester": 6},
    "Sistem Paralel dan Terdistribusi": {"sks": 3, "semester": 6},

    # Semester 7
    "Capstone Project": {"sks": 4, "semester": 7},
    "Kapita Selekta": {"sks": 2, "semester": 7},
    "Keamanan Siber": {"sks": 3, "semester": 7},
    "Kecerdasan Web": {"sks": 3, "semester": 7},
    "Keprofesian Informatika": {"sks": 2, "semester": 7},
    "Komputasi Evolusioner": {"sks": 3, "semester": 7},
    "Manajemen Proyek TIK": {"sks": 3, "semester": 7},
    "Pemrosesan Bahasa Alami": {"sks": 3, "semester": 7},
    "Pengembangan Aplikasi Perangkat Bergerak": {"sks": 3, "semester": 7},
    "Sains Data": {"sks": 3, "semester": 7},
    "Visi Komputer": {"sks": 3, "semester": 7},
}

PENGAJAR_MATKUL = {
    "Agama Islam": ["Suriansyah S.Pd,M.Pd.", "Muhammad Gufron S.Pd, M.Pd"],
    "Agama Kristen": ["Silas Ratu M.Pd.K."],
    "Agama Katolik": ["Andreas Joni Pasundan S.S,Bth"],
    "Agama Buddha": ["Maryono S.Si, M.Si."],
    "Algoritma dan Pemrograman": ["Rizal Kusuma Putra, M.T.", "Gusti Ahmad Fanshuri Alfarisy, S.Kom., M.Kom.", ""],
    "Bahasa Inggris": ["Yustina Fitriani, S.Pd, M.Pd.", "Alif Suci Dirgantari S.Pd, M.Pd"],
    "Fisika 1": ["Febrian Dedi Sastrawan S.si, M.Sc.", "Fadli Robiandi S.Si, M.Si"],
    "Matematika 1": ["Winarni, S.Si, M.Si:", "Retno Wahyu Dewanti S.Si, M.Si"],
    "Pancasila": ["Akbar Taufik Amrullah S.H., M.Kn.", "Farida Nur Hidayah, S.H, M.H."],
    "Aljabar Linier dan Geometri": ["Ramadhan Paninggalih S.Si., M.Si., M.Sc."],
    "Arsitektur Komputer": ["Aninditya Anggari Nuryono, S.T., M.Eng.", "Riska Kurniyanto Abdullah, S.T., M.Kom."],
    "Capstone Project": ["Ramadhan Paninggalih S.Si., M.Si., M.Sc."],
    "Deep Learning": ["Boby Mogi Pratama, S.Si., M.Han."],
    "Desain Web": ["Rizal Kusuma Putra, M.T."],
    "Implementasi dan Pengujian Perangkat Lunak": ["Nur Fajri Azhar S.Kom., M.Kom."],
    "Interaksi Manusia dan Komputer": ["Nisa Rizqiya Fadhliana, S.Kom., M.T."],
    "Kapita Selekta": ["Nisa Rizqiya Fadhliana, S.Kom., M.T."],
    "Keamanan Siber": ["Darmansyah, S.Si., M.T.I"],
    "Kecerdasan Web": ["Gusti Ahmad Fanshuri Alfarisy, S.Kom., M.Kom."],
    "Keprofesian Informatika": ["Nur Fajri Azhar S.Kom., M.Kom.", "Darmansyah, S.Si., M.T.I"],
    "Kerja Praktek": ["Nisa Rizqiya Fadhliana, S.Kom., M.T."],
    "Komputasi Evolusioner": ["Muchammad Chandra Cahyo Utomo, S. Kom., M. Kom."],
    "Manajemen Basis Data": ["Bowo Nugroho, S.Kom., M.Eng."],
    "Manajemen Proyek TIK": ["Riska Kurniyanto Abdullah, S.T., M.Kom."],
    "Matematika Diskrit": ["Ramadhan Paninggalih S.Si., M.Si., M.Sc."],
    "Pemrograman Fungsional": ["Gusti Ahmad Fanshuri Alfarisy, S.Kom., M.Kom."],
    "Pemrosesan Bahasa Alami": ["Bima Prihasto, S.SI., M.Si., Ph.D."],
    "Pengantar Informatika": ["Muchammad Chandra Cahyo Utomo, S. Kom., M. Kom."],
    "Pengantar Kecerdasan Artifisial": ["Bima Prihasto, S.SI., M.Si., Ph.D.", "Gusti Ahmad Fanshuri Alfarisy, S.Kom., M.Kom."],
    "Pengembangan Aplikasi Perangkat Bergerak": ["Rizal Kusuma Putra, M.T."],
    "Pengolahan Citra Digital": ["Rizky Amelia, S.Si., M.Han."],
    "Proposal Tugas Akhir": ["Nisa Rizqiya Fadhliana, S.Kom., M.T."],
    "Sains Data": ["Ramadhan Paninggalih S.Si., M.Si., M.Sc."],
    "Sistem Digital": ["Boby Mugi Pratama, S.Si., M.Han."],
    "Sistem Operasi": ["Darmansyah, S.SI., M.T.I"],
    "Sistem Paralel dan Terdistribusi": ["Riska Kurniyanto Abdullah, S.T., M.Kom."],
    "Struktur Data": ["Muchammad Chandra Cahyo Utomo, S. Kom., M. Kom.", "Bowo Nugroho, S.Kom., M.Eng."],
    "Tugas Akhir": ["Nisa Rizqiya Fadhliana, S.Kom., M.T."],
    "Visi Komputer": ["Rizky Amelia, S.Si., M.Han."]
}



print(MATA_KULIAH)
print(PENGAJAR_MATKUL)