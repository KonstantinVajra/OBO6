import random

class Hero:
    def __init__(self, name, race):
        self.name = name
        self.health = 100
        self.attack_power = 20
        self.race = race
        self.special_ability = self.set_special_ability()

    def set_special_ability(self):
        abilities = {
            'elf': 'dodge',
            'orc': 'extra_strength',
            'human': 'heal'
        }
        return abilities.get(self.race, None)

    def attack(self, other):
        damage = self.attack_power
        if self.race == 'orc' and random.random() < 0.3:
            print(f"{self.name} использует свою способность 'extra_strength' для удара!")
            damage *= 1.5
        other.health -= damage
        print(f"{self.name} атакует {other.name}, нанося {damage} урона.")

    def is_alive(self):
        return self.health > 0

    def display_status(self):
        print(f"{self.name} ({self.race}) - Здоровье: {self.health}")

class Game:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        print("Добро пожаловать в Тёмный лес Элвинор!")
        print("Место, окутанное магией и древними тайнами...")
        turn = 0
        while self.player.is_alive() and self.computer.is_alive():
            if turn % 2 == 0:
                self.take_turn(self.player, self.computer)
            else:
                self.take_turn(self.computer, self.player)
            turn += 1
        self.declare_winner()

    def take_turn(self, current_hero, other_hero):
        current_hero.attack(other_hero)
        other_hero.display_status()
        if not other_hero.is_alive():
            return
        print()

    def declare_winner(self):
        winner = self.player if self.player.is_alive() else self.computer
        print(f"Игра окончена! Победил {winner.name}!")

# Инициализация игры
player_name = input("Введите имя вашего героя: ")
player_race = input("Выберите расу вашего героя (elf, orc, human): ")
player_hero = Hero(player_name, player_race)

computer_hero = Hero("Гоблин", random.choice(["elf", "orc", "human"]))

game = Game(player_hero, computer_hero)
game.start()
