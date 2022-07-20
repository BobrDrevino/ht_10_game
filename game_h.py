import random


class Unit:
    def __init__(self, name, health=100, power=1, agility=1, intellect=1):
        self.name = name
        self.health = health
        self.power = power
        self.agility = agility
        self.intellect = intellect

    def __str__(self):
        return f'{self.name}, {self.health}, {self.power}, {self.agility}, {self.intellect}'

    def healing(self):
        health20percent = int(self.health * 0.2)
        if self.health < 100:
            self.health += random.choice(range(1, health20percent))

    def damage(self):
        health20percent = int(self.health * 0.2)
        if self.health > 0:
            self.health -= random.choice(range(1, health20percent))


class Mage(Unit):
    def __init__(self, name, health=100, power=1, agility=1, intellect=1):
        super().__init__(name=name, health=health, power=power, agility=agility, intellect=intellect)
        self.mage_type = random.choice(['fire', 'air', 'water'])

    def __str__(self):
        str1 = super().__str__()
        return f'{str1}, {self.mage_type}'

    def get_level_up(self):
        self.intellect += 1 if self.intellect < 10 else 0


class Archer(Unit):
    def __init__(self, name, health=100, power=1, agility=1, intellect=1):
        super().__init__(name=name, health=health, power=power, agility=agility, intellect=intellect)
        self.bow_type = random.choice(['bow', 'crossbow', 'sling'])

    def __str__(self):
        str1 = super().__str__()
        return f'{str1}, {self.bow_type}'

    def get_level_up(self):
        self.agility += 1 if self.agility < 10 else 0


class Knight(Unit):
    def __init__(self, name, health=100, power=1, agility=1, intellect=1):
        super().__init__(name=name, health=health, power=power, agility=agility, intellect=intellect)
        self.weapon_type = random.choice(['sword', 'axe', 'pike'])

    def __str__(self):
        str1 = super().__str__()
        return f'{str1}, {self.weapon_type}'

    def get_level_up(self):
        self.power += 1 if self.power < 10 else 0


mag = Mage(name="Dumbledore")
mag.get_level_up()
mag.get_level_up()
mag.damage()
mag.damage()
print(mag)

archer = Archer(name='Eyeless')
archer.get_level_up()
archer.damage()
print(archer)

knight = Knight(name='Bob')
knight.get_level_up()
knight.damage()
print(knight)

