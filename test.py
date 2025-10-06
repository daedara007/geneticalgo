# Implementasi Genetic Algorithm untuk pencarian jadwal Mahasiwa Informatika Semester Ganjil
import random
import copy
from collections import defaultdict

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
    "Aljabar Linier dan Geometri": {"sks": 3, "semester": 2},
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

WAKTU_SLOT = {
    #Senin
    ("Senin", "07:30"): 1,
    ("Senin", "10:20"): 2,
    ("Senin", "13:00"): 3,
    ("Senin", "16:00"): 4,

    #Selasa
    ("Selasa", "07:30"): 1,
    ("Selasa", "10:20"): 2,
    ("Selasa", "13:00"): 3,
    ("Selasa", "16:00"): 4,

    #Rabu
    ("Rabu", "07:30"): 1,
    ("Rabu", "10:20"): 2,
    ("Rabu", "13:00"): 3,
    ("Rabu", "16:00"): 4,

    #Kamis
    ("Kamis", "07:30"): 1,
    ("Kamis", "10:20"): 2,
    ("Kamis", "13:00"): 3,
    ("Kamis", "16:00"): 4,

    #Jumat
    ("Jumat", "07:30"): 1,
    ("Jumat", "10:20"): 2,
    ("Jumat", "13:00"): 3,
    ("Jumat", "16:00"): 4,
}

RUANGAN = [
    #Gedung G
    'G101', 'G102', 'G103', 'G104', 'G105', 'G106',
    'G201', 'G202', 'G203', 'G204', 'G205', 'G206',
    'G301', 'G302', 'G303', 'G304', 'G305', 'G306',
    #Gedung F
    'F101', 'F102', 'F103', 'F104', 'F105', 'F106',
    'F201', 'F202', 'F203', 'F204', 'F205', 'F206',
    'F301', 'F302', 'F303', 'F304', 'F305', 'F306',
    #Gedung E
    'E101', 'E102', 'E103', 'E104', 'E105', 'E106',
    'E201', 'E202', 'E203', 'E204', 'E205', 'E206',
    'E301', 'E302', 'E303', 'E304', 'E305', 'E306'
]

# Built helpers
SLOT_LIST = list(WAKTU_SLOT.values())  # [1,2,3,4]
SLOT_TO_TIME = {v: k for k, v in WAKTU_SLOT.items()}  # reverse mapping

# sanitize pengajar lists (hapus empty strings)
for k, lst in list(PENGAJAR_MATKUL.items()):
    PENGAJAR_MATKUL[k] = [p.strip() for p in lst if isinstance(p, str) and p.strip()]

# For mata kuliah without pengajar list, allow placeholder 'TBD' or None
def possible_instructors(matkul):
    if matkul in PENGAJAR_MATKUL and PENGAJAR_MATKUL[matkul]:
        return PENGAJAR_MATKUL[matkul]
    # fallback: pick all lecturers from provided dict (less ideal) or 'TBD'
    # we'll return ['TBD'] to avoid giving wrong instructors
    return ['TBD']

# ---------------------------
# GA Implementation
# ---------------------------
random.seed(42)

def random_individual():
    """Buat satu kromosom: dict matkul -> (slot, ruangan, pengajar)"""
    indiv = {}
    for matkul, info in MATA_KULIAH.items():
        slot = random.choice(SLOT_LIST)
        ruang = random.choice(RUANGAN)
        instrs = possible_instructors(matkul)
        pengajar = random.choice(instrs)
        indiv[matkul] = (slot, ruang, pengajar)
    return indiv

