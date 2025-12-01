# import random

# # pet class
# class pet:
#     def __init__(self, name, happiness=100, hunger=100, hygiene=100, energy=100):
#         self.name = name
#         self.happiness = happiness
#         self.hunger = hunger
#         self.hygiene = hygiene
#         self.energy = energy
#         self.age_days = 0

#     def show_stats(self):
#         print(f"---{self.name}'s stats---")
#         print(f"age:       {self.age_days} days")
#         print(f"happiness: {self.happiness}")
#         print(f"hunger:    {self.hunger}")
#         print(f"hygiene:   {self.hygiene}")
#         print(f"energy:    {self.energy}")
#         print("---------------------------")

#     def is_alive(self):
#         return (
#             self.happiness > 0
#             and self.hunger > 0
#             and self.hygiene > 0
#             and self.energy > 0
#         )

# # hooman class
# class hooman:
#     def __init__(self, name, hunger=100, work=100, energy=100, money=50):
#         self.name = name
#         self.hunger = hunger
#         self.work = work
#         self.energy = energy
#         self.money = money
#         self.work_counter = 0
#         self.sleep_counter = 0

#     def work_action(self):
#         self.work += 20
#         self.money += 25
#         self.energy -= 15
#         self.work_counter += 1
#         print ("You worked. +$25, -15 energy.")

#     def sleep(self):
#         self.energy += 25
#         self.money -= 5
#         self.sleep_counter += 1
#         print ("You slept (+25 energy). Cost: $5. The day has now passed.")
#         print ("Sleeping costs money because yes")

# # death
# def check_death(player, cat):
#     if player.hunger <= 0 or player.energy <= 0 or player.money <= 0:
#         print("you have died due to neglecting yourself aka you being stupid and dumb.")
#         cat.show_stats()
#         print(f"the cat survived up to {cat.age_days} days.")
#         return True
#     if not cat.is_alive():
#         print(f"your cat {cat.name} has died due to you being stupid....")
#         print("You've also died.")
#         cat.show_stats()
#         print(f"{cat.name} survived up to {cat.age_days} days.")
#         return True
#     return False

# # game loop
# def game():
#     print ("Welcome to serving cats.")
#     print ("Each day you have 17 moves. Sleeping will skip the rest of the day immediately.")
#     print ("Remember to sleep as your last move or you will lose some stats.")

#     player_name = input("Your Name: ")
#     cat_name = input("Enter Your Cat's Name: ")

#     player = hooman(player_name)
#     cat = pet(cat_name)

#     feed_cost = 10
#     toy_small_cost = 15
#     toy_large_cost = 30
#     treat_cost = 20
#     play_cost = 5

#     moves_left = 17
#     last_action = None

#     while True:
#         # check deaths
#         if check_death(player, cat):
#             break

#         # overwork idiots
#         if player.work_counter > 7:
#             cat.happiness -= 5
#             cat.energy -= 5
#             cat.hunger -= 5
#             cat.hygiene -= 5
#             print(f"{cat.name} is neglected because you overworked. (-5 happiness & energy)")

#         if player.sleep_counter > 6:
#             cat.hunger -= 5
#             cat.hygiene -= 5
#             print(f"{cat.name} is neglected because you overslept. (-5 hunger & hygiene)")

#         print('\n')
#         print(f"--- menu (moves left: {moves_left}) ---")
#         print("1. show cat stats (free)")
#         print("2. show your stats (free)")
#         print(f"3. feed cat (${feed_cost})")
#         print(f"4. small toy play (${toy_small_cost})")
#         print(f"5. large toy play (${toy_large_cost})")
#         print(f"6. give treat (${treat_cost})")
#         print(f"7. play with cat (${play_cost})")
#         print("8. work (+$25, -15 energy)")
#         print("9. sleep (skip rest of day, +25 energy, -$5)")
#         print("10. quit")
#         print("11. i hate cats")

#         choice = input("choose option: ")
#         last_action = choice
#         valid_move = True

#         if choice == "1":
#             cat.show_stats()

