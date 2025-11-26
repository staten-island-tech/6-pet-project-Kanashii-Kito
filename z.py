import random

# pet class
class pet:
    def __init__(self, name, happiness=100, hunger=100, hygiene=100, energy=100):
        self.name = name
        self.happiness = happiness
        self.hunger = hunger
        self.hygiene = hygiene
        self.energy = energy
        self.age_days = 0

    def show_stats(self):
        print(f"---{self.name}'s stats---")
        print(f"age:       {self.age_days} days")
        print(f"happiness: {self.happiness}")
        print(f"hunger:    {self.hunger}")
        print(f"hygiene:   {self.hygiene}")
        print(f"energy:    {self.energy}")
        print("---------------------------")

    def is_alive(self):
        return (
            self.happiness > 0
            and self.hunger > 0
            and self.hygiene > 0
            and self.energy > 0
        )

# hooman class
class hooman:
    def __init__(self, name, hunger=100, work=100, energy=100, money=100):
        self.name = name
        self.hunger = hunger
        self.work = work
        self.energy = energy
        self.money = money
        self.work_counter = 0
        self.sleep_counter = 0

    def work_action(self):
        self.work += 20
        self.money += 25
        self.energy -= 15
        self.work_counter += 1
        print("You worked. +$25, -15 energy.")

    def sleep(self):
        self.energy += 25
        self.money -= 5
        self.sleep_counter += 1
        print("You slept (+25 energy). Cost: $5. the day has now passed.")

# check death
def check_death(player, cat):
    if player.hunger <= 0 or player.energy <= 0 or player.money <= 0:
        print("you have died due to neglecting yourself aka you being stupid and dumb.")
        cat.show_stats()
        print(f"the cat survived up to {cat.age_days} days.")
        return True
    if not cat.is_alive():
        print(f"your cat {cat.name} has died due to you being stupid... game over.")
        cat.show_stats()
        print(f"{cat.name} survived up to {cat.age_days} days.")
        return True
    return False

# game loop
def game():
    print("welcome to serving cats.")
    print("each day you have 17 moves. sleeping will skip the rest of the day immediately.")

    player_name = input("enter your name: ")
    cat_name = input("enter your cat's name: ")

    player = hooman(player_name)
    cat = pet(cat_name)

    feed_cost = 10
    toy_small_cost = 15
    toy_large_cost = 30
    treat_cost = 20
    play_cost = 5

    moves_left = 17
    last_action = None

    while True:
        # check deaths
        if check_death(player, cat):
            break

        # overwork penalties
        if player.work_counter > 7:
            cat.happiness -= 5
            cat.energy -= 5
            print(f"{cat.name} is neglected because you overworked. (-5 happiness & energy)")

        if player.sleep_counter > 6:
            cat.hunger -= 5
            cat.hygiene -= 5
            print(f"{cat.name} is neglected because you overslept. (-5 hunger & hygiene)")

        print(f"--- menu (moves left: {moves_left}) ---")
        print("1. show cat stats (free)")
        print("2. show your stats (free)")
        print(f"3. feed cat (${feed_cost})")
        print(f"4. small toy play (${toy_small_cost})")
        print(f"5. large toy play (${toy_large_cost})")
        print(f"6. give treat (${treat_cost})")
        print(f"7. play with cat (${play_cost})")
        print("8. work (+$25, -15 energy)")
        print("9. sleep (skip rest of day, +25 energy, -$5)")
        print("10. quit")
        print("11. i hate cats option")

        choice = input("choose option: ")
        last_action = choice
        valid_move = True

        if choice == "1":
            cat.show_stats()

        elif choice == "2":
            print(f"--- {player.name}'s stats ---")
            print(f"hunger: {player.hunger}")
            print(f"work:   {player.work}")
            print(f"energy: {player.energy}")
            print(f"money:  {player.money}")
            print("---------------------------")

        elif choice == "3":
            if player.money >= feed_cost:
                player.money -= feed_cost
                cat.hunger += 25
                print("you fed the cat. +25 hunger.")
            else:
                print("you are too broke to feed the cat.")
                valid_move = False

        elif choice == "4":
            if player.money >= toy_small_cost:
                player.money -= toy_small_cost
                cat.happiness += 15
                print("you gave a small toy. +15 happiness.")
            else:
                print("can't afford the small toy.")
                valid_move = False

        elif choice == "5":
            if player.money >= toy_large_cost:
                player.money -= toy_large_cost
                cat.happiness += 30
                print("you gave a large toy. +30 happiness.")
            else:
                print("can't afford the large toy.")
                valid_move = False

        elif choice == "6":
            if player.money >= treat_cost:
                player.money -= treat_cost
                cat.happiness += 25
                cat.hygiene += 5
                print("you gave a treat. +25 happiness, +5 hygiene.")
            else:
                print("can't afford the treat.")
                valid_move = False

        elif choice == "7":
            if player.money >= play_cost:
                player.money -= play_cost
                cat.happiness += 10
                print("you played with the cat. +10 happiness.")
            else:
                print("you can't even afford to play with the cat.")
                valid_move = False

        elif choice == "8":
            player.work_action()

        elif choice == "9":
            player.sleep()
            moves_left = 0
            continue

        elif choice == "10":
            confirm = input("quit? (yes/no): ").lower()
            if confirm in ("yes", "y"):
                print("thanks for playing.")
                break
            valid_move = False

        elif choice == "11":
            confirm = input("are you sure you want to kill the cat? (yes/no): ").lower()
            if confirm in ("yes", "y"):
                print("the cats revolt. you are vaporized.")
                break
            else:
                print("you hesitated. the cats do not forgive. you are vaporized.")
                break

        else:
            print("invalid choice.")
            valid_move = False

        if valid_move:
            moves_left -= 1

        # day logic
        if moves_left == 0:
            cat.age_days += 1
            print(f"a day has passed. your cat is now {cat.age_days} days old.")

            if last_action != "9":
                player.hunger -= 5
                player.energy -= 5
                print("you did not sleep at the end of the day. -5 hunger and -5 energy.")

            moves_left = 17
            print("a new day begins.")

game()

















# examples from internet so make stuff in term to look better
""" 
print("First line")
print('\n')
print("Second line") 
"""