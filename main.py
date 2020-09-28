from abc import abstractmethod


class Animal:
    def __init__(self, name='', weight=0):
        self.name = name
        self.weight = weight

    def feed(self, food_qty):
        self.weight += food_qty

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_weight(self):
        return self.weight

    # making abstract method to prevent instantiate from this class
    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def make_specific_class_actions(self):
        pass


class MilkingAnimal(Animal):
    def do_milk(self):
        return 'доится'

    def make_specific_class_actions(self):
        return self.do_milk() + ' и делает ' + self.make_sound()

    @abstractmethod
    def make_sound(self):
        pass


class WoolenAnimal(Animal):
    def do_shave(self):
        return 'стрижет шерсть'

    def make_specific_class_actions(self):
        return self.do_shave() + ' и делает ' + self.make_sound()

    @abstractmethod
    def make_sound(self):
        pass


class LayingAnimal(Animal):
    def do_lay(self):
        return 'несет яйца'

    def make_specific_class_actions(self):
        return self.do_lay() + ' и делает ' + self.make_sound()

    @abstractmethod
    def make_sound(self):
        pass


class Goose(LayingAnimal):
    type = 'Гусь'

    def make_sound(self):
        return 'га-га'


class Cow(MilkingAnimal):
    type = 'Корова'

    def make_sound(self):
        return 'му-му'


class Sheep(WoolenAnimal, MilkingAnimal):
    type = 'Овца'

    def make_sound(self):
        return 'бе-бе'

    def make_specific_class_actions(self):
        return super().do_shave() + ', ' + super().do_milk() + ' и делает ' + self.make_sound()


class Hen(LayingAnimal):
    type = 'Курица'

    def make_sound(self):
        return 'ко-ко'


class Goat(MilkingAnimal):
    type = 'Коза'

    def make_sound(self):
        return 'ме-ме'


class Duck(LayingAnimal):
    type = 'Утка'

    def make_sound(self):
        return 'кря-кря'


farm = [Goose('Серый', 4),
        Goose('Белый', 5),
        Cow('Манька', 200),
        Sheep('Барашек', 10),
        Sheep('Кудрявый', 12),
        Hen('Ко-Ко', 2),
        Hen('Кукареку', 1),
        Goat('Рога', 30),
        Goat('Копыта', 25),
        Duck('Кряква', 3)]

for animal in farm:
    animal.feed(1)
    print(animal.type + ' "' + animal.name + '" ' + animal.make_specific_class_actions())

total_weight = 0

if len(farm) > 0:
    # setting first animal as heaviest by default
    heaviest_animal = farm[0] if len(farm) > 0 else None
    for animal in farm:
        total_weight += animal.weight
        heaviest_animal = animal if heaviest_animal.weight < animal.weight else heaviest_animal

    print(f'\nОбщий вес животных на ферме: {total_weight}')
    print(f'Самое тяжелое животное: {heaviest_animal.name}')
else:
    print(f'\nНа ферме никого нет!')
