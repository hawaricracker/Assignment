print("Masukkan jumlah siswa: ", end="")
n = int(input())
kamus = {}

for i in range(n):
    print(f'Masukkan nama siswa ke-{i+1}: ', end="")
    s = input()
    print(f'Masukkan nilai untuk {s}: ', end="")
    x = int(input())
    kamus[s] = x

print(f'Dictionary = {kamus}')