import os
from characters import Hero, Enemy
from weapon import iron_sword, short_bow, knife

hero = Hero(name="Hero", health=185)
hero.equip(short_bow)
enemy = Enemy(name="Enemy", health=175, weapon=knife)

while True:
    os.system("cls")

    hero.attack(enemy)
    enemy.attack(hero)

    hero.health_bar.draw()
    enemy.health_bar.draw()

    if hero.health <= 0 or enemy.health <= 0:
        if hero.health <= 0:
            print(f"Battle lost! No eternal fame!")
        elif enemy.health <= 0:
            print(f"Hero has won the battle. Legendary!")
        break

    hero.drop()
    input("Battle...")
