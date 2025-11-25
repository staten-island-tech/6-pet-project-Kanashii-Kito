import random
import time

# -----------------------------------------------------------------------------------------------------------------------------------------------------
# ITEM / INVENTORY / SHOP TEMPLATES
# -----------------------------------------------------------------------------------------------------------------------------------------------------

class Item:
    
    """Base template for any item in the game."""

    def __init__(self, name, category, effect_value, description):
        self.name = name
        self.category = category    # "food", "toy", "treat", etc.
        self.effect_value = effect_value
        self.description = description


class Inventory:

    """Stores player's items."""

    def __init__(self):
        self.items = {}  
        # DO NOT FORGET -> Ex. {"item_name": quantity}

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
        print("\n--- INVENTORY ---")
        if not self.items:
            print("Your inventory is empty.")
        else:
            for name, qty in self.items.items():
                print(f"{name} x{qty}")
        print("------------------")


# -----------------------------------------------------------------------------------------------------------------------------------------------------
# SHOP
# -----------------------------------------------------------------------------------------------------------------------------------------------------
class Shop:
    """Simple shop template where you can define your own items."""

    def __init__(self):
        self.store_items = {
            "Basic Food": {"price": 10, "category": "food", "value": 20},
            "Premium Food": {"price": 25, "category": "food", "value": 40},
            "Small Toy": {"price": 15, "category": "toy", "value": 15},
            "Large Toy": {"price": 30, "category": "toy", "value": 30},
            "Treat Pack": {"price": 20, "category": "treat", "value": 25},
            #  Add a couple more items here later
        }

    def show_shop(self):
        print("--- SHOP ---")
        for item, data in self.store_items.items():
            print(f"{item} - ${data['price']} ({data['category']})")
        print("-------------")

    def buy(self, player, inventory):
        self.show_shop()
        choice = input("Enter item name to buy (or 'exit'): ")

        if choice == "exit":
            return

        if choice not in self.store_items:
            print("That item doesn't exist.")
            return

        item_data = self.store_items[choice]
        price = item_data["price"]

        if player.money < price:
            print("You don't have enough money!")
            return

        player.money -= price
        inventory.add_item(choice, 1)
        print(f"You bought {choice}!")


# -----------------------------------------------------------------------------------------------------------------------------------------------------
# ACHIEVEMENT SYSTEM
# -----------------------------------------------------------------------------------------------------------------------------------------------------
class Achievements:
    """achievements system, note for self: please don't break this again"""

    def __init__(self):
        self.unlocked = []

        self.achievement_list = [
            {"name": "First Purchase", "condition": "bought_item"},
            {"name": "Rich Human", "condition": "money_over_500"},
            #  add more later or not ur choice
        ]

        self.play_count = 0
        self.items_bought = 0

    def check(self, player, pet):
        """TO SELF: REMEMBER TO : Call this frequently to check if new achieves unlock."""

        new = []

        for ach in self.achievement_list:
            if ach["name"] in self.unlocked:
                continue

            cond = ach["condition"]

            if cond == "bought_item" and self.items_bought >= 1:
                new.append(ach["name"])
            if cond == "played_10_times" and self.play_count >= 10:
                new.append(ach["name"])
            if cond == "money_over_500" and player.money >= 500:
                new.append(ach["name"])

        for a in new:
            self.unlocked.append(a)
            print(f" ACHIEVEMENT UNLOCKED: {a}!\n")


# -----------------------------------------------------------------------------------------------------------------------------------------------------
# PET CLASS
# -----------------------------------------------------------------------------------------------------------------------------------------------------
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


# -----------------------------------------------------------------------------------------------------------------------------------------------------
# HUMAN CLASS
# -----------------------------------------------------------------------------------------------------------------------------------------------------
class Hooman:
    def __init__(self, name, hunger=100, work=100, energy=100, money=100):
        self.name = name
        self.hunger = hunger
        self.work = work
        self.energy = energy
        self.money = money

    def statsloss(self):
        self.energy -= random.randint(2, 6)
        self.hunger -= random.randint(3, 8)
        self.work -= random.randint(2, 5)

    def show_stats(self):
        print(f"--- {self.name}'s Stats ---")
        print(f"Hunger: {self.hunger}")
        print(f"Work:   {self.work}")
        print(f"Energy: {self.energy}")
        print(f"Money:  {self.money}")
        print("---------------------------")


# -----------------------------------------------------------------------------------------------------------------------------------------------------
# GAME LOOP
# -----------------------------------------------------------------------------------------------------------------------------------------------------
def game():
    print("Welcome")
# add another print with other things later

    player_name = input("Enter your name: ")
    cat_name = input("Enter your cat's name: ")

    player = Hooman(player_name)
    cat = Pet(cat_name)
    inventory = Inventory()
    shop = Shop()
    achievements = Achievements()

    while True:
        player.statsloss()
        cat.apply_losses()

        print("--- MENU ---")
        print("1. Show Cat Stats")
        print("2. Show Your Stats")
        print("3. Inventory")
        print("4. Go to Shop")
        print("5. Use an Item")
        print("6. Play With Cat")
        print("7. Quit")
        choice = input("Choose option: ")

        if choice == "1":
            cat.show_stats()

        elif choice == "2":
            player.show_stats()

        elif choice == "3":
            inventory.show_inventory()

        elif choice == "4":
            shop.buy(player, inventory)
            achievements.items_bought += 1

        elif choice == "5":
            inventory.show_inventory()
            item_name = input("Choose item to use: ")

            if item_name in inventory.items:
                data = shop.store_items.get(item_name)

                if not data:
                    print("Item has no defined effect yet.")
                else:
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
                print("You don't have that item.")

        elif choice == "6":
            cat.happiness += 10
            achievements.play_count += 1
            print(f"You played with {cat.name}! Happiness increased.")

        elif choice == "7":
            # -----------------------------
            # Quit Confirmation Prompt
            # --------------------------
            confirm = input("Are you sure you want to quit? (yes/no): ").lower()

            if confirm in ("yes", "y"):
                print("Game || Killed//Quitted")
                break
            else:
                print("Quit cancelled. Returning to menu...")

        else:
            print("Invalid choice.")

        achievements.check(player, cat)

        time.sleep(0.5)


game()
