class Animal:
    def __init__(self, name, age):
        try:
            if not name:
                raise ValueError("Nama hewan tidak boleh kosong.")
            age = int(age)
            if age <= 0:
                raise ValueError("Usia hewan harus lebih dari 0.")
        except ValueError as e:
            print(e)
        except:
            print("Umur Harus Angka!!!")
        
        self.__name = name
        self.__age = age

    def make_sound(self):
        pass 

    def get_info(self):
        return f"Nama: {self.__name}, Usia: {self.__age} tahun"
    
    def change_age(self, age):
        self.__age = age
    
class Dog(Animal):
    def make_sound(self):
        print("Woof Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

x = input("Pilihan:\n"
"1. Anjing\n"
"2. Kucing\n"
"Pilih hewan yang akan diinput : ")

try:
    x = int(x)
except:
    print("Input Tidak Valid!!!")

nama = input("Masukkan Nama : ")
umur = input("Masukkan Umur : ")

if(x == 1):
    p = Dog(nama, umur)
else:
    p = Cat(nama, umur)
