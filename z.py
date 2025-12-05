import random
# classes
class Pet:
    def __init__(self, name, happiness=100, hunger=100, hygiene=100, energy=100):
        self.name = name
        self.happiness = happiness
        self.hunger = hunger
        self.hygiene = hygiene
        self.energy = energy
        self.age_days = 0

    def show_stats(self):
        print(f"---- {self.name}'s stats ----")
        print(f"Age:       {self.age_days} days")
        print(f"Happiness: {self.happiness}")
        print(f"Hunger:    {self.hunger}")
        print(f"Hygiene:   {self.hygiene}")
        print(f"Energy:    {self.energy}")
        print("------------------------------")

    def is_alive(self):
        return (
            self.happiness > 0
            and self.hunger > 0
            and self.hygiene > 0
            and self.energy > 0
        )

    def statscap(self):
        # keep stats within 0 to 100
        self.happiness = max(0, min(100, self.happiness))
        self.hunger = max(0, min(100, self.hunger))
        self.hygiene = max(0, min(100, self.hygiene))
        self.energy = max(0, min(100, self.energy))

class Hooman:
    def __init__(self, name, hunger=100, work= "Do no work too much or you might die.", energy=100, money=80):
        self.name = name
        self.hunger = hunger
        self.work = work      # unchanged on purpose || do not touch future eric
        self.energy = energy
        self.money = money

    def show_stats(self):
        print(f"---- {self.name}'s stats ----")
        print(f"Hunger: {self.hunger}")
        print(f"Work:   {self.work}")
        print(f"Energy: {self.energy}")
        print(f"Money:  {self.money}")
        print("----------------------------")

    def statscap(self):
        # keep stats within 0 to 100 for the human
        self.hunger = max(0, min(100, self.hunger))
        self.energy = max(0, min(100, self.energy))

    def work_action(self):
        # work increases money at the cost of energy
        self.money += 35
        self.energy -= 10
        print("You worked. +$35, -10 energy.")

    def feed_hooman(self):
        self.hunger += 24
        self.money -= 17

    def nap(self):
        self.energy += 7

    def sleep(self):
        # sleep restores energy but increases hunger
        self.energy += 35
        self.hunger -= 10
        print("You slept: +35 energy, -10 hunger.")
        print("The day ends.")

# random events for the cat
def random_event(cat, human):
    event = random.randint(1, 5)

    if event == 1:
        cat.hygiene -= 10
        print(f"{cat.name} rolled in dust. -10 hygiene.")
    elif event == 2:
        cat.hunger -= 10
        print(f"{cat.name} got extra hungry. -10 hunger.")
    elif event == 3:
        cat.happiness += 10
        print(f"{cat.name} found a toy. +10 happiness.")
    elif event == 4:
        found = random.randint(5, 20)
        human.money += found
        print(f"{cat.name} brought you ${found} it found?")
    elif event == 5:
        cat.energy -= 5
        print(f"{cat.name} zoomies drained energy. -5 energy.")

    cat.statscap()

# check if the player or cat died
def check_death(player, cat):
    if player.hunger <= 0 or player.energy <= 0 or player.money < 0:
        print("You died due to neglecting yourself.")
        return True

    if not cat.is_alive():
        print(f"Your cat {cat.name} has died... and so have you.")
        return True

    return False

