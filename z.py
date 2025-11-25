import random

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# invent/shop

class Inventory:
    def __init__(self):
        self.items = {}

    def add_item(self, item_name, quantity=1):
        if item_name not in self.items:
            self.items[item_name] = 0
        self.items[item_name] += quantity

    def remove_item(self, item_name, quantity=1):
        if item_name in self.items:
            self.items[item_name] -= quantity
            if self.items[item_name] <= 0:
                del self.items[item_name]

    def show_inventory(self):
        print("------ INVENTORY ------")
        if not self.items:
            print("Your inventory is empty.")
        else:
            for name, qty in self.items.items():
                print(f"{name} x{qty}")
        print("-----------------------")


class Shop:
    def __init__(self):
        self.store_items = {
            "Basic Food": {"price": 10, "category": "food", "value": 20},
            "Premium Food": {"price": 25, "category": "food", "value": 40},
            "Small Toy": {"price": 15, "category": "toy", "value": 15},
            "Large Toy": {"price": 30, "category": "toy", "value": 30},
            "Treat Pack": {"price": 20, "category": "treat", "value": 25},
        }

    def show_shop(self):
        print("------ SHOP ------")
        for i, (item, data) in enumerate(self.store_items.items(), start=1):
            print(f"{i}. {item} - ${data['price']} ({data['category']})")
        print("0. Exit Shop")
        print("------------------")

    def buy(self, player, inventory):
        while True:
            self.show_shop()
            choice = input("Enter number to buy (Input '0' to exit): ")

            if not choice.isdigit():
                print("Please enter a valid number.")
                continue

            choice = int(choice)
            if choice == 0:
                return

            items_list = list(self.store_items.items())
            if 1 <= choice <= len(items_list):
                item_name, item_data = items_list[choice - 1]
                price = item_data["price"]
                if player.money < price:
                    print("You don't have enough money.")
                    continue

                player.money -= price
                inventory.add_item(item_name, 1)
                print(f"You bought {item_name}.")
                return
            else:
                print("Invalid selection. Try again.")


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# pet class

class Pet:
    def __init__(self, name, happiness=100, hunger=100, hygiene=100, energy=100):
        self.name = name
        self.happiness = happiness
        self.hunger = hunger
        self.hygiene = hygiene
        self.energy = energy

    def apply_losses(self):
        self.happiness -= random.randint(4, 10)
        self.hunger -= random.randint(10, 20)
        self.hygiene -= random.randint(5, 15)
        self.energy -= random.randint(5, 15)

    def show_stats(self):
        print(f"--- {self.name}'s Stats ---")
        print(f"Happiness: {self.happiness}")
        print(f"Hunger:    {self.hunger}")
        print(f"Hygiene:   {self.hygiene}")
        print(f"Energy:    {self.energy}")
        print("---------------------------")

    def is_alive(self):
        return self.happiness > 0 and self.hunger > 0 and self.hygiene > 0 and self.energy > 0


# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# hooman class

class Hooman:
    def __init__(self, name, hunger=100, work=100, energy=100, money=100):
        self.name = name
        self.hunger = hunger
        self.work = work
        self.energy = energy
        self.money = money
        self.work_counter = 0
        self.sleep_counter = 0

    def statsloss(self):
        self.energy -= random.randint(20, 40)
        self.hunger -= random.randint(1, 10)
        self.work -= random.randint(20, 50)

    def work_action(self):
        self.work += 20
        self.money += 25
        self.energy -= 15
        self.work_counter += 1
        print(f"You worked! Money earned, energy decreased.")

    def sleep(self):
        self.energy += 25
        self.sleep_counter += 1
        print("You slept and regained energy.")

    def show_stats(self):
        print(f"--- {self.name}'s Stats ---")
        print(f"Hunger: {self.hunger}")
        print(f"Work:   {self.work}")
        print(f"Energy: {self.energy}")
        print(f"Money:  {self.money}")
        print("---------------------------")


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# loop

def game():
    print("Welcome to serving cats. You better not let your cat die.")
    print ("Each action like checking something or buying something will affect yours and your cat's stats || This is because YOUR CAT IS DEMANDING. If you neglect ur cat, you die.")
    player_name = input("Enter your name: ")
    cat_name = input("Enter your cat's name: ")

    player = Hooman(player_name)
    cat = Pet(cat_name)
    inventory = Inventory()
    shop = Shop()

    while True:
        player.statsloss()
        cat.apply_losses()

        #p.stat penalties for human overuse
        if player.work_counter > 7:
            cat.happiness -= 5
            cat.energy -= 5
            print(f"{cat.name} is neglected because you overworked! (-5 happiness & energy)")
        if player.sleep_counter > 6:
            cat.hunger -= 5
            cat.hygiene -= 5
            print(f"{cat.name} is neglected because you overslept! (-5 hunger & hygiene)")

        #pet death yesno
        if not cat.is_alive():
            print(f"Your cat {cat.name} has fallen ill due to neglect. You do not deserve to live. You've died.")
            break

        print("--- MENU ---")
        print ("\n")
        print("1. Show Cat Stats")
        print("2. Show Your Stats")
        print("3. Inventory")
        print("4. Go to Shop")
        print("5. Use an Item")
        print("6. Play With Cat")
        print("7. Work")
        print("8. Sleep")
        print("9. Quit")
        print("10. I hate cats option.") 

        choice = input("Choose option: ")

        if choice == "1":
            cat.show_stats()

        elif choice == "2":
            player.show_stats()

        elif choice == "3":
            inventory.show_inventory()

        elif choice == "4":
            shop.buy(player, inventory)

        elif choice == "5":
            item_list = list(inventory.items.items())
            if not item_list:
                print("Inventory is empty.")
                continue
            for i, (name, qty) in enumerate(item_list, start=1):
                print(f"{i}. {name} x{qty}")
            print("0. Cancel")
            item_choice = input("Choose item number: ")
            if not item_choice.isdigit():
                continue
            item_choice = int(item_choice)
            if item_choice == 0:
                continue
            if 1 <= item_choice <= len(item_list):
                item_name, qty = item_list[item_choice - 1]
                data = shop.store_items.get(item_name)
                if data:
                    category = data["category"]
                    value = data["value"]
                    if category == "food":
                        cat.hunger += value
                        print(f"You fed {cat.name}. Hunger increased.")
                    elif category == "toy":
                        cat.happiness += value
                        print(f"You played with {cat.name}. Happiness increased.")
                    elif category == "treat":
                        cat.happiness += value
                        cat.hygiene += value // 4
                        print(f"You gave a treat. Happiness + Hygiene increased.")
                    inventory.remove_item(item_name)
            else:
                print("Invalid item selection.")

        elif choice == "6":
            cat.happiness += 10
            print(f"You played with {cat.name}! Happiness increased.")

        elif choice == "7":
            player.work_action()

        elif choice == "8":
            player.sleep()

        elif choice == "9":
            confirm = input("Are you sure you want to quit? (yes/no): ").lower()
            if confirm in ("yes", "y"):
                print("Thank you for playing.")
                break
            else:
                print ("")
                continue

        elif choice == "10":
            confirm = input("Are you SURE you want to kill the cat? (yes/no): ").lower()
            if confirm in ("yes", "y"):
                print("The cat revolution begins! The cats rise up and you have been exterminated for your crimes. ")
                break
            else:
                print("You decided not to harm the cat. But you still thought to harm us. You have been exterminated.")
                break
        else:
            print("Invalid choice.")



game()
















# examples from internet so make stuff in term to look better
""" 
print("First line")
print('\n')
print("Second line") 
"""