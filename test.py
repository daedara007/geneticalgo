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

# Prepare data
mata_kuliah = list(MATA_KULIAH.keys())
sks_dict = {mk: MATA_KULIAH[mk]['sks'] for mk in mata_kuliah}
slots = list(set(WAKTU_SLOT.values()))  # [1,2,3,4]
ruangs = RUANGAN

# Dosen options, filter empty and add dummy for missing matkul
dosen_options = {}
for mk in mata_kuliah:
    dosens = [d for d in PENGAJAR_MATKUL.get(mk, []) if d.strip()]
    if not dosens:
        dosens = [f"Dosen Dummy for {mk}"]  # Dummy if missing
    dosen_options[mk] = dosens

# Genetic Algorithm Parameters
POPULATION_SIZE = 100
GENERATIONS = 200
MUTATION_RATE = 0.1
CROSSOVER_RATE = 0.7
TOURNAMENT_SIZE = 5

# Individual representation: dict {matkul: (slot, ruang, dosen)}
def create_individual():
    individual = {}
    for mk in mata_kuliah:
        slot = random.choice(slots)
        ruang = random.choice(ruangs)
        dosen = random.choice(dosen_options[mk])
        individual[mk] = (slot, ruang, dosen)
    return individual

# Fitness function: negative penalty (higher is better)
def fitness(individual):
    penalty = 0
    
    # Room clashes: same slot and same ruang
    slot_room_usage = {}
    for mk, (slot, ruang, dosen) in individual.items():
        key = (slot, ruang)
        if key in slot_room_usage:
            penalty += 10  # Penalty for room clash
        else:
            slot_room_usage[key] = mk
    
    # Dosen clashes: same slot and same dosen
    slot_dosen_usage = {}
    for mk, (slot, ruang, dosen) in individual.items():
        key = (slot, dosen)
        if key in slot_dosen_usage:
            penalty += 10  # Penalty for dosen clash
        else:
            slot_dosen_usage[key] = mk
    
    # Penalty for matkul >=3 SKS in slot 2 or 4
    for mk, (slot, ruang, dosen) in individual.items():
        if sks_dict[mk] >= 3 and slot in [2, 4]:
            penalty += 5  # Penalty for unsuitable slot
    
    return -penalty

# Selection: Tournament selection
def tournament_selection(population):
    selected = []
    for _ in range(len(population)):
        candidates = random.sample(population, TOURNAMENT_SIZE)
        best = max(candidates, key=fitness)
        selected.append(copy.deepcopy(best))
    return selected

# Crossover: Single point crossover on matkul assignments
def crossover(parent1, parent2):
    if random.random() > CROSSOVER_RATE:
        return copy.deepcopy(parent1), copy.deepcopy(parent2)
    
    child1 = copy.deepcopy(parent1)
    child2 = copy.deepcopy(parent2)
    
    # Choose a crossover point
    crossover_point = random.randint(1, len(mata_kuliah) - 1)
    mk_list = list(mata_kuliah)
    
    for i in range(crossover_point, len(mk_list)):
        mk = mk_list[i]
        child1[mk], child2[mk] = child2[mk], child1[mk]
    
    return child1, child2

# Mutation: Randomly change slot, ruang, or dosen for a matkul
def mutate(individual):
    for mk in mata_kuliah:
        if random.random() < MUTATION_RATE:
            # Randomly mutate one part
            mutation_type = random.choice(['slot', 'ruang', 'dosen'])
            if mutation_type == 'slot':
                new_slot = random.choice(slots)
                slot, ruang, dosen = individual[mk]
                individual[mk] = (new_slot, ruang, dosen)
            elif mutation_type == 'ruang':
                new_ruang = random.choice(ruangs)
                slot, ruang, dosen = individual[mk]
                individual[mk] = (slot, new_ruang, dosen)
            elif mutation_type == 'dosen':
                new_dosen = random.choice(dosen_options[mk])
                slot, ruang, dosen = individual[mk]
                individual[mk] = (slot, ruang, new_dosen)
    return individual

# Main GA loop
def genetic_algorithm():
    # Initialize population
    population = [create_individual() for _ in range(POPULATION_SIZE)]
    
    for generation in range(GENERATIONS):
        # Selection
        selected = tournament_selection(population)
        
        # New population
        new_population = []
        for i in range(0, len(selected), 2):
            parent1 = selected[i]
            parent2 = selected[i+1] if i+1 < len(selected) else selected[0]
            child1, child2 = crossover(parent1, parent2)
            new_population.append(mutate(child1))
            new_population.append(mutate(child2))
        
        population = new_population[:POPULATION_SIZE]
        
        # Print best fitness every 50 generations
        if generation % 50 == 0:
            best = max(population, key=fitness)
            print(f"Generation {generation}: Best Fitness = {fitness(best)}")
    
    # Return best individual
    best_individual = max(population, key=fitness)
    return best_individual

# Run the GA
best_schedule = genetic_algorithm()

# Print the best schedule
print("\nBest Schedule:")
for mk, (slot, ruang, dosen) in best_schedule.items():
    print(f"{mk}: Slot {slot}, Ruang {ruang}, Dosen {dosen}")

print(f"Fitness: {fitness(best_schedule)}")