# game loop
def game():
    print("Welcome.")
    print("Each day has 17 moves. Sleeping ends the day immediately.")

    player_name = input("Your Name: ")
    cat_name = input("Cat's Name: ")

    player = Hooman(player_name)
    cat = Pet(cat_name)

    # prices for actions
    feed_cost = 5
    toy_small_cost = 8
    toy_large_cost = 15
    treat_cost = 10
    play_cost = 3
    nap_counter = 0

    moves_left = 17

    while True:

        # check death first
        if check_death(player, cat):
            print ("Game Report:")
            cat.show_stats()
            player.show_stats()
            break

        # turn-based stat decay
        player.hunger -= 1
        player.energy -= 1

        cat.hunger -= 1
        cat.energy -= 1
        cat.hygiene -= 1

        # aging makes the cat harder to maintain over time
        if cat.age_days > 5:
            cat.hunger -= 1
        if cat.age_days > 12:
            cat.energy -= 1
        if cat.age_days > 20:
            cat.happiness -= 1

        # stats cap at 100 so nothing breaks
        player.statscap()
        cat.statscap()

        # 15% chance for a random event each turn
        if random.random() < 0.15:
            random_event(cat, player)

        print ("\n")
        print (f"---- Menu (Moves left: {moves_left}) ----")
        print ("1. show cat stats")
        print ("2. show your stats")
        print (f"3. feed cat (${feed_cost})")
        print (f"4. small toy (${toy_small_cost})")
        print (f"5. large toy (${toy_large_cost})")
        print (f"6. treat (${treat_cost})")
        print (f"7. play with cat (${play_cost})")
        print ("8. work (+$35)")
        print ("9. Tiny Nap (+7 energy)")
        print ("10. sleep (end day)")
        print ("11. quit")
        print ("-------------------------------------------")
        print ("\n")

        choice = input("Choose: ")

        valid_move = True

        if choice == "1":
            cat.show_stats()
            valid_move = False

        elif choice == "2":
            player.show_stats()
            valid_move = False

        elif choice == "3":
            if player.money >= feed_cost:
                player.money -= feed_cost
                cat.hunger += 20
                print("You fed the cat. +20 hunger.")
            else:
                print("You can't afford food.")
                valid_move = False

        elif choice == "4":
            if player.money >= toy_small_cost:
                player.money -= toy_small_cost
                cat.happiness += 15
                print("Small toy. +15 happiness.")
            else:
                print("Too expensive.")
                valid_move = False

        elif choice == "5":
            if player.money >= toy_large_cost:
                player.money -= toy_large_cost
                cat.happiness += 25
                print("Large toy. +25 happiness.")
            else:
                print("Too expensive.")
                valid_move = False

        elif choice == "6":
            if player.money >= treat_cost:
                player.money -= treat_cost
                cat.happiness += 10
                cat.hygiene += 5
                print("Treat given.+10 happiness, +5 hygiene.")
            else:
                print("You can't afford it.")
                valid_move = False

        elif choice == "7":
            if player.money >= play_cost:
                player.money -= play_cost
                cat.happiness += 10
                print("You played with the cat. +10 happiness.")
            else:
                print("Too poor to play?")
                valid_move = False

        elif choice == "8":
            player.work_action()

        elif choice == "9":
            player.nap()
            nap_counter+=1
            if nap_counter == 2:
                print ("You overslept and it's the next day.")
                print ("Cat Stats have been changed.")
                print ("Hunger - 20 | Happiness - 14 | Hygiene - 25 | Energy - 9")
                cat.hunger -= 20
                cat.happiness -= 14
                cat.hygiene -= 25
                cat.energy -= 9
                player.hunger -= 40
                player.money -= 10
                player.energy += 1
                moves_left = 1
                nap_counter = 0

        elif choice == "10":
            player.sleep()
            valid_move=False
            moves_left = 0  # end the day

        elif choice == "11":
            print("Thanks for playing")
            break

        else:
            print("Invalid choice.")
            valid_move = False

        if valid_move:
            moves_left -= 1

        # end of day actions
        if moves_left == 0:
            cat.age_days += 1
            print(f"A day has passed. {cat.name} is now {cat.age_days} days old.")

            # secondary stats cap
            player.statscap()
            cat.statscap()

            # daily allowance helps with money balance
            player.money += 5
            print("You received a daily cat-llowance: +$5")


            # check for final 50/50 ending
            if cat.age_days >= 27:
                print(f"{cat.name} has reached old age at {cat.age_days} days.")

                if random.random() < 0.5:
                    print("You've won.")
                else:
                    print(f"{cat.name} becomes the ruler of the household... The cats wins.")
                
                break
            print("A new day begins.")
            moves_left = 17

game()