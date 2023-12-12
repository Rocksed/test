import random
from list_of import digits, letters


class Randomizer:

    def __init__(self, list_of_digits, list_of_letters):
        self.list_of_digits = list_of_digits
        self.list_of_letters = list_of_letters

    def random_code(self):
        bonus_code = []
        while True:
            bonus_code += random.choices(self.list_of_digits)
            bonus_code += random.choices(self.list_of_letters)
            bonus_code += random.choices(self.list_of_digits)
            bonus_code += random.choices(self.list_of_letters)
            if len(bonus_code) == 19:
                break
            bonus_code += '-'
        return bonus_code

    def normal_div(self):
        normal_code = ""
        for _ in self.random_code():
            normal_code += _
        return normal_code


item = Randomizer(digits, letters)
result = item.random_code()

print(item.normal_div())
f = open('code.txt', 'a')
f.write(item.normal_div() + '\n')
f.close()
