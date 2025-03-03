import random

class Robot():
    def __init__(self, nama):
        self.hp = 100
        self.nama = nama
    
    def stats(self):
        print(f'Sisa HP {self.nama} = {self.hp}')

    def diserang(self, damage, enemy):
        print(f'{enemy} -> {self.nama} = {damage}')
        self.hp -= damage
        self.stats()

x = Robot('x')
y = Robot('y')

x.stats()
y.stats()

while(x.hp > 0 and y.hp > 0):
    input()
    if y.hp > 0:
        x.diserang(random.randint(1,50), 'y')
    if x.hp > 0:
        y.diserang(random.randint(1,50), 'x')



