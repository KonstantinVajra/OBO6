import time
import random


def slow_print(text, delay=1.5):
    """Медленно выводит текст с паузой для погружения."""
    print(text)
    time.sleep(delay)


def choose_character():
    """Позволяет игроку выбрать персонажа."""
    slow_print("Добро пожаловать в мир Элдора! Вы – один из немногих воинов, кто решился бросить вызов тьме.")
    slow_print("Выберите своего персонажа:")
    slow_print("1. Воин (Здоровье: 60, Урон: 6-14, Зелья: 1)")
    slow_print("2. Разбойник (Здоровье: 45, Урон: 8-16, Зелья: 2)")
    slow_print("3. Маг (Здоровье: 40, Урон: 10-20, Зелья: 3)")

    while True:
        choice = input("Введите номер персонажа (1/2/3): ")
        if choice == "1":
            return {"hp": 60, "damage": (6, 14), "potion": 1}
        elif choice == "2":
            return {"hp": 45, "damage": (8, 16), "potion": 2}
        elif choice == "3":
            return {"hp": 40, "damage": (10, 20), "potion": 3}
        else:
            slow_print("Некорректный выбор, попробуйте снова.")


def player_attack(enemy, player_damage):
    input("\nНажмите Enter, чтобы атаковать...\n")
    damage = random.randint(player_damage[0], player_damage[1])
    enemy["hp"] -= damage
    slow_print(f"Вы нанесли {damage} урона! У противника осталось {max(enemy['hp'], 0)} HP.")


def enemy_attack(player, enemy_damage):
    damage = random.randint(enemy_damage[0], enemy_damage[1])
    player["hp"] -= damage
    slow_print(f"Противник атакует! Вы получаете {damage} урона. У вас осталось {max(player['hp'], 0)} HP.")


def battle():
    player = choose_character()
    enemy = {"hp": 40, "damage": (3, 12)}

    slow_print("Вы вступаете в бой! Ваш противник опасен.")

    while player["hp"] > 0 and enemy["hp"] > 0:
        action = input("\nВыберите действие: (1) Атаковать (2) Использовать зелье\n")

        if action == "1":
            player_attack(enemy, player["damage"])
        elif action == "2" and player["potion"] > 0:
            heal = random.randint(10, 20)
            player["hp"] += heal
            player["potion"] -= 1
            slow_print(f"Вы выпили зелье и восстановили {heal} HP! Осталось зелий: {player['potion']}")
        else:
            slow_print("Некорректный ввод или у вас нет зелий!")
            continue

        if enemy["hp"] <= 0:
            slow_print("Вы победили! Противник повержен.")
            break

        enemy_attack(player, enemy["damage"])
        if player["hp"] <= 0:
            slow_print("Вы проиграли... Ваше приключение окончено.")
            break


if __name__ == "__main__":
    battle()
