
import random
class Pet:
    def __init__(pet, happiness, hunger, hygiene, energy):
        pet.happiness = happiness
        pet.hunger = hunger  
        pet.hygiene = hygiene
        pet.energy = energy
    happinessloss = random.randint (4, 10)
    hungerloss = random.randint (10,20)
    hygieneloss = random.randint (20, 30)
    energyloss = random.randint (20, 25)

# Pet
    def __init__(pet, name, happiness):
        pet.name = name
        pet.__happiness = happiness  # private attribute
    def play(pet, amount):
        """Increase happiness by a given amount."""
        if amount > 0:
            pet.__happiness += amount
    def treat(pet, amount):
        """Increase happiness by a given amount."""
        if amount > 0:
            pet.__happiness += 5
    def show_happiness(pet):
        print(f"{pet.name} has a happiness level of {pet.__happiness}")


class hooman :
    def __init__(self, name, p_hunger, p_work, p_energy, money):
        self.money = money
        self.name = name
        self.p_hunger = p_hunger
        self.p_work = p_work
        self.p_energy = p_energy

    p_energy = 100
    p_hunger = 100
    p_work = 100
    money = 100

    def statsloss (self, p_hunger, p_work, p_energy, money):
        p_energy -= random.randint (10,20)
        p_hunger -= random.randint (20, 30)
        p_work -= random.randint (10,20)
        money -= random.randint (1,10)

        

    print ("Welcome to this lovely game." \
    " You're a human and you WILL be taking care of a cat. " \
    "If you do not consent to taking care of said cat, please throw yourself out a window or the cats will attack you. ")


        


#     def buy (self, shop, inventory):
#         self.shop = shop
#         self.inventory = inventory
    
#     shop = [
# {
#     "Name": "Pet Food",
#     "Cost": 2499.99,
#     "Department": "Pet", 
#     "Description": "Food for ur pet.",
# },

# {
#     "Name": "Premium Pet Food",
#     "Cost": 4999.99,
#     "Department": "Pet", 
#     "Description": "Better food for ur pet.",
# },

# {
#     "Name": "Treats",
#     "Cost": 19999.99,
#     "Department": "Pet", 
#     "Description": "Pet Treats.",
# },

# {
#     "Name": "Pet Insurance",
#     "Cost": 99999.99,
#     "Department": "Pet", 
#     "Description": "Insurance for your Pet so it doesn't kill you if you fail ."
# },

# {
#     "Name": "Contract || Contract",
#     "Cost": 0.00,
#     "Department": "Kitt e", 
#     "Description": "Your contract with your kitty // cat."
# },
# ]