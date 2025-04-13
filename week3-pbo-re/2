
class Tugas:
    def __init__(self):
        self.daftar = []

    def TambahTugas(self, tugas):
        self.daftar.append(tugas)
        print("Tugas berhasil ditambahkan!")

    def HapusTugas(self, no):
        try:
            self.daftar.remove(self.daftar[no-1])
        except ValueError:
            print(f"Error: Tugas dengan nomor {no} tidak ditemukan.")
        except IndexError:
            print(f"Error: Tugas dengan nomor {no} tidak ditemukan.")
    
    def TampilkanTugas(self):
        print("Daftar Tugas")
        for i in self.daftar:
            print(f"- {i}")

daftar_tugas = Tugas()

while True:
    choice = input("Pilih aksi:\n"
    "1. Tambah tugas\n"
    "2. Hapus tugas\n"
    "3. Tampilkan daftar tugas\n"
    "4. Keluar\n"
    "Masukkan pilihan (1/2/3/4): ")

    try:
        choice = int(choice)
    except ValueError as e:
        if(choice in str(e) and choice != ''):
            print('Input Harus Angka!!!')
        else:
            print('Input Tidak Boleh Kosong!!!')

    if choice == 4:
        break
    elif choice == 1:
        tugas = input("Masukkan tugas yang ingin ditambahkan: ")
        daftar_tugas.TambahTugas(tugas)
    elif choice == 2:
        no = int(input("Masukkan nomor tugas yang ingin dihapus: "))
        daftar_tugas.HapusTugas(no)
    else:
        daftar_tugas.TampilkanTugas()
