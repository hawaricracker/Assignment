import math

angka = input("Masukkan Angka: ")

try:
    try:
        angka = int(angka)
    except ValueError:
        print("Input tidak valid. Harap masukkan angka yang valid.")
        raise TypeError

    if angka < 0:
        raise ValueError("Angka tidak boleh negatif.")
    elif angka == 0:
        raise ValueError("Angka tidak boleh nol.")
    result = math.sqrt(angka)
    print(result)

except ValueError as e:
    print(e)

except TypeError:
    pass