#         elif choice == "2":
#             print(f"--- {player.name}'s stats ---")
#             print(f"hunger: {player.hunger}")
#             print(f"work:   {player.work}")
#             print(f"energy: {player.energy}")
#             print(f"money:  {player.money}")
#             print("---------------------------")

#         elif choice == "3":
#             if player.money >= feed_cost:
#                 player.money -= feed_cost
#                 cat.hunger += 25
#                 print("you fed the cat. +25 hunger.")
#             else:
#                 print("you are too broke to feed the cat.")
#                 valid_move = False

#         elif choice == "4":
#             if player.money >= toy_small_cost:
#                 player.money -= toy_small_cost
#                 cat.happiness += 15
#                 print("you gave a small toy. +15 happiness.")
#             else:
#                 print("can't afford the small toy.")
#                 valid_move = False

#         elif choice == "5":
#             if player.money >= toy_large_cost:
#                 player.money -= toy_large_cost
#                 cat.happiness += 30
#                 print("you gave a large toy. +30 happiness.")
#             else:
#                 print("can't afford the large toy.")
#                 valid_move = False

#         elif choice == "6":
#             if player.money >= treat_cost:
#                 player.money -= treat_cost
#                 cat.happiness += 25
#                 cat.hygiene += 5
#                 print("you gave a treat. +25 happiness, +5 hygiene.")
#             else:
#                 print("can't afford the treat.")
#                 valid_move = False

#         elif choice == "7":
#             if player.money >= play_cost:
#                 player.money -= play_cost
#                 cat.happiness += 10
#                 print("you played with the cat. +10 happiness.")
#             else:
#                 print("you can't even afford to play with the cat.")
#                 valid_move = False

#         elif choice == "8":
#             player.work_action()

#         elif choice == "9":
#             player.sleep()
#             moves_left = 0
#             continue

#         elif choice == "10":
#             confirm = input("quit? (yes/no): ").lower()
#             if confirm in ("yes", "y"):
#                 print("thanks for playing.")
#                 break
#             valid_move = False

#         elif choice == "11":
#             confirm = input("are you sure you want to kill the cat? (yes/no): ").lower()
#             if confirm in ("yes", "y"):
#                 print("the cats revolt. you are dead.")
#                 break
#             else:
#                 print("You hesitated. The cats do not forgive for your 愚蠢. You died by being killed by fluffiness from cats.")
#                 break

#         else:
#             print("invalid choice.")
#             valid_move = False

#         if valid_move:
#             moves_left -= 1

        
        
        
        
        
#         # day
#         if moves_left == 0:
#             cat.age_days += 1
#             print(f"a day has passed. your cat is now {cat.age_days} days old.")

#             if last_action = "9":
#                 player.hunger -= 5
#                 player.energy -= 5
#                 print("you did not sleep at the end of the day. -5 hunger and -5 energy.")

#             moves_left = 17
            
#             print("a new day begins.")

# game()

















# # examples from internet so make stuff in term to look better
# """ 
# print("First line")
# print('\n')
# print("Second line") 
# """





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
    def __init__(self, name, hunger=100, work=100, energy=100, money=50):
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
        self.work += 10
        self.money += 35
        self.energy -= 10
        print("You worked. +$35, -10 energy.")

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
    print("Welcome to Serving Cats.")
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

    moves_left = 17

    while True:

        # check death first
        if check_death(player, cat):
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
        print ("9. sleep (end day)")
        print ("10. quit")
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
                print("Too poor to play??")
                valid_move = False

        elif choice == "8":
            player.work_action()

        elif choice == "9":
            player.sleep()
            moves_left = 0  # end the day

        elif choice == "10":
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

            # daily allowance helps with money balance
            player.money += 5
            print("You received a daily cat-llowance: +$5")


            # check for final 50/50 ending
            if cat.age_days >= 74:
                print(f"{cat.name} has reached old age at {cat.age_days} days.")

                if random.random() < 0.5:
                    print("You've won.")
                else:
                    print(f"{cat.name} becomes the ruler of the household... The cats wins.")
                
                break



            print("A new day begins.")
            moves_left = 17


game()
