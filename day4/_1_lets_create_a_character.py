#JSON: JavaScrip Object Notation
import json
class Character:
    def __init__(self, name, str, vit, cha, streetwise, fun_factor, fortune, skill_hacking, fear_flashing):
        self.name = name
        self.str = int(str)
        self.vit = int(vit)
        self.cha = cha
        self.streetwise = streetwise
        self.fun_factor = fun_factor
        self.fortune = fortune
        self.skill_hacking = skill_hacking # >:]
        self.fear_flashing = fear_flashing
    
    def attack(self, char):
        print(f"You deal {self.str} dmg to {char.name}")
        char.vit -= self.str

# stat_list = []
# for i in range(8):
#     stat_list.append(input("Add next stat: "))


# new_char = Character(stat_list[0], stat_list[1], stat_list[2], stat_list[3], stat_list[4], stat_list[5], stat_list[6], stat_list[7])

# char = {
#     "name" : "something",
#     "strength" : 15
# }

# with open("new_char.json", "w") as file:
#     json.dump(new_char.__dict__, file)
        

with open("new_char.json", "r") as file:
    loaded_char_dictionary = json.load(file)

print(loaded_char_dictionary)

loaded_character = Character(loaded_char_dictionary["name"], 
                             loaded_char_dictionary["str"], 
                             loaded_char_dictionary["vit"],
                             loaded_char_dictionary["cha"],
                             loaded_char_dictionary["streetwise"],
                             loaded_char_dictionary["fun_factor"],
                             loaded_char_dictionary["fortune"],
                             loaded_char_dictionary["skill_hacking"],
                             loaded_char_dictionary["fear_flashing"])

print(loaded_character.name)
print(loaded_character.vit)
loaded_character.attack(loaded_character)
print(loaded_character.vit)

#API Application Programming Interface