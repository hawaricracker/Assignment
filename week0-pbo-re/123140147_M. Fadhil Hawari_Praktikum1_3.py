print("Masukkan nama : ", end="")
n = input()
print("Masukkan NIM : ", end="")
nim = input()
print("Masukkan resolusi di tahun ini : ", end="")
res = input()

with open('./week0-pbo-re/Me.txt', 'w') as f:
    f.write(f'Nama : {n}\nNIM : {nim}\nResolusi di tahun ini : {res}\n')