def fitness(indiv, penalties=None):
    """
    Hitung fitness sebagai negative total penalty (semakin besar fitness -> lebih baik).
    penalties: dict custom penalty weights (optional).
    """
    if penalties is None:
        penalties = {
            'room_conflict': 100,   # per pair conflict in same room&slot
            'instructor_conflict': 100, # per pair instructor conflict same slot
            'heavy_in_bad_slot': 10, # per course with sks>=3 in slot 2 or 4
        }
    total_penalty = 0

    # 1) room conflicts: for each slot+room count how many matkul, pairs = n*(n-1)/2
    slot_room_map = defaultdict(list)
    for matkul, (slot, ruang, _) in indiv.items():
        slot_room_map[(slot, ruang)].append(matkul)
    for key, lst in slot_room_map.items():
        n = len(lst)
        if n > 1:
            total_penalty += penalties['room_conflict'] * (n * (n - 1) // 2)

    # 2) instructor conflicts: for each instructor and slot, count how many
    instr_slot_map = defaultdict(list)
    for matkul, (slot, _, pengajar) in indiv.items():
        instr_slot_map[(pengajar, slot)].append(matkul)
    for key, lst in instr_slot_map.items():
        n = len(lst)
        if n > 1:
            total_penalty += penalties['instructor_conflict'] * (n * (n - 1) // 2)

    # 3) heavy courses (sks >= 3) in slot 2 or 4
    for matkul, (slot, _, _) in indiv.items():
        sks = MATA_KULIAH[matkul]['sks']
        if sks >= 3 and slot in (2, 4):
            total_penalty += penalties['heavy_in_bad_slot']

    # Return fitness (higher is better)
    return -total_penalty, total_penalty

# GA operators
def tournament_selection(pop, k=3):
    """k-tournament selection (return a copy)"""
    selected = random.sample(pop, k)
    selected.sort(key=lambda x: x['fitness'], reverse=True)  # fitness higher = better
    return copy.deepcopy(selected[0]['indiv'])

def crossover(parent1, parent2, cx_prob=0.5):
    """Uniform-style crossover: for each matkul, swap with prob cx_prob"""
    child1 = {}
    child2 = {}
    for matkul in MATA_KULIAH.keys():
        if random.random() < cx_prob:
            child1[matkul] = copy.deepcopy(parent2[matkul])
            child2[matkul] = copy.deepcopy(parent1[matkul])
        else:
            child1[matkul] = copy.deepcopy(parent1[matkul])
            child2[matkul] = copy.deepcopy(parent2[matkul])
    return child1, child2

def mutate(indiv, mut_prob=0.1):
    """Mutasi: untuk tiap matkul, dengan prob mut_prob ubah slot/ruang/pengajar salah satu"""
    new_indiv = copy.deepcopy(indiv)
    for matkul in MATA_KULIAH.keys():
        if random.random() < mut_prob:
            # choose which attribute to mutate
            attr = random.choice(['slot', 'ruang', 'pengajar'])
            slot, ruang, pengajar = new_indiv[matkul]
            if attr == 'slot':
                new_indiv[matkul] = (random.choice(SLOT_LIST), ruang, pengajar)
            elif attr == 'ruang':
                new_indiv[matkul] = (slot, random.choice(RUANGAN), pengajar)
            else:  # pengajar
                instrs = possible_instructors(matkul)
                new_indiv[matkul] = (slot, ruang, random.choice(instrs))
    return new_indiv

# Main GA runner
def run_ga(pop_size=100, generations=200, cx_prob=0.6, mut_prob=0.08, verbose=True):
    # init population
    population = []
    for _ in range(pop_size):
        indiv = random_individual()
        fit, pen = fitness(indiv)
        population.append({'indiv': indiv, 'fitness': fit, 'penalty': pen})
    # evolve
    best_history = []
    for gen in range(1, generations + 1):
        new_pop = []
        # elitism: keep best 2
        population.sort(key=lambda x: x['fitness'], reverse=True)
        elites = population[:2]
        new_pop.extend(copy.deepcopy(elites))

        while len(new_pop) < pop_size:
            p1 = tournament_selection(population, k=3)
            p2 = tournament_selection(population, k=3)
            c1, c2 = crossover(p1, p2, cx_prob=cx_prob)
            c1 = mutate(c1, mut_prob)
            c2 = mutate(c2, mut_prob)
            f1, p1_pen = fitness(c1)
            f2, p2_pen = fitness(c2)
            new_pop.append({'indiv': c1, 'fitness': f1, 'penalty': p1_pen})
            if len(new_pop) < pop_size:
                new_pop.append({'indiv': c2, 'fitness': f2, 'penalty': p2_pen})

        population = new_pop

        # keep track best
        population.sort(key=lambda x: x['fitness'], reverse=True)
        best = population[0]
        best_history.append((gen, best['fitness'], best['penalty']))
        if verbose and (gen % max(1, generations//10) == 0 or gen==1 or gen==generations):
            print(f"Gen {gen:4d} | Best fitness: {best['fitness']} | Penalty: {best['penalty']}")

    # final best
    population.sort(key=lambda x: x['fitness'], reverse=True)
    best = population[0]
    return best, best_history

# Pretty print schedule
def print_schedule(indiv):
    rows = []
    for matkul, (slot, ruang, pengajar) in indiv.items():
        daytime = SLOT_TO_TIME.get(slot, ("", ""))
        rows.append((slot, matkul, MATA_KULIAH[matkul]['sks'], dayTime_str(daytime), ruang, pengajar))
    # sort by slot
    rows.sort(key=lambda x: (x[0], x[1]))
    print(f"{'Slot':<4} | {'Mata Kuliah':<30} | {'SKS':<3} | {'Hari/Jam':<12} | {'Ruang':<5} | {'Dosen'}")
    print("-" * 90)
    for r in rows:
        print(f"{r[0]:<4} | {r[1]:<30} | {r[2]:<3} | {r[3]:<12} | {r[4]:<5} | {r[5]}")

def dayTime_str(daytime):
    if not daytime:
        return ""
    day, t = daytime
    return f"{day} {t}"

# ---------------------------
# Run example
# ---------------------------
if __name__ == "__main__":
    best, history = run_ga(pop_size=150, generations=300, cx_prob=0.6, mut_prob=0.08, verbose=True)
    print("\n=== Jadwal Terbaik Ditemukan ===")
    print(f"Fitness: {best['fitness']}  | Total penalty: {best['penalty']}")
    print_schedule(best['indiv']